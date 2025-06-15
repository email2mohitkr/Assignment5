'''
Task 1: 
Create a Dictionary of Student Marks
Problem Statement: Write a Python program that:

1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.




'''
name={'Mohit' : 85,'Sunny':99,'Dipu':99,'Riya':63}

str=input("Enter the student's name: " )
case=str.capitalize()
#print(str.capitalize())
if (case in name):
    val=name.get(case,'Student not found.')
    print(case + "'s marks :", val)
else:
    val = name.get(case, 'Student not found.')
    print(val)