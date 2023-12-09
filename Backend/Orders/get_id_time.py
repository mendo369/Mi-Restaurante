import datetime

def generate_id_from_time_and_date():
  """Genera un ID a partir de la hora, el mes y el año.

  Returns:
    Un ID único a partir de la hora, el mes y el año.
  """

  # Obtenemos la fecha y la hora actuales.
  now = datetime.datetime.now()

  # Convertimos la fecha a un número entero.
  date_int = int(f"{now.year}{now.month}{now.day}")

  # Generamos un ID combinando la fecha, la hora, los minutos y los segundos.
  id = f"{date_int}{now.hour}{now.minute}{now.second}"

  # Devolvemos el ID.
  return id