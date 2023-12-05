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

if __name__=="__main__":
#    create_dish("Flan", "un flan de queso",8000, True)
   dishes =get_dishes()
   print(dishes)