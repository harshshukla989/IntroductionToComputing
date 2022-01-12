# Question 1

print("Question 1 \n")
print("Enter the first number: ")
number1 = input()
print("Enter the second number: ")
number2 = input()
print("Enter the third number: ")
number3 = input()
average = (int(number1) + int(number2) + int(number3)) / 3
print("The average of 3 numbers is:", average)
print("\n")

# Question 2

print("Question 2 \n")
print("Enter the Gross income in $: ")
Gross_income = input()
print("Specify the Number of dependents:")
dependents = input()
# deduction1= standard deduction
deduction1 = 10000
# deduction2= Dependent deduction
deduction2 = 3000 * int(dependents)
Taxable_income = int(Gross_income) - int(deduction1) - int(deduction2)
Tax_rate = 0.20 * int(Taxable_income)
Tax = int(Taxable_income) + int(Tax_rate)
print("The total income tax of the person is : $", Tax)
print("\n")

# Question 3

print("Question 3 \n")
Student = []
print("Enter the SID: ")
SID = int(input())
print("Enter the name of the student: ")
Name = input()
print("Enter the gender of the student:")
Gender = input()
print("Enter the Course Name:")
Course = input()
print("Enter the CGPA of the student:")
CGPA = float(input())
Student.append(SID)
Student.append(Name)
Student.append(Gender)
Student.append(Course)
Student.append(CGPA)
print(Student)
print("\n")

# Question 4

print("Question 4 \n")
studentlist = []  # We have created a blank list
print("Enter the marks of the five students:")
student1 = input() #here we are taking inputs for our list
student2 = input()
student3 = input()
student4 = input()
student5 = input()
studentlist.append(student1) #inputs are getting added in our list
studentlist.append(student2)
studentlist.append(student3)
studentlist.append(student4)
studentlist.append(student5)
studentlist.sort() #this command sorts the inputs
print(studentlist)
print("\n")

# Question 5

print("Question 5 \n")
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.remove('Black')  # to remove the element Black from the list
print(color)
color[3] = 'Purple'  # As black has already been removed so we'll just replace pink with purple
print(color)
print("\n")
