# OUTSCALE Python SDK Architecture

## 1. Purpose

This document describes the architecture of the OUTSCALE Python SDK V2.

SDK V2 moves the Python SDK from a single-service gateway-style interface to a generated, typed, multi-service SDK. The SDK is designed to support OSC, OKS, and future OUTSCALE services from one Python package while keeping synchronous OSC usage available for compatibility.

The main development focus areas are:

- Make async usage the primary SDK experience.
- Generate typed async methods for service operations.
- Keep synchronous calls supported for compatibility with blocking Python applications.
- Replace the single `Gateway` entry point with `Client` and `AsyncClient` service namespaces.
- Support multiple services such as OSC and OKS from one SDK object.
- Allow more services to be added later without redesigning the SDK.
- Support both OSC action-style OpenAPI and REST/path-style OpenAPI.
- Generate request and response models from OpenAPI using Pydantic.
- Keep service-specific differences inside the generator, overlays, service clients, or generated modules.
- Share runtime behavior for credentials, endpoints, authentication, retries, rate limiting, transport, logging, and errors.
- Avoid manual edits to generated code.

## 2. Public API

SDK V2 exposes two main client entry points:

- `AsyncClient`: primary, typed, async-first API.
- `Client`: synchronous compatibility API for blocking usage.

Both clients expose service namespaces:

```text
Client / AsyncClient
  |- osc
  |- oks
  |- future services
```

### Async Usage

Async usage is the main SDK V2 interface. Generated typed methods use `snake_case` names and typed request/response models.

```python
import asyncio

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.osc import ReadVmsRequest


async def main():
    async with AsyncClient(profile="default") as client:
        response = await client.osc.read_vms(ReadVmsRequest())
        for vm in response.vms:
            print(vm.vm_id)


if __name__ == "__main__":
    asyncio.run(main())
```

Async OKS usage follows the same generated typed pattern:

```python
import asyncio

from osc_sdk_python import AsyncClient
from osc_sdk_python.generated.oks import ListProjectsRequest


async def main():
    async with AsyncClient(profile="default") as client:
        projects = await client.oks.list_projects(ListProjectsRequest())
        print(projects)


if __name__ == "__main__":
    asyncio.run(main())
```

Async clients also keep raw calls where needed:

```python
from osc_sdk_python import AsyncClient

async with AsyncClient(profile="default") as client:
    response = await client.osc.raw("ReadVms")
```

### Sync Usage

Sync usage is kept for compatibility. Sync service clients expose dynamic OpenAPI operation methods using the existing action-style names.

```python
from osc_sdk_python import Client

with Client(profile="default") as client:
    vms = client.osc.ReadVms()
    projects = client.oks.ListProjects()
```

Raw sync calls are also supported:

```python
from osc_sdk_python import Client

with Client(profile="default") as client:
    response = client.osc.raw("ReadVms")
```

### Gateway Compatibility

The package may keep `Gateway` and `AsyncGateway` aliases for compatibility, but the SDK V2 architecture should use `Client` and `AsyncClient` as the preferred public entry points. `Client` gives the SDK a stable structure for multi-service support, while `Gateway` represents the older single-service OSC shape.

## 3. High-Level Architecture

```text
User code
  -> Client / AsyncClient
  -> service namespace: osc, oks, ...
  -> generated typed method or compatibility dynamic method
  -> RequestSpec
  -> shared runtime call layer
  -> httpx transport
  -> authentication, retry, rate limiting
  -> response decoding
  -> Pydantic typed response or compatibility dict response
```

The SDK is split into three main areas:

- Public client layer: `Client`, `AsyncClient`, service gateways, and compatibility aliases.
- Generated service layer: async typed mixins and Pydantic models under `osc_sdk_python.generated.*`.
- Runtime layer: request execution, authentication, transport, retries, rate limiting, logging, and errors.

## 4. Package Structure

The SDK V2 structure is organized around shared runtime code and generated service slices.

```text
osc_sdk_python/
  __init__.py
  outscale_gateway.py
  credentials.py
  exceptions.py
  problem.py
  runtime/
    call.py
    request.py
    transport.py
  codegen/
    adapters.py
    generator.py
    ir.py
    overlay.py
  generated/
    osc/
      __init__.py
      async_client.py
      models.py
    oks/
      __init__.py
      async_client.py
      models.py
  resources/
    osc/
      api.yaml
      cfg.yaml / overlay files when needed
    oks/
      api.yaml
      cfg.yaml / overlay files when needed
```

