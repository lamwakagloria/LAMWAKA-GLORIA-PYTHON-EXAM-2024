def student_details():
    name = input("Gloria Arinda: ")
    student_number = input("SEP23/BCS/088U/F: ")
    programming_mark = float(input("90: "))
    data_science_mark = float(input("87: "))
    computer_applications_mark = float(input("77: "))
    average_mark = (programming_mark + data_science_mark + computer_applications_mark) / 3
    
    print("\nStudent Details:")
    print(f"Name: {name}")
    print(f"Student Number: {student_number}")
    print(f"Programming Marks: {programming_mark}")
    print(f"Data Science Marks: {data_science_mark}")
    print(f"Computer Applications Marks: {computer_applications_mark}")
    print(f"Average Marks: {average_mark:.3f}")



    
