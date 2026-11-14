from fastapi import FastAPI, HTTPException
from menu_items import menu
from schemas import Product, Order, ProductPatch, ProductRequest



app = FastAPI()

next_id = 4


@app.get("/")
def welcome():
    return {"restaurant" : "Deeps Cafe" , "status" : "open"}

@app.get("/menu")
def menu_list(available_only: bool = False,max_price: float = None, item_id: int = None ,low_stock : bool = False,category: str = None):
    result = menu
    if available_only:
        result =  [item for item in menu if item['is_available']]
    if max_price is not None:
        result =  [item for item in result if item['price'] <= max_price]
    if item_id is not None:
        result = [item for item in result if item['item_id'] == item_id]
    if low_stock:
        result = [item for item in result if item['stock'] <= 5]
    if category is not None:
        result = [item for item in result if item['category'] == category]
    return result

    
@app.post("/menu", status_code = 201)
def add_menu(product : ProductRequest): 
    global next_id
    for item in menu:
        if item['name'].lower() == product.name.lower():
            raise HTTPException(409, "Product already exists")
    new_item = product.model_dump()
    new_item["item_id"] = next_id
    menu.append(new_item)
    next_id += 1
    return {"added": new_item}

@app.put("/menu/{item_id}")
def update_item(item_id : int,product: Product):
    for i,item in enumerate(menu):
        if item['item_id'] == item_id:
            new_item = product.model_dump()
            new_item["item_id"] = item_id
            menu[i] = new_item
            return {"message": "Changes applied"}
    raise HTTPException(404, "Item missing")    

@app.patch("/menu/{item_id}")
def patch_item(item_id : int,product: ProductPatch):
    for item in menu:
        if item['item_id'] == item_id:
            patch_data = product.model_dump(exclude_unset = True)
            for key, value in patch_data.items():
                item[key] = value
            return {"message": "Changes applied"}
    raise HTTPException(404, "Item missing") 
                



@app.delete("/menu/{item_id}")
def delete_item(item_id: int):
    for item in menu:
        if item['item_id'] == item_id:
            menu.remove(item)
            return {"deleted": item['name']}
    raise HTTPException(404, "Item missing")


@app.post("/order")
def order_item(order : Order):
    return {"order": order, "status": "recieved"}


@app.get("/menu/{item_id}")
def menu_item(item_id: int):
    for item in menu:
        if item['item_id'] == item_id:
            return item
    raise HTTPException(404, "Product not found") 

@app.get("/about")
def about():
    return {"description":"This app will work as manger to your restaurent system", "version": 1}