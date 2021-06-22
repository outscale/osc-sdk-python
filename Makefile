all: help

.PHONY: help
help:
	@echo "Available targets:"
	@echo "- build: build python package"
	@echo "- test: run all tests"
	@echo "- test-pylint: check code with pylint"
	@echo "- test-bandit: security check with bandit"
	@echo "- test-int: run integration tests"
	@echo "- osc-api-update: update to last osc-api version"
	@echo "- clean: clean temp files, venv, etc"

.PHONY: test
test: clean test-pylint test-bandit test-int build
	@echo "All tests: OK"

.PHONY: test-pylint
test-pylint: .venv/ok
	@./tests/test_pylint.sh

.PHONY: test-bandit
test-bandit: .venv/ok
	@./tests/test_bandit.sh

.PHONY: test-int
test-int: .venv/ok init
	./tests/test_int.sh

.PHONY: build
build: .venv/ok init
	@./tests/build.sh

.PHONY: osc-api-update
osc-api-update:
	cd osc_sdk_python/osc-api/; git fetch; git checkout origin/master; cd ..; git add osc-api

.PHONY: init
init: osc_sdk_python/osc-api/outscale.yaml
	@echo Initialization: OK

osc_sdk_python/osc-api/outscale.yaml:
	git submodule update --init .

.venv/ok:
	@./tests/setup_venv.sh

.PHONY: clean
clean:
	@echo cleaning...
	rm -rf .venv osc_sdk.egg-info dist
