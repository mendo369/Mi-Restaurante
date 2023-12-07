import hashlib

def register(email, password):

  if not email_validate(email):
    print("error")
    return False
  
  if not password_validate_and_hash(password):
    print("Contraseña no valida")
    return False
  
  password = password_validate_and_hash(password)


  db = open("registro_inicio.txt", "a")
  db.write(f"{email}, {password}\n")
  db.close()

  print("user save")

def login(email, password):
  db = open("registro_inicio.txt", "r")
  for line in db:
    user = line.strip().split(', ')
    if(user[0]==email):
      if(compare_password(password, user[1])):
        return user
      else:
        return "Credenciales invalidas"
      # print(type(user[1]))
    
  db.close()
  return False

def email_validate(email):
  if "@" not in email:
    return False

  domain = email.split("@")[1]
  organization = domain.split(".")[0]
  organizations_valid = ["gmail", "hotmail", "yahoo", "outlook", "correounivalle"]
  if organization not in organizations_valid:
    print (domain)
    return False

  if domain.endswith(".com") or domain.endswith(".co"):
    return True
  else:
    print("no .com .co")

    return False

def password_validate_and_hash(password):
  if len(password) < 10:
    return None

  # Comprobamos que la contraseña tenga al menos 1 letra minúscula.

  if not any(c.islower() for c in password):
    return None

  # Comprobamos que la contraseña tenga al menos 1 letra mayúscula.

  if not any(c.isupper() for c in password):
    return None

  # Comprobamos que la contraseña tenga al menos 1 número.

  if not any(c.isdigit() for c in password):
    return None

  # Comprobamos que la contraseña tenga al menos 1 carácter especial.

  caracteres_especiales = "@*$!?\&/"
  if not any(c in caracteres_especiales for c in password):
    return None

  # Encriptamos la contraseña con SHA-256.

  return hashlib.sha256(password.encode()).hexdigest()

def compare_password(password, password_hashed):
  try:
    hashed = hashlib.sha256(password.encode()).hexdigest()

    if(hashed == password_hashed):
      return True
    return False
  except Exception as e:
    return False

if __name__ == "__main__":
  # register("luis@gmail.com", "Ld$123mend")
  user = login("luis@gmail.com", "Ld$123mend")
  print(user)