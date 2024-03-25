from typing import Dict

from fastapi import APIRouter

__tags = ["healthcheck"]
healthcheck_router = APIRouter(tags=__tags)


@healthcheck_router.get("/healthcheck")
async def get_healthcheck() -> str:
    return "ok"
