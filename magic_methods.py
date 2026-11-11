#magic methods = dunder methods __init__, __str__, __eq__
#               they are automatically called by many of pythons built-in operations.
#               they allow developers to define or customize the behaviour of objects

class book:

    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.name} by {self.author}"

    def __eq__(self, other):
        return self.name == other.name and self.author == other.author

    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __add__(self, other):
        return self.pages + other.pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return f"Data Not Available!"
    


book1 = book("Percy Jackson", "Rick Riordon", 410)
book2 = book("Red Rising", "Unknown", 524)
book3 = book("Harry potter", "J.K. Rowling", 234)

print(book1["name"])
        
