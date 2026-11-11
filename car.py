
class car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"you drive the {self.year} car")

    def stop(self):
        print(f"you stop the {self.year} car")

    def describe(self):
        print(f" {self.model} {self.year} {self.color}")
