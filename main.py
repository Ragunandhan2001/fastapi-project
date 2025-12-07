from fastapi import FastAPI
from database import session,engine
import database_models

app = FastAPI()


database_models.Base.metadata.create_all(bind = engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
        
        