Key responsibilities:

- `outscale_gateway.py` wires service clients and compatibility APIs.
- `runtime.call` owns sync and async request execution.
- `runtime.request` defines `RequestSpec`, the common request description passed to the runtime.
- `runtime.transport` owns httpx auth, retries, rate limiting, and HTTP error conversion.
- `codegen` turns OpenAPI into generated models and async typed methods.
- `generated.<service>` contains generated Pydantic models and async typed mixins.

## 5. Client Layer

`Client` creates synchronous service namespaces:

```text
Client
  |- osc: OutscaleGateway
  |- oks: OksGateway
```

`AsyncClient` creates asynchronous service namespaces:

```text
AsyncClient
  |- osc: AsyncOutscaleGateway
  |- oks: AsyncOksGateway
```

Each service namespace receives the same client configuration arguments, so profile, credentials, endpoint overrides, retry settings, rate limits, and TLS settings are applied consistently.

The async service clients inherit generated typed mixins:

```text
AsyncOutscaleGateway
  -> AsyncOscTypedMixin
  -> AsyncOpenAPIActionAPI

AsyncOksGateway
  -> AsyncOksTypedMixin
  -> AsyncOpenAPIPathAPI
```

This is why async operations can expose typed snake_case methods such as `read_vms` and `list_projects`.

## 6. Sync Compatibility Layer

The sync API keeps dynamic operation dispatch. The service client reads the OpenAPI specification, builds a gateway structure, and resolves method calls dynamically.

```text
client.osc.ReadVms(...)
  -> __getattr__("ReadVms")
  -> validate action and parameters from OpenAPI request schema
  -> Call.api("ReadVms", service="api", ...)
  -> POST /api/v1/ReadVms
  -> return decoded JSON dict
```

For REST/path-style services, the sync layer can map an operation name to method, path, path parameters, query parameters, and request body.

Sync is important, but it is not the primary typed SDK V2 surface. Its role is compatibility and blocking use cases.

## 7. Async Typed Layer

The async typed layer is generated under `osc_sdk_python.generated.<service>`.

For each service, the generator emits:

- `models.py`: Pydantic request and response models.
- `async_client.py`: an async typed mixin with one method per operation.
- `__init__.py`: exported models and the service mixin.

Generated methods:

- Use `snake_case` operation names converted from OpenAPI `operationId`.
- Accept a typed request model or a Python value that Pydantic can validate.
- Serialize request models using OpenAPI aliases.
- Build a `RequestSpec` for the runtime.
- Await the shared async runtime call.
- Validate the decoded response into the generated response model.
- Raise SDK-owned validation or response exceptions when Pydantic validation fails.

Example generated OSC method shape:

```python
response = await client.osc.read_vms(ReadVmsRequest())
```

Example generated OKS method shape:

```python
projects = await client.oks.list_projects(ListProjectsRequest())
```

This design gives async users typed responses such as `response.vms` and `vm.vm_id` instead of only raw dictionaries.

## 8. Generator Architecture

The generator converts service OpenAPI files into Python source code.

```text
resources/<service>/api.yaml or cfg.yaml
  -> load_spec
  -> optional overlay application
  -> PathOperationAdapter
  -> intermediate representation
  -> render Pydantic models
  -> render async typed mixin
  -> render service exports
```

The generator entry point is:

```bash
python -m osc_sdk_python.codegen.generator
```

A subset of services can be generated explicitly:

```bash
python -m osc_sdk_python.codegen.generator oks osc
```

Generated files include a header stating that typed request and response models are async-first and that generated typed methods are exposed on `AsyncClient`.

## 9. Supported OpenAPI Styles

The generator must support two OpenAPI styles.

### 9.1 OSC Action-Style OpenAPI

OSC operations are action-style operations. The OpenAPI path usually matches the action name.

Example shape:

```text
/ReadVms
  operationId: ReadVms
  request schema: ReadVmsRequest
  response schema: ReadVmsResponse
```

The generator recognizes this as an action-body operation when the path name matches the operation ID. In that case, the request model is serialized as the JSON body.

Async typed behavior:

