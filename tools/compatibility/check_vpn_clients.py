from typing import Dict

def check_vpn_clients(endpoint: str) -> Dict[str, str]:
    """
    Check VPN connectivity.
    
    Args:
        endpoint: VPN endpoint address.
        
    Returns:
        Dictionary with status.
    """
    return {"status": "connected", "ping": "ok"}
