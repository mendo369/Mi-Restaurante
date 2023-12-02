def register(email, contraseña):

  if not email_validate(email):
    print("error")
    return False

  db = open("registro_inicio.txt", "a")
  db.write(f"{email}, {contraseña}\n")
  db.close()

  print("user save")

def login(email, password):
  return

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

if __name__ == "__main__":
  register("luis@gmail.com", "password")