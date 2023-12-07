import json
import datetime

def get_reservations():
    reservations = []

    db = open("reservations.txt", "r")
    for line in db:
        reservation = json.loads(line.strip())
        reservations.append(reservation)
    db.close()

    return reservations

def create_reservation(reservation_date: str,
                reservation_time: str,
                number_of_guests: int,
                assigned_table: int,):
   reservation = {
       "date" :reservation_date,
       "time": reservation_time,
       "guests": number_of_guests,
       "number": assigned_table
   }

   db = open("reservations.txt", "a")
   db.write(f"{json.dumps(reservation)} \n")
   db.close()

   return True

def update_reservation(table_number: int,
                new_data):
    reservations = get_reservations()

    for i, diccionario in enumerate(reservations):
        if diccionario["number"] == table_number:
            index = i
            break

    if index is None:
        print(f"El diccionario con nombre '{table_number}' no se encontró en la lista")
        return False

    reservations[index].update(new_data)

    db = open("reservations.txt", "w")
    for table in reservations:
        db.write(json.dumps(table) + "\n")

    db.close()

    return True

def delete_reservation(dish_name):
    reservations = get_reservations()
    print(reservations)
    index = None

    for i, diccionario in enumerate(reservations):
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

    return reservations

if __name__=="__main__":
    # print(create_reservation("11/diciembre", "10 am", 4, 2))
    # print(get_reservations())
    print(update_reservation(1, new_data={"time": "11 am"}))