from abc import ABC, abstractmethod
from typing import Any, Dict

class AIProvider(ABC):
    """Abstract base class for AI providers."""
    
    @abstractmethod
    def generate_config_overlays(self, scenario: Dict[str, Any]) -> Dict[str, str]:
        """Generate configuration overlays based on the scenario."""
        pass
        
    @abstractmethod
    def generate_report_snippet(self, results: Dict[str, Any], language: str = "en") -> str:
        """Generate a human-readable report snippet from results."""
        pass

class NoopAIProvider(AIProvider):
    """
    No-op implementation of AIProvider for testing and CI.
    Does not call any external LLM.
    """
    
    def generate_config_overlays(self, scenario: Dict[str, Any]) -> Dict[str, str]:
        # Return empty dict or basic templates for testing
        return {}
        
    def generate_report_snippet(self, results: Dict[str, Any], language: str = "en") -> str:
        if language == "ru":
            return "### Результаты (Автоматический отчет)\n\nТесты завершены успешно."
        return "### Results (Automated Report)\n\nTests completed successfully."
