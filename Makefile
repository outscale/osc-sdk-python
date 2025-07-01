all: help

.PHONY: help
help:
	@echo "Available targets:"
	@echo "- package: build python package"
	@echo "- test: run all tests"
	@echo "- test-lint: check code with pylint"
	@echo "- test-int: run integration tests"
	@echo "- osc-api-update: update to last osc-api version"
	@echo "- clean: clean temp files, venv, etc"

.PHONY: test
test: clean test-lint test-int package
	@echo "All tests: OK"

.PHONY: test-lint
test-lint:
	@uv tool run ruff check

.PHONY: test-int
test-int: init
	@uv run pytest -s

.PHONY: package
package: init
	@uv build

.PHONY: upload-package
upload-package: package
	@uv publish --trusted-publishing=always

.PHONY: osc-api-update
osc-api-update:
	cd osc_sdk_python/osc-api/; git fetch; git checkout origin/master; cd ..; git add osc-api

.PHONY: init
init: osc_sdk_python/osc-api/outscale.yaml
	@echo Initialization: OK

osc_sdk_python/osc-api/outscale.yaml:
	git submodule update --init .

.PHONY: clean
clean:
	@echo cleaning...
	rm -rf .venv osc_sdk_python.egg-info dist
