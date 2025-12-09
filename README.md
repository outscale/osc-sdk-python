[![Project Graduated](https://docs.outscale.com/fr/userguide/_images/Project-Graduated-green.svg)](https://docs.outscale.com/en/userguide/Open-Source-Projects.html) [![](https://dcbadge.limes.pink/api/server/HUVtY5gT6s?style=flat&theme=default-inverted)](https://discord.gg/HUVtY5gT6s)

# Outscale Python SDK

<p align="center">
  <img alt="Outscale Python SDK" src="https://img.icons8.com/?size=100&id=2866&format=png&color=000000" width="100px">
</p>

---

## 🌐 Links

- Documentation: <https://docs.outscale.com/api.html?python#3ds-outscale-api>
- Project repository: <https://github.com/outscale/osc-sdk-python>
- Outscale website: <https://outscale.com/>
- Join our community on [Discord](https://discord.gg/HUVtY5gT6s)

---

## 📄 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Examples](#-examples)
- [Known Issues & Troubleshooting](#-known-issues--troubleshooting)
- [License](#-license)
- [Contributing](#-contributing)

---

## 🧭 Overview

**Outscale Python SDK** (`osc-sdk-python`) is the official Python SDK to interact with the [OUTSCALE API](https://docs.outscale.com/api.html?python#3ds-outscale-api).

It allows you to:

- Configure multiple profiles through environment variables or credential files.
- Customize retry and rate-limit behavior.
- Enable detailed logging of requests and responses.

You will need an Outscale account and API credentials. If you do not have one yet, please visit the [Outscale website](https://outscale.com/).

---

## ✅ Requirements

- Python 3.x
- `pip` (Python package manager)
- Access to the OUTSCALE API (valid access key / secret key or basic auth)
- Network access to the Outscale API endpoints

---

## ⚙ Installation

### Option 1: Install from PyPI

Install the pre-built Python package:

```bash
pip install osc-sdk-python
````

### Option 2: Install from source

Clone the repository and build the package:

```bash
git clone https://github.com/outscale/osc-sdk-python.git
cd osc-sdk-python
make package
```

Then install the built wheel:

```bash
pip install dist/osc_sdk_python-0.38.1-py3-none-any.whl
```

---

## 🛠 Configuration

When you use the SDK, you can choose a **profile**. Profiles can be defined via **environment variables** or in a **credentials file**.
Environment variables take precedence over files.

In the credentials file, you can set a default profile named `default`. It will be used if you do not explicitly specify a profile.

### Environment variables

The SDK understands the following environment variables:

```bash
export OSC_PROFILE=<PROFILE>            # default: "default"

# or explicit credentials:
export OSC_ACCESS_KEY=<ACCESS_KEY>
export OSC_SECRET_KEY=<SECRET_KEY>

# optional:
export OSC_REGION=<REGION>              # default: eu-west-2
export OSC_MAX_RETRIES=<INT>            # default: 3
export OSC_RETRY_BACKOFF_FACTOR=<FLOAT> # default: 1.0
export OSC_RETRY_BACKOFF_JITTER=<FLOAT> # default: 3.0
export OSC_RETRY_BACKOFF_MAX=<FLOAT>    # default: 30
```

### Credentials files

By default, the SDK looks for a JSON configuration file at `~/.osc/config.json`.

Example:

```json
{
  "default": {
    "access_key": "<ACCESS_KEY>",
    "secret_key": "<SECRET_KEY>",
    "region": "<REGION>"
  },
  "profile_1": {
    "access_key": "<ACCESS_KEY>",
    "secret_key": "<SECRET_KEY>",
    "region": "<REGION>"
  },
  "profile_2": {
    "access_key": "<ACCESS_KEY>",
    "secret_key": "<SECRET_KEY>",
    "region": "<REGION>"
  }
}
```

Notes:

* If `~/.osc/config.json` is not found, `~/.oapi_credentials` will be used as a fallback.
* Environment variables have priority over credentials files.

### Basic Authentication

You can also use `osc-sdk-python` with **basic authentication** using your account email and password.
Note that some API calls may be blocked with this method. See the [authentication documentation](https://docs.outscale.com/api#authentication) for more details.

Example:

```python
from osc_sdk_python import Gateway

with Gateway(email="your@email.com", password="yourAccountPassword") as gw:
    keys = gw.ReadAccessKeys()
```

### Retry Options

The following options can be provided when initializing the `Gateway` to customize the retry behavior of the SDK:

* `max_retries` (integer, default `3`)
* `retry_backoff_factor` (float, default `1.0`)
* `retry_backoff_jitter` (float, default `3.0`)
* `retry_backoff_max` (float, default `30`)

These correspond to their counterparts in [`urllib3.util.Retry`](https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html#urllib3.util.Retry).

Example:

```python
from osc_sdk_python import Gateway

gw = Gateway(
    max_retries=5,
    retry_backoff_factor=0.5,
    retry_backoff_jitter=1.0,
    retry_backoff_max=120,
)
```

### Rate Limit Options

You can also configure rate limiting when initializing the `Gateway`:

* `limiter_max_requests` (integer, default `5`)
* `limiter_window` (integer, default `1`)

Example:

```python
from osc_sdk_python import Gateway

gw = Gateway(
    limiter_max_requests=20,
    limiter_window=5,
)
```

More usage patterns and logging examples are documented in:

* [docs/examples.md](docs/examples.md)

---

## 🧪 Examples

Some example topics covered in `docs/examples.md`:

* Listing VMs and volumes
* Using profiles and regions
* Raw calls with `gw.raw("ActionName", **params)`
* Enabling and reading logs

---

## 🧩 Known Issues & Troubleshooting

Common issues (such as UTF-8 / locale errors when reading the API spec) and their workarounds are documented in:

* [docs/troubleshooting.md](docs/troubleshooting.md)

---

## 📜 License

**Outscale Python SDK** is released under the BSD-3-Clause.

© 2025 OUTSCALE SAS

See [LICENSE](./LICENSE) for full details.

---

## 🤝 Contributing

We welcome contributions!

Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before submitting a pull request.
