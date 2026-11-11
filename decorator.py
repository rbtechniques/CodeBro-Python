#Decorator = a function that extends the behaviour of another function
#           w/o modifying the function   
#           Pass the base function as an argument to the decorator

def add_sprinkles(function):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        function(*args, **kwargs)
    return wrapper

@add_sprinkles
def get_icecream(flavor):
    print(f"Here Is your {flavor} ice cream!")


get_icecream("Vanilla")           
