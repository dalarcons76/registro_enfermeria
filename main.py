"""Gunicorn entry point compatible with deployments configured as ``main:app``."""

from app import app, create_app

__all__ = ["app", "create_app"]
