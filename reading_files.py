#Python reading files(.txt, .json, .csv)

"""
# Txt file

file_path = "CodeBro/test2.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("file not found!")
except PermissionError:
    print("You dont have permission to read this file!")


#Json File

import json
file_path = "CodeBro/test2.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["rapper"])

except FileNotFoundError:
    print("file not found!")
except PermissionError:
    print("You dont have permission to read this file!")
"""

#Csv File

import csv
file_path = "CodeBro/test2.csv"
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)  #access specific column using Index

except FileNotFoundError:
    print("file not found!")
except PermissionError:
    print("You dont have permission to read this file!")

