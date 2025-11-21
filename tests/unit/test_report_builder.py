from tools.reports.report_builder import build_report

def test_build_report_basic():
    results = {
        "compatibility": {"tls": {"passed": 10, "failed": 0}},
        "perf": {"handshake_avg_ms": 50}
    }
    report = build_report(results, language="en")
    assert "# Test Report" in report
    assert "Handshake Avg Ms: 50 ms" in report
    assert "**TLS**: 10 passed, 0 failed" in report
