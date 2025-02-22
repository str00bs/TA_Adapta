"""Root module of the application"""

import importlib.metadata

try:
    __version__ = importlib.metadata.version("adapta")
    __author__ = importlib.metadata.author("adapta")
except ImportError:
    pass
