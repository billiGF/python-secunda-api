import uvicorn
from fastapi import FastAPI
from src.api.routers import main_router
from src.core.db import database
from logger import logger


app = FastAPI()
app.include_router(main_router)




if __name__ == '__main__':
    if not database:
        logger.info(msg='Not connected')
    logger.info('Database Conncected!')
    uvicorn.run('main:app', reload=True)