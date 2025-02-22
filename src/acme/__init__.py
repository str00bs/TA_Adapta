"""Root module of the application"""

import importlib.metadata

try:
    __version__ = importlib.metadata.version("acme")
    __author__ = importlib.metadata.author("acme")
except ImportError:
    pass
