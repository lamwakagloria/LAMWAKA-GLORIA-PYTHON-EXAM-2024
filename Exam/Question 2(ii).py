def calculate_mpg():
    miles_driven = float(input("Enter the number of miles driven: "))
    gallons_used = float(input("Enter the number of gallons of gas used: "))
    
    if gallons_used == 0:  
        print("Error: Gallons used cannot be zero.")
    else:
        mpg = miles_driven / gallons_used
        print(f"The car's miles-per-gallon (MPG) is: {mpg:.2f}")
calculate_mpg()




