from tools.perf.bench_tls_handshake import measure_handshake
from tools.perf.bench_tls_throughput import measure_throughput
from tools.perf.bench_vpn_throughput import measure_vpn_throughput

def test_measure_handshake_stub():
    result = measure_handshake("localhost:443")
    assert isinstance(result, (int, float))
    assert result >= 0

def test_measure_throughput_stub():
    result = measure_throughput("https://localhost")
    assert isinstance(result, (int, float))

def test_measure_vpn_throughput_stub():
    result = measure_vpn_throughput("tun0")
    assert isinstance(result, (int, float))
