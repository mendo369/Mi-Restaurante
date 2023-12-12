import json
import datetime

def get_reservations():
    try:

        reservations = []

        db = open("reservations.txt", "r")
        for line in db:
            reservation = json.loads(line.strip())
            reservations.append(reservation)
        db.close()

        return reservations
    
    except Exception as e:

        return []

def create_reservation(reservation_date: str,
                reservation_time: str,
                number_of_guests: int,
                assigned_table: int,):
    try:

        reservation = {
            "date" :reservation_date,
            "time": reservation_time,
            "guests": number_of_guests,
            "table_number": assigned_table
        }

        db = open("reservations.txt", "a")
        db.write(f"{json.dumps(reservation)} \n")
        db.close()

        return True
    
    except Exception as e:

        return False

def update_reservation(reservation,
                      new_data):
    try:

        reservations = get_reservations()
        
        index = None

        # print(new_data)

        for i, diccionario in enumerate(reservations):
            if (diccionario["table_number"] == reservation["table_number"]) and  (diccionario["date"] == reservation["date"]) and (diccionario["time"] == reservation["time"]):
                index = i
                break

        if index is None:
            print("El diccionario con nombre ", reservation["table_number"],"no se encontró en la lista")
            return False

        reservations[index].update(new_data)

        db = open("reservations.txt", "w")
        for table in reservations:
            db.write(json.dumps(table) + "\n")

        db.close()

        return True
    
    except Exception as e:

        return False

def delete_reservation(reservation):
    try:

        reservations = get_reservations()
        index = None

        for i, diccionario in enumerate(reservations):
            if (diccionario["table_number"] == reservation["table_number"]) and  (diccionario["date"] == reservation["date"]) and (diccionario["time"] == reservation["time"]):
                index = i
                print(index)
                break

        if index is None:
            print("El diccionario con nombre ", reservation["table_number"],"no se encontró en la lista")
            return False
        
        del reservations[index]

        db = open("reservations.txt", "w")
        for reservation in reservations:
                db.write(json.dumps(reservation) + "\n")
        db.close()

        return True
    
    except Exception as e:

        return False

if __name__=="__main__":
    print(get_reservations())
    # print(create_reservation("16/diciembre", "10 am", 5, 4))
    # print(update_reservation(reservation={"table_number":2, "date": "11/diciembre", "time":"10 am"}, new_data={"time": "12 m"}))
    print(delete_reservation(reservation={"table_number":4, "date": "16/diciembre", "time":"10 am"}))