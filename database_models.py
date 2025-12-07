from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()

class ProductData(Base):
    id = Column(Integer,primary_key=True,index=True)
    product_name = Column(String(100))
    product_code = Column(String(100))
    price = Column(Float)
    gst = Column(Integer)
    