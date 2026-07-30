import json

import pytest

from osc_sdk_python import Client
from osc_sdk_python.credentials import Profile
from osc_sdk_python.exceptions import SdkConfigurationError


def test_default_region_and_protocol_are_used(monkeypatch):
    """Test default region and protocol are set when no config is provided"""
    monkeypatch.delenv("OSC_CONFIG_FILE", raising=False)
    monkeypatch.delenv("OSC_PROFILE", raising=False)
    monkeypatch.delenv("OSC_REGION", raising=False)
    monkeypatch.delenv("OSC_PROTOCOL", raising=False)

    profile = Profile.from_standard_configuration(None, None)

    assert profile.region == "eu-west-2"
    assert profile.protocol == "https"


def test_environment_values_override_defaults(monkeypatch):
    """Test profile values can be loaded from environment variables"""
    monkeypatch.setenv("OSC_ACCESS_KEY", "env-ak")
    monkeypatch.setenv("OSC_SECRET_KEY", "env-sk")
    monkeypatch.setenv("OSC_REGION", "cloudgouv-eu-west-1")
    monkeypatch.setenv("OSC_PROTOCOL", "http")
    monkeypatch.setenv("OSC_ENDPOINT_API", "https://osc.example.test")
    monkeypatch.setenv("OSC_ENDPOINT_OKS", "https://oks.example.test")
    monkeypatch.delenv("OSC_CONFIG_FILE", raising=False)
    monkeypatch.delenv("OSC_PROFILE", raising=False)

    profile = Profile.from_standard_configuration(None, None)

    assert profile.access_key == "env-ak"
    assert profile.secret_key == "env-sk"
    assert profile.region == "cloudgouv-eu-west-1"
    assert profile.protocol == "http"
    assert profile.get_endpoint("api") == "https://osc.example.test"
    assert profile.get_endpoint("oks") == "https://oks.example.test"


def test_profile_file_loading(tmp_path, monkeypatch):
    """Test profile values can be loaded from a config file"""
    monkeypatch.delenv("OSC_ACCESS_KEY", raising=False)
    monkeypatch.delenv("OSC_SECRET_KEY", raising=False)
    monkeypatch.delenv("OSC_REGION", raising=False)
    monkeypatch.delenv("OSC_PROTOCOL", raising=False)
    monkeypatch.delenv("OSC_ENDPOINT_API", raising=False)

    config = tmp_path / "config.json"
    config.write_text(
        json.dumps(
            {
                "default": {
                    "access_key": "file-ak",
                    "secret_key": "file-sk",
                    "region": "eu-west-2",
                    "protocol": "https",
                }
            }
        )
    )

    profile = Profile.from_standard_configuration(str(config), "default")

    assert profile.access_key == "file-ak"
    assert profile.secret_key == "file-sk"
    assert profile.region == "eu-west-2"


def test_environment_values_override_profile_file(tmp_path, monkeypatch):
    """Test environment variables take priority over config file values"""
    config = tmp_path / "config.json"
    config.write_text(
        json.dumps(
            {
                "default": {
                    "access_key": "file-ak",
                    "secret_key": "file-sk",
                    "region": "file-region",
                    "protocol": "https",
                    "endpoints": {
                        "api": "https://file-osc.example.test",
                    },
                }
            }
        )
    )

    monkeypatch.setenv("OSC_ACCESS_KEY", "env-ak")
    monkeypatch.setenv("OSC_SECRET_KEY", "env-sk")
    monkeypatch.setenv("OSC_REGION", "env-region")
    monkeypatch.setenv("OSC_PROTOCOL", "http")
    monkeypatch.setenv("OSC_ENDPOINT_API", "https://env-osc.example.test")

    profile = Profile.from_standard_configuration(str(config), "default")

    assert profile.access_key == "env-ak"
    assert profile.secret_key == "env-sk"
    assert profile.region == "env-region"
    assert profile.protocol == "http"
    assert profile.get_endpoint("api") == "https://env-osc.example.test"


def test_constructor_values_override_environment_and_profile_file(
    tmp_path, monkeypatch
):
    """Test explicit constructor values have the highest priority"""
    config = tmp_path / "config.json"
    config.write_text(
        json.dumps(
            {
                "default": {
                    "access_key": "file-ak",
                    "secret_key": "file-sk",
                    "region": "file-region",
                    "protocol": "https",
                }
            }
        )
    )

    monkeypatch.setenv("OSC_ACCESS_KEY", "env-ak")
    monkeypatch.setenv("OSC_SECRET_KEY", "env-sk")
    monkeypatch.setenv("OSC_REGION", "env-region")

    client = Client(
        path=str(config),
        profile="default",
        access_key="arg-ak",
        secret_key="arg-sk",
        region="arg-region",
    )
    try:
        assert client.osc.profile.access_key == "arg-ak"
        assert client.osc.profile.secret_key == "arg-sk"
        assert client.osc.profile.region == "arg-region"
        assert client.oks.profile.access_key == "arg-ak"
        assert client.oks.profile.secret_key == "arg-sk"
        assert client.oks.profile.region == "arg-region"
    finally:
        client.close()


def test_missing_default_config_is_ignored(monkeypatch):
    """Test missing default config falls back to defaults"""
    monkeypatch.delenv("OSC_CONFIG_FILE", raising=False)
    monkeypatch.delenv("OSC_PROFILE", raising=False)

    profile = Profile.from_standard_configuration(None, None)

    assert profile.region == "eu-west-2"
    assert profile.protocol == "https"


def test_missing_explicit_profile_raises(tmp_path):
    """Test an explicitly requested missing profile raises an error"""
    config = tmp_path / "config.json"
    config.write_text(json.dumps({"default": {"access_key": "ak"}}))

    with pytest.raises(SdkConfigurationError):
        Profile.from_standard_configuration(str(config), "missing")


def test_malformed_config_raises(tmp_path):
    """Test malformed config files raise an error"""
    config = tmp_path / "config.json"
    config.write_text("{bad-json")

    with pytest.raises(SdkConfigurationError):
        Profile.from_standard_configuration(str(config), "default")


def test_osc_and_oks_default_endpoints_are_separated():
    """Test OSC and OKS resolve to separate default endpoints"""
    profile = Profile(region="eu-west-2", protocol="https")

    assert profile.get_endpoint("api") == "https://api.eu-west-2.outscale.com/api/v1"
    assert (
        profile.get_endpoint("oks") == "https://api.eu-west-2.oks.outscale.com/api/v2"
    )
