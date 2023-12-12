import json

def get_dishes():
    try:
        dishes = []
        db = open("dishes.txt", "r")
        for line in db:
            dish = json.loads(line.strip())
            dishes.append(dish)
        db.close()
        return dishes
    except Exception as e:
        return []

def create_dish(name,
                description,
                price,
                available):
    try:
        dish = {
            "name": name,
            "description": description,
            "price": price,
            "available": available
        }
        db = open("dishes.txt", "a")
        db.write(f"{json.dumps(dish)} \n")
        db.close()
        return True
    except Exception as e:
        return False

def update_dish(dish_name, new_data):
    try:
        dishes = get_dishes()

        for i, diccionario in enumerate(dishes):
            if diccionario["name"] == dish_name:
                index = i
                break

        if index is None:
            print(f"El diccionario con nombre '{dish_name}' no se encontró en la lista")
            return False

        dishes[index].update(new_data)

        db = open("dishes.txt", "w")
        for dish in dishes:
            db.write(json.dumps(dish) + "\n")

        db.close()

        return True
    
    except Exception as e:
        return False

def delete_dish(dish_name):
    try:
        dishes = get_dishes()
        print(dishes)
        index = None

        for i, diccionario in enumerate(dishes):
            if diccionario["name"] == dish_name:
                index = i
                break

        if index is None:
            print(f"El diccionario con nombre '{dish_name}' no se encontró en la lista")
            return False
        
        del dishes[index]

        db = open("dishes.txt", "w")
        for dish in dishes:
                db.write(json.dumps(dish) + "\n")
        db.close()

        return True
    
    except Exception as e:
        return False

if __name__=="__main__":
   print(get_dishes())
#    create_dish("Coctel", "Coctel de tres licores",15000, False)
#    print(update_dish("Flan2", new_data={"name": "Flan", "available":True}))
#    print(delete_dish("Coctel Grande"))