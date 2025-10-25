import uvicorn
from fastapi import FastAPI
from src.api.routers import main_router
import logging


app = FastAPI()
app.include_router(main_router)



if __name__ == '__main__':
    logging.info(msg='Susseccfult')
    uvicorn.run('main:app', reload=True)