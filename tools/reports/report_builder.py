from typing import Any, Dict


def build_report(results: Dict[str, Any], language: str = "en") -> str:
    """
    Build a markdown report from the results dictionary.
    
    Args:
        results: Dictionary containing test results.
        language: Language code ('en' or 'ru').
        
    Returns:
        Markdown string.
    """
    report = []
    
    if language == "ru":
        report.append("# Отчет о тестировании")
    else:
        report.append("# Test Report")
        
    report.append("")
    
    # Compatibility Section
    if "compatibility" in results:
        compat = results["compatibility"]
        if language == "ru":
            report.append("## Совместимость")
        else:
            report.append("## Compatibility")
            
        for check_type, data in compat.items():
            passed = data.get("passed", 0)
            failed = data.get("failed", 0)
            report.append(f"- **{check_type.upper()}**: {passed} passed, {failed} failed")
            
    # Performance Section
    if "perf" in results:
        perf = results["perf"]
        if language == "ru":
            report.append("## Производительность")
        else:
            report.append("## Performance")
            
        for metric, value in perf.items():
            name = metric.replace("_", " ").title()
            report.append(f"- {name}: {value} ms" if "ms" in metric or "time" in metric else f"- {name}: {value}")
            
    return "\n".join(report)
