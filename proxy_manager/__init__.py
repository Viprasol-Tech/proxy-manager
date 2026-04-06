"""
proxy-manager - Manage proxy connections

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import ProxyManager, proxy, process, main

__all__ = ["ProxyManager", "proxy", "process", "main"]
