import asyncio
import logging
from os import environ

import uvicorn
from dotenv import load_dotenv

load_dotenv()

from config import HTTP_PORT
from database import init_database
from MuppetsServer import MuppetsServer
from MuppetsServer.auth_app import app as auth_app
from MuppetsServer.routers.php_compat import router as php_router

logging.basicConfig(
    level=logging.DEBUG if environ.get("type", "release") == "debug" else logging.INFO,
    format="%(levelname)s/%(name)s:\t%(message)s",
)

app = auth_app
app.include_router(php_router)

@app.on_event("startup")
async def startup_event():
    await init_database()
    try:
        asyncio.create_task(MuppetsServer.start())
    except:
        pass

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(HTTP_PORT),
        log_level="info"
    )
