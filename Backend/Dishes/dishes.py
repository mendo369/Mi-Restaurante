import json

def get_dishes():
    dishes = []
    db = open("dishes.txt", "r")
    for line in db:
        dish = json.loads(line.strip())
        dishes.append(dish)
    db.close()
    return dishes

def create_dish(name, description, price, available):
   dish = {
      "name": name,
      "description": description,
      "price": price,
      "availabnle": available
   }
   db = open("dishes.txt", "a")
   db.write(f"{json.dumps(dish)} \n")
   db.close()
   return True

def update_dish(dish_name, new_data):
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

    return dishes

def delete_dish(dish_name):
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

    return dishes

if __name__=="__main__":
#    create_dish("Coctel", "Coctel de tres licores",15000, False)
   print(get_dishes())
   print(update_dish("Flan2", new_data={"name": "Flan", "available":False}))
#    print(delete_dish("Coctel Peque\u00c3\u00b1o"))