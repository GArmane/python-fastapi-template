"""Aplication routers module entrypoint.

Add modules into "routers" variable to load them into FastAPI registry.
"""

from app.api.routers import public

routers = [public]
