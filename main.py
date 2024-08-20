from fastapi import FastAPI, HTTPException
import redis

from models import ItemPayload



app = FastAPI()


grocery_list: dict[int, ItemPayload] = {}

redis_client = redis.StrictRedis(host='0.0.0.0', port=6379, db=0, decode_responses=True)


@app.post("/items/{item_name}/{quantity}")
def add_item(item_name: str, quantity: int) -> dict[str, ItemPayload]:
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be greater than 0.")
    
    # assignment, condition the loop through
   # items_ids = {item.item_name: item.item_id if item.item_id is not None else 0 for item in grocery_list.values()}
    
    item_ids_str = redis_client.hget("item_name_to_id", item_name)

    # if item already exist just increase the quantity
    if item_ids_str is not None:
        # item_id = items_ids[item_name]
        # grocery_list[item_id].quantity += quantity
        item_id = int(item_ids_str)
        redis_client.hincrby(f"item_id:{item_id}", "quantity", quantity)
    # add new item to the grocery_list
    else:
        # first generte id for the new item
        #item_id = max(grocery_list.keys()) + 1 if grocery_list else 0
        # grocery_list[item_id] = ItemPayload(
        #     item_id=item_id,
        #     item_name=item_name,
        #     quantity=quantity,
        # )
        item_id: int = redis_client.incr("item_ids")
        redis_client.hset(
            f"item_id:{item_id}",
            mapping={
                "item_id": item_id,
                "item_name": item_name,
                "quantity": quantity,
            })
        redis_client.hset("item_name_to_id", item_name, item_id)
        

    return {"item": ItemPayload(item_id=item_id, item_name=item_name, quantity=quantity)}

# decorator and the function
# @app.get("/")
# def root():
#     return {"message":"Hello world"}

# getting the list of a  specifice item
@app.get("/items/{item_id}")
def list_item(item_id: int) -> dict[str, dict[str, str]]:
    # if item_id not in grocery_list:
    #     raise HTTPException(status_code=404, detail="Item not found")
    # return {"item": grocery_list[item_id]}
    if not redis_client.hexists(f"item_id:{item_id}", "item_id"):
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return {"item": redis_client.hgetall(f"item_id:{item_id}")}




# get all items
@app.get("/items")
def list_all_items():
    items: list[ItemPayload] = []
    stored_items: dict[str, str] = redis_client.hgetall("item_name_to_id")

    for name, id_str in stored_items.items():
        item_id: int = int(id_str)
        
        item_name_str: str | None = redis_client.hget(f"item_id:{item_id}", "item_name")

        if item_name_str is not None:
            item_name: str = item_name_str
        else:
            continue

        item_quantity_str: str | None = redis_client.hget(f"item_id:{item_id}", "quantity")

        if item_quantity_str is not None:
            item_quantity: int = int(item_quantity_str)
        else:
            item_quantity = 0

        items.append(
            ItemPayload(item_id=item_id, item_name=item_name, quantity=item_quantity)
        )

    return {"items": items}



# delete an item by id
@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    # if item_id not in grocery_list:
    #     raise HTTPException(status_code=404, detail="Item not found.")
    # del grocery_list[item_id]

    if not redis_client.hexists(f"item_id:{item_id}", "item_id"):
        raise HTTPException(status_code=404, detail="Item not found.")
    else:
        item_name: str | None = redis_client.hget(f"item_id:{item_id}", "item_name")

    redis_client.hdel("item_name_to_id", f"{item_name}")
    redis_client.delete(f"item_id:{item_id}")

    return {"result": "Item deleted."}



# delete quantity of item by id
@app.delete("/items/{item_id}/{quantity}")
def remove_quantity(item_id: int, quantity: int):
    # if item_id not in grocery_list:
    #     raise HTTPException(status_code=404, detail="Item not found.")
    # if grocery_list[item_id].quantity <= quantity:
    #     del grocery_list[item_id]
    #     return {"result":"item deleted"}
    # else:
    #     grocery_list[item_id].quantity -= quantity
    # return {"result": f"{quantity} items removed from {grocery_list[item_id].item_name}."}
    if not redis_client.hexists(f"item_id:{item_id}", "item_id"):
        raise HTTPException(status_code=404, detail="Item not found.")
    
    item_quantity: str | None = redis_client.hget(f"item_id:{item_id}", "quantity")

    if item_quantity is None:
        existing_quantity: int = 0
    else:
        existing_quantity: int = int(item_quantity)

    if existing_quantity <= quantity:
        item_name: str | None = redis_client.hget(f"item_id:{item_id}", "item_name")
        redis_client.hdel("item_name_to_id", f"{item_name}")
        redis_client.delete(f"item_id:{item_id}")
        return {"result": "Item deleted."}
    else:
        redis_client.hincrby(f"item_id:{item_id}","quantity", -quantity)
        return {"result": f"{quantity} items removed."}