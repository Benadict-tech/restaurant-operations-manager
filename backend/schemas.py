from pydantic import BaseModel

class Product(BaseModel):
    item_id : int
    name: str
    price: float
    stock: int
    category: str
    is_available: bool = True

class ProductRequest(BaseModel):
    name: str 
    price: float 
    stock: int 
    category: str
    is_available: bool 

class Order(BaseModel):
    product_name: str
    quantity: int

class ProductPatch(BaseModel):
    name: str | None = None
    price: float | None = None
    stock: int | None = None
    category: str | None = None
    is_available: bool  | None = None
