"""Expose the Flask application from the legacy root-level app.py module."""

import importlib.util
import sys
from pathlib import Path

_application_path = Path(__file__).resolve().parent.parent / "app.py"
_module_name = "_registro_enfermeria_application"
_spec = importlib.util.spec_from_file_location(_module_name, _application_path)
if _spec is None or _spec.loader is None:
    raise ImportError(f"No se pudo cargar la aplicación desde {_application_path}")

_application_module = importlib.util.module_from_spec(_spec)
sys.modules[_module_name] = _application_module
_spec.loader.exec_module(_application_module)

app = _application_module.app
create_app = _application_module.create_app

__all__ = ["app", "create_app"]
