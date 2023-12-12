import json
import get_id_time

def get_orders():
    try:
        
        orders = []

        db = open("orders.txt", "r")
        for line in db:
            order = json.loads(line.strip())
            orders.append(order)
        db.close()

        return orders

    except Exception as e:

        return []
    
def create_order(dishes: [],
                table_number: int):
    try:

        id = get_id_time.generate_id_from_time_and_date()

        order = {
            "id":id,
            "dishes" :dishes,
            "table_number": table_number
        }

        with open("orders.txt", "a", encoding="utf-8") as db:
                db.write(f"{json.dumps(order)} \n")

        return True
    
    except Exception as e:

        return False

def update_order(order_id:str,
                new_data):
    try:
        orders = get_orders()
        
        index = None

        # print(new_data)

        for i, order in enumerate(orders):
            if order["id"] == order_id:
                index = i
                break

        if index is None:
            return False

        orders[index].update(new_data)

        db = open("orders.txt", "w")
        for order in orders:
            db.write(json.dumps(order) + "\n")

        db.close()

        return True
    
    except Exception as e:

        return False

def delete_order(order_id):
    try:

        orders = get_orders()
        index = None

        for i, order in enumerate(orders):
            if order["id"] == order_id:
                index = i
                break

        if index is None:
            return False
        
        del orders[index]

        db = open("orders.txt", "w")
        for order in orders:
                db.write(json.dumps(order) + "\n")
        db.close()

        return True
    
    except Exception as e:

        return False

if __name__ == "__main__":
    print(get_orders())
    # print(create_order(dishes=["Perro", "Pepsi"], table_number=4))
    # print(update_order(order_id="2023121217138", new_data={"table_number": 8}))
    # print(delete_order(order_id="202312915646"))
