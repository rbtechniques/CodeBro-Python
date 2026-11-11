#static method = a method that belong to a class rather than any object from that class(instance)
#                usually used for general  utility function

class employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = employee("aalu", "Cook")
employee2 = employee("Halku", "Manager")
employee3 = employee("Thor", "Cashier")



