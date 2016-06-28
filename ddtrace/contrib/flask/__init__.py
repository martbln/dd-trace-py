from ..util import require_modules

required_modules = ['flask']

with require_modules(required_modules) as missing_modules:
    if not missing_modules:
        from .middleware import TraceMiddleware

        __all__ = ['TraceMiddleware']