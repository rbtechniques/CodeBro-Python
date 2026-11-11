import time
my_time = int(input("Enter time for countdown"))
for i in range(my_time, 0, -1):
    seconds = i%60
    minutes = i//60
    hours = minutes//60
    print(f"{hours:02}:{minutes:02}:{seconds:02} seconds remaining")
    time.sleep(1)
print("TIME'S UP!")