from tools.compatibility.check_tls_clients import check_tls_clients
from tools.compatibility.check_smime_clients import check_smime_clients
from tools.compatibility.check_vpn_clients import check_vpn_clients

def test_check_tls_clients_stub():
    results = check_tls_clients("localhost:443", ["chrome", "firefox"])
    assert "chrome" in results
    assert "firefox" in results
    assert results["chrome"] in ["passed", "failed", "skipped"]

def test_check_smime_clients_stub():
    results = check_smime_clients(["outlook", "thunderbird"])
    assert "outlook" in results

def test_check_vpn_clients_stub():
    results = check_vpn_clients("vpn.example.com")
    assert "status" in results
