from fastapi import FastAPI,Depends,HTTPException
from database import session,engine
from models import Product
from sqlalchemy.orm import Session
import database_models

app = FastAPI()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

database_models.Base.metadata.create_all(bind = engine)

@app.post("/products")
def add_product(product:Product,db:Session = Depends(get_db)):
    new_product = database_models.ProductData(product_name = product.product_name,product_code = product.product_code,price=product.price,gst=product.gst)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return "Product Added successfully"

@app.get("/products")
def get_all_product(db:Session=Depends(get_db)):
    product = db.query(database_models.ProductData).all()
    return product

@app.get("/products/{product_id}")
def get_product_by_id(product_id:int,db:Session=Depends(get_db)):
    product = db.query(database_models.ProductData).filter(database_models.ProductData.id == product_id).first()
    if product:
        return product 
    else:
        raise HTTPException(404,"Product Not Found")
    
@app.put("/products/{product_id}")
def update_product(product_id:int,pro:Product,db:Session=Depends(get_db)):
    product = db.query(database_models.ProductData).filter(database_models.ProductData.id == product_id).first()
    if product:
        product_name = pro.product_name
        product_code = pro.product_code
        price=pro.price
        gst=pro.gst
        db.commit()
    else:
        raise HTTPException(404,"Product Not Found")
    
@app.delete("/products/{product_id}")
def delete(product_id:int,db:Session = Depends(get_db)):
    product = db.query(database_models.ProductData).filter(database_models.ProductData.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
    else:
        raise HTTPException(404,"Product Not Product")
    
    
        
