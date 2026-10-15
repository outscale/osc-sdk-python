all: help

.PHONY: help
help:
	@echo "Available targets:"
	@echo "- package: build python package"
	@echo "- test: run all tests"
	@echo "- test-lint: check code with ruff"
	@echo "- typecheck: run pyright"
	@echo "- test-int: run integration tests"
	@echo "- codegen: regenerate OSC/OKS clients (ruff check --fix on generated/)"
	@echo "- osc-api-update: update to last osc-api version"
	@echo "- clean: clean temp files, venv, etc"

.PHONY: test
test: clean test-lint test-int package
	@echo "All tests: OK"

.PHONY: codegen
codegen:
	@uv run python -m osc_sdk_python.codegen.generator oks osc --skip-overlay

.PHONY: test-lint
test-lint:
	@uv run ruff check

.PHONY: typecheck
typecheck:
	@uv run pyright osc_sdk_python

.PHONY: test-int
test-int:
	@uv run pytest -s

.PHONY: package
package:
	@uv build

.PHONY: upload-package
upload-package: package
	@uv publish --trusted-publishing=always

.PHONY: clean
clean:
	@echo cleaning...
	rm -rf .venv osc_sdk_python.egg-info dist
