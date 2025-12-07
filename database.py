from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url_db = "mysql+pymysql://root:Ragunandhan%40123@localhost:3306/new_product_db"
engine = create_engine(url_db)
session = sessionmaker(autocommit=False,autoflush=False,bind=engine)