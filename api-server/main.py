import uvicorn
from fastapi import FastAPI

from presentation.controller.v1 import v1_router


class ApplicationBuilder:
    """
    FastAPI Application Builder
    """
    app: FastAPI

    def __init__(self):
        self.app = FastAPI()

    def set_routers(self):
        self.app.include_router(v1_router)
        return self

    def build(self) -> FastAPI:
        return self.app


"""
Application Runner
"""
if __name__ == '__main__':
    app = ApplicationBuilder().set_routers().build()
    uvicorn.run(app, port=5000)
