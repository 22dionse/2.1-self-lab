#!/usr/bin/env python3
import csv

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

def write_trips(trips):
    with open("trips.csv", "w", newline="") as file:    
        writer = csv.writer(file)
        writer.writerows(trips) 

def read_trips(trips):
    with open("reader.csv", "r", newline="")
        reader = csv.reader(file)
        for row in reader:
            print(row[0] + " (" + str(row[1]) + ")")
    


def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()
        
        more = input("More entries? (y or n): ")
    
    trips = ["miles_driven, gallons_used, mpg"]
    print()
    trips.append([miles_driven, gallons_used, mpg])
    print(trips)
    write_trips(trips)

    
    print("Bye")

if __name__ == "__main__":
    main()
