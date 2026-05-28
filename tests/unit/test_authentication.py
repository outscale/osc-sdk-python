import base64

import pytest

from osc_sdk_python.authentication import Authentication
from osc_sdk_python.credentials import Profile


class FixedDateAuthentication(Authentication):
    def build_dates(self):
        return "20260102T030405Z", "20260102"


def test_osc_signed_auth_header_uses_access_key_and_scope():
    """Test OSC signed auth builds an OSC4 authorization header"""
    auth = FixedDateAuthentication(
        Profile(access_key="ak", secret_key="sk", region="eu-west-2"),
        host="api.eu-west-2.outscale.com",
        service="api",
    )

    headers = auth.forge_headers_signed("/ReadVms", "{}")

    assert headers["X-Osc-Date"] == "20260102T030405Z"
    assert headers["User-Agent"].startswith("osc-sdk-python/")
    assert headers["Authorization"].startswith("OSC4-HMAC-SHA256 ")
    assert "Credential=ak/20260102/eu-west-2/api/osc4_request" in headers["Authorization"]
    assert "SignedHeaders=content-type;host;x-osc-date" in headers["Authorization"]
    assert "Signature=" in headers["Authorization"]


def test_basic_auth_header_uses_login_and_password():
    """Test basic auth header uses login/password credentials"""
    auth = FixedDateAuthentication(
        Profile(login="user@example.com", password="secret", region="eu-west-2"),
        host="api.eu-west-2.outscale.com",
    )

    headers = auth.get_basic_auth_header()

    expected = base64.b64encode(b"user@example.com:secret").decode("utf-8")
    assert headers["Authorization"] == f"Basic {expected}"
    assert headers["X-Osc-Date"] == "20260102T030405Z"


def test_basic_auth_header_requires_login_and_password():
    """Test basic auth fails clearly when login/password is incomplete"""
    auth = FixedDateAuthentication(
        Profile(login="user@example.com", region="eu-west-2"),
        host="api.eu-west-2.outscale.com",
    )

    with pytest.raises(Exception, match="email or password not set"):
        auth.get_basic_auth_header()


def test_oks_auth_header_uses_access_key_and_secret_key():
    """Test OKS auth header sends AccessKey and SecretKey headers"""
    auth = FixedDateAuthentication(
        Profile(access_key="ak", secret_key="sk", region="eu-west-2"),
        host="api.eu-west-2.oks.outscale.com",
        service="oks",
    )

    headers = auth.forge_headers_oks()

    assert headers["AccessKey"] == "ak"
    assert headers["SecretKey"] == "sk"
    assert headers["User-Agent"].startswith("osc-sdk-python/")


def test_iam_v2_credentials_are_selected_for_configured_service():
    """Test IAM v2 credentials are selected for configured services"""
    auth = FixedDateAuthentication(
        Profile(
            access_key="ak",
            secret_key="sk",
            access_key_v2="ak-v2",
            secret_key_v2="sk-v2",
            iam_v2_services=["oks"],
            region="eu-west-2",
        ),
        host="api.eu-west-2.oks.outscale.com",
        service="oks",
    )

    headers = auth.forge_headers_oks()

    assert headers["AccessKey"] == "ak-v2"
    assert headers["SecretKey"] == "sk-v2"
