import json

import pytest

from osc_sdk_python.credentials import Profile


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

    with pytest.raises(AttributeError):
        Profile.from_standard_configuration(str(config), "missing")


def test_malformed_config_raises(tmp_path):
    """Test malformed config files raise an error"""
    config = tmp_path / "config.json"
    config.write_text("{bad-json")

    with pytest.raises(json.JSONDecodeError):
        Profile.from_standard_configuration(str(config), "default")


def test_osc_and_oks_default_endpoints_are_separated():
    """Test OSC and OKS resolve to separate default endpoints"""
    profile = Profile(region="eu-west-2", protocol="https")

    assert profile.get_endpoint("api") == "https://api.eu-west-2.outscale.com/api/v1"
    assert profile.get_endpoint("oks") == "https://api.eu-west-2.oks.outscale.com/api/v2"
