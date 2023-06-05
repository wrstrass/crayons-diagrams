from fastapi import FastAPI
from views import router
from web_socket import router as ws_router


app = FastAPI()


app.include_router(router)
app.include_router(ws_router)
