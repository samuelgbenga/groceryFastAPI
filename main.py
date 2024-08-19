from fastapi import FastAPI, HTTPException

from models import ItemPayload



app = FastAPI()


grocery_list: dict[int, ItemPayload] = {}


@app.post("/items/{item_name}/{quantity}")
def add_item(item_name: str, quantity: int):
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0.")
    
    # assignment, condition the loop through
    items_ids = {item.item_name: item.item_id if item.item_id is not None else 0 for item in grocery_list.values()}
    
    # if item already exist just increase the quantity
    if item_name in items_ids.keys():
        item_id = items_ids[item_name]
        grocery_list[item_id].quantity += quantity
    # add new item to the grocery_list
    else:
        # first generte id for the new item
        item_id = max(grocery_list.keys()) + 1 if grocery_list else 0
        grocery_list[item_id] = ItemPayload(
            item_id=item_id,
            item_name=item_name,
            quantity=quantity,
        )

    return {"item": grocery_list[item_id]}

# decorator and the function
# @app.get("/")
# def root():
#     return {"message":"Hello world"}

# getting the list of a  specifice item
@app.get("/items/{item_id}")
def list_item(item_id: int) -> dict[str, ItemPayload]:
    if item_id not in grocery_list:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": grocery_list[item_id]}

# get all items
@app.get("/items")
def list_all_items() -> dict[str, dict[int, ItemPayload]]:
    return {"items": grocery_list}

# delete an item by id
@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    if item_id not in grocery_list:
        raise HTTPException(status_code=404, detail="Item not found.")
    del grocery_list[item_id]
    return {"result": "Item deleted."}

# delete quantity of item by id
@app.delete("/items/{item_id}/{quantity}")
def remove_quantity(item_id: int, quantity: int):
    if item_id not in grocery_list:
        raise HTTPException(status_code=404, detail="Item not found.")
    if grocery_list[item_id].quantity <= quantity:
        del grocery_list[item_id]
        return {"result":"item deleted"}
    else:
        grocery_list[item_id].quantity -= quantity
    return {"result": f"{quantity} items removed from {grocery_list[item_id].item_name}."}
