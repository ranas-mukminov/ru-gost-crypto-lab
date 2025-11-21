from tools.ai.ai_provider import NoopAIProvider

def test_noop_provider_generate_config_overlays():
    provider = NoopAIProvider()
    scenario = {"name": "test", "type": "web_tls"}
    overlays = provider.generate_config_overlays(scenario)
    assert isinstance(overlays, dict)
    # Noop provider might return empty dict or default templates
    assert overlays == {} or "docker-compose.override.yml" in overlays

def test_noop_provider_generate_report_snippet():
    provider = NoopAIProvider()
    results = {"success": True}
    snippet = provider.generate_report_snippet(results, language="en")
    assert isinstance(snippet, str)
    assert "Report" in snippet or "Results" in snippet
