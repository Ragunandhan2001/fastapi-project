from pydantic import BaseModel

class Product(BaseModel):
    id :int
    product_name : str
    product_code :str
    price :float
    gst:int
    
    