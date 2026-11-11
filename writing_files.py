#python writing files(.txt, .json, .csv)
#"w" is used for writing a file! If the file already exists, it will overwrite the file!
#"x" is also used for writing a file if that file doesnt already exists! We will get a FileExistsError !
#You can use 'Try Except' Method to solve this error in "x"! 
#"a" is used to append new data to an existing file!
"""
txt_data = "I like Ramayana!"
file_path = "CodeBro/test2.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' created!")


#if we want to write a list in the file, we cant do it directly, we need to use loops to enter data in the file!

movies = ["Ramayana", "Doomsday","Dune","GodZilla"]

file_path = "CodeBro/test2.txt"
try:
    with open(file_path, "w") as file:
        for movie in movies:
            file.write(movie + "\n")
        print(f"txt file '{movies}' created!")
except FileExistsError:
    print("This file already Exists!")
"""
#For .json File

import json
import csv

Jobs = [["name", "age", "Job"],
        ["rahul", 19, "student"],
        ["Naam Sujal", 20, "rapper"],
        ["Yash", 40, "Actor"]
]

file_path = "CodeBro/test2.csv"
try:
    with open(file_path, "w",newline="") as file: #use newline="" to prevent new line in writer method
        writer = csv.writer(file)
        for row in Jobs:
            writer.writerow(row) #this writer method gives a new line after every row
        #json.dump(Jobs, file, indent=4)
        print(f"Csv file '{Jobs}' created!")
except FileExistsError:
    print("This file already Exists!")