```text
client.osc.read_vms(ReadVmsRequest(...))
  -> RequestSpec(service="api", method="POST", path="/ReadVms", json_body=<request>)
  -> typed ReadVmsResponse
```

Sync compatibility behavior:

```text
client.osc.ReadVms(...)
  -> POST /api/v1/ReadVms
  -> decoded dict
```

The action-style support preserves compatibility while allowing the async SDK to provide typed Python methods.

### 9.2 REST/Path-Style OpenAPI

REST/path-style services describe operations through HTTP methods, paths, parameters, and request bodies.

Example shape:

```text
GET /projects
  operationId: ListProjects
  query parameters: name, status, page, limit
  response schema: ProjectResponseList

POST /projects
  operationId: CreateProject
  request body: CreateProjectRequest body
  response schema: ProjectResponse
```

Async typed behavior:

```text
client.oks.list_projects(ListProjectsRequest(...))
client.oks.create_project(CreateProjectRequest(...))
```

The generator maps:

- Path parameters into `path_params`.
- Query parameters into `query_params`.
- JSON request bodies into `json_body`.
- 2xx JSON responses into generated response models.

## 10. Intermediate Representation

The generator uses a common intermediate representation so OSC action-style and REST/path-style APIs can share code generation.

The IR contains:

- `Field`: Python name, OpenAPI alias, type annotation, and required flag.
- `Model`: model name, field list, or alias type.
- `Operation`: operation ID, generated method name, request model, response model, HTTP method, path, path fields, query fields, body field, and action-body flag.

This common IR is the bridge between OpenAPI differences and consistent Python output.

## 11. OpenAPI Overlays

Some service specifications may need SDK-specific corrections before generation. The overlay loader supports `cfg.yaml` files that point to a base spec and an overlay file.

Overlays can:

- Patch schema details.
- Remove invalid or unsupported nodes.
- Fix names or metadata used by generation.
- Adjust operation or parameter definitions.
- Keep corrections outside generated Python files.

Current release policy: overlays are not applied during release generation. Release builds use the base OpenAPI specifications with `--skip-overlay` because the current overlay files are not yet fully validated and can incorrectly mark optional response fields as required.

The rule remains: fix the spec input, overlay, or generator. Do not manually edit generated code. However, overlays should only become part of release generation after they are reviewed, tested, and proven not to over-constrain generated models.

## 12. Runtime Request Flow

Both sync and async calls use `RequestSpec` to describe the HTTP request.

```text
RequestSpec
  service
  method
  path
  json_body
  query_params
```

The runtime resolves the final endpoint from the profile:

```text
profile.get_endpoint(service) + RequestSpec.path
```

Then it sends the request through httpx using the SDK transport.

Sync flow:

```text
Call.request
  -> httpx.Client
  -> SdkTransport
  -> response JSON
```

Async flow:

```text
AsyncCall.request
  -> httpx.AsyncClient
  -> AsyncSdkTransport
  -> response JSON
```

## 13. Authentication

Authentication is handled by `SdkAuth` in the httpx layer.

The runtime supports:

- OSC signed authentication with access key and secret key.
- IAM V2 credentials for configured services.
- OKS-specific access key and secret key headers.
- Basic authentication when login and password are configured.
- Service-aware signing using region and service name.

Services can choose the right authentication behavior through the `service` value on `RequestSpec`.

## 14. Configuration and Profiles

The SDK uses profiles for credentials, regions, endpoints, and runtime options.

Configuration precedence is:

1. Explicit client constructor arguments.
2. Environment variables.
3. `~/.osc/config.json` or a configured credentials file.
4. SDK defaults.

Important profile fields include:

- `access_key` and `secret_key`.
- `access_key_v2` and `secret_key_v2`.
- `iam_v2_services`.
- `login` and `password`.
- `region`, defaulting to `eu-west-2`.
- `protocol`, defaulting to `https`.
- Service endpoints such as `api`, `oks`, `lbu`, `oos`, `fcu`, `eim`, and `direct_link`.
- TLS verification behavior.

The service endpoint model is important for multi-service support because each namespace can resolve to its own base URL.

## 15. Retry, Rate Limiting, and Transport

The runtime uses httpx transports for both sync and async clients.

Shared transport behavior includes:

