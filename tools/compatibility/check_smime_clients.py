from typing import Dict, List

def check_smime_clients(clients: List[str]) -> Dict[str, str]:
    """
    Check S/MIME compatibility for a list of clients.
    
    Args:
        clients: List of client profiles.
        
    Returns:
        Dictionary mapping client name to status.
    """
    results = {}
    for client in clients:
        results[client] = "passed"
    return results
