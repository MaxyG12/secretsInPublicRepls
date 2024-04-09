import os 

adminPass = os.environ['adminPass']
userPass = os.environ['userPass']
print("🌟Login System🌟")
print()
username = input("Username > ")
password = input("Password > ")
if username == "admin" and password == adminPass:
  print("Hello admin")
elif username == "user" and password == userPass:
  print("Hello user")
else:
  print("Better luck next time")

