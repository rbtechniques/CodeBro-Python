#exception = an event that interrupts the flow of a program
#           (ZeroDivisionError, TypeError, ValueError)
#           1.try 2.except 3.finally

try:
    number = int(input("Enter A Number: "))
    print(1/number) 
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter Only numbers please")
except Exception:
    print("Something went wrong")
finally:
    print("Do something!")