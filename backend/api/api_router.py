from fastapi import APIRouter
from fastapi.responses import JSONResponse

import common
from api.routes import users

api_router = APIRouter()

#
# Generic routes
#

@api_router.get("/api/version", tags=["version"])
async def get_kmoo_version():
    """
    Returns the version of the KMOO.
    """
    return {"version": common.KMOO_VERSION}

api_router.include_router(users.router, prefix="/api")
