from tools.scenario_loader import load_scenario
from tools.ai.ai_provider import NoopAIProvider
from tools.reports.report_builder import build_report
from tools.compatibility.check_tls_clients import check_tls_clients
from tools.perf.bench_tls_handshake import measure_handshake

def test_lab_web_scenario_flow(tmp_path):
    # 1. Setup Scenario
    scenario_content = """
    name: integration_test_web
    type: web_tls
    topology:
      services: [nginx]
    test_plan:
      compatibility: true
      performance: true
    """
    scenario_file = tmp_path / "scenario.yaml"
    scenario_file.write_text(scenario_content)
    
    # 2. Load Scenario
    scenario = load_scenario(str(scenario_file))
    assert scenario.name == "integration_test_web"
    
    # 3. Generate Configs (Mock AI)
    ai = NoopAIProvider()
    overlays = ai.generate_config_overlays(scenario.model_dump())
    # Noop provider returns empty or basic dict, just check it runs
    assert isinstance(overlays, dict)
    
    # 4. Simulate Checks
    compat_results = check_tls_clients("localhost:443", ["chrome", "firefox"])
    perf_result = measure_handshake("localhost:443")
    
    results = {
        "compatibility": {"tls": compat_results},
        "perf": {"handshake_avg_ms": perf_result}
    }
    
    # 5. Generate Report
    report = build_report(results, language="en")
    assert "# Test Report" in report
    assert "chrome" in report or "passed" in report
    assert str(perf_result) in report
