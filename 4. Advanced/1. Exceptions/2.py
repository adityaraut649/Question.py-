# Custom Exception

class InvalidMarksError(Exception):
    pass
try:
    marks = int(input("Enter the marks"))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks Should be the between 0 to 100")

    print(f"Marks is: {marks}")
except InvalidMarksError as e: 
   print("Custom Error " , e)





#Example 
print("Program Started")
try:
    usename = input("Enter usename:")
    password = input("Enter password:")


    if usename != "admin":
      raise Exception("Invalid username")

    if usename != "Aditya@123":
      raise Exception("Invalid password")
    
    print("Login Successfully")

except Exception as e:
   print("Login failed ", e)
finally:
   print("Program ended")