- Rate limiting before requests.
- Retry policy with max retries, exponential backoff, jitter, and `Retry-After` support.
- Client/server HTTP error conversion into SDK exceptions.
- Transport error wrapping.
- TLS verification settings from the profile.
- `trust_env=False` to avoid implicit environment proxy behavior unless the SDK chooses to support it explicitly.

Sync uses `SdkTransport`. Async uses `AsyncSdkTransport`.

## 16. Error Model

SDK V2 exposes SDK-owned exceptions rather than leaking raw transport or validation errors.

Important exception categories include:

- `SdkError` as the base SDK exception.
- `SdkUsageError` for incorrect SDK usage.
- `SdkConfigurationError` for missing or invalid configuration.
- `SdkValidationError` for request validation problems.
- `SdkResponseError` for invalid response bodies.
- `SdkTransportError` for low-level transport failures.
- `SdkClientError` for HTTP 4xx responses.
- `SdkServerError` for HTTP 5xx responses.

The runtime also decodes OUTSCALE problem formats where possible and attaches request/response context to HTTP errors.

## 17. Logging

SDK V2 uses Python's standard `logging` module with the `osc_sdk_python` logger.

Request logs include:

- Mode: sync or async.
- Service name.
- HTTP method.
- URI.
- JSON payload.

Logging should remain safe for users. Sensitive values such as credentials and authentication headers must not be exposed in normal logs.

## 18. Testing Strategy

The repository separates tests by behavior area:

```text
tests/
  async_/
    osc/
    oks/
  sync/
    osc/
    oks/
  unit/
```

Testing should cover:

- Async typed OSC operations.
- Async typed OKS operations.
- Sync compatibility methods.
- Raw sync and async calls.
- Client lifecycle and context managers.
- Profile loading and endpoint resolution.
- Authentication behavior.
- RequestSpec path resolution.
- Transport retry and rate limiting.
- OpenAPI adapter behavior.
- Overlay application.
- SDK exception mapping.
- Pydantic request and response validation.

The async tests are especially important because async typed usage is the primary SDK V2 interface.

## 19. Adding a New Service

A new service should be added through the generator pipeline.

Steps:

1. Add `resources/<service>/api.yaml`.
2. Add `cfg.yaml` and overlay files only if the base OpenAPI specification needs SDK-specific corrections; keep release generation on `--skip-overlay` until those overlays are validated.
3. Configure the service name used in `RequestSpec` and endpoint resolution.
4. Run the generator for that service.
5. Add the generated service package under `osc_sdk_python.generated.<service>`.
6. Add the async typed mixin to the async service gateway.
7. Register the service namespace on `Client` and `AsyncClient`.
8. Add sync compatibility behavior if the service needs blocking support.
9. Add async, sync, and generator tests.
10. Update README and examples.

Future services should fit into the same client and runtime architecture rather than creating separate one-off SDK clients.

## 20. Versioning and Compatibility

SDK V2 should follow semantic versioning.

Compatibility rules:

- Async typed APIs are the main SDK V2 direction.
- Sync support remains available for compatibility.
- `Gateway` compatibility can remain, but `Client` and `AsyncClient` should be the preferred V2 entry points.
- Breaking changes require a major version bump or a migration path.
- Generated code should be reproducible from the intended release inputs, generator flags, templates, and generator code.
- Generated files should not be manually edited.

## 21. Notes

- Release generation currently uses `--skip-overlay` for OSC and OKS until overlays are redesigned and validated.
- Async profile or credential updates could be improved: `AsyncCall.update_profile()` recreates the underlying httpx.AsyncClient without explicitly closing the previous instance. Since AsyncClient requires await client.aclose(), consider introducing an async update_profile() method or another lifecycle mechanism to ensure the previous client is cleaned up safely.

## 22. Summary

The OUTSCALE Python SDK V2 is an async-first, generated, typed, multi-service SDK.

`AsyncClient` is the primary interface and exposes typed snake_case operations generated from OpenAPI, such as `client.osc.read_vms(...)` and `client.oks.list_projects(...)`. `Client` keeps synchronous compatibility through service namespaces and dynamic operation methods such as `client.osc.ReadVms(...)`.

The generator supports both OSC action-style OpenAPI and REST/path-style OpenAPI by normalizing them into a shared intermediate representation. The runtime then applies common configuration, endpoint resolution, authentication, retries, rate limiting, logging, error handling, and httpx transport behavior across all services.

