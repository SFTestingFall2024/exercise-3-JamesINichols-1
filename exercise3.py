#GitHub Name: LEMcD
#Course ID:  COP2002, Section:  0M1
#Date Created:  September 8, 2024
#Program Title:  Exercise 2
#Description:  Using variables, assignment statements, calculations, and different ways of printing them

#Creat variables for introduction sentences

name="Leigh McDavitt"
major="Information Systems Technology-Security concentration"
interest="I get to learn Python Langauage"


#Print introduction string sentences

print("My name is "+(name)+"." "  My major is " +(major)+".")
print("I'm most interested in this class because "+(interest)+"."+"\n")

#Create variables for numbers used in calculations

num1=28
num2=37

#Create variables for calculations using the number variables already defined & print the results

sum=num1+num2 #variable for addtion 
answer1=str(num1)+" "+"+"+" "+str(num2)+" "+"="" "+str(sum)+"\n" #variable to print entire addition equation with spaces
print(answer1)


difference=num1-num2 #variable for subraction 
answer2=str(num1)+" "+"-"+" "+str(num2)+" "+"="" "+str(difference)+"\n" #variable to print entire subraction equation with spaces
print(answer2)
      
product=num1*num2 #variable for multiplication 
answer3=str(num1)+" "+"*"+" "+str(num2)+" "+"="" "+str(product)+"\n" #variable to print entire multiplication equation with spaces
print(answer3)

quotient=num1/num2 #variable for division 
answer4=str(num1)+" "+"/"+" "+str(num2)+" "+"="" "+str(quotient)+"\n" #variable to print entire division equation with spaces
print(answer4)
      
modulus=num1%num2 #variable for remainder
answer5=str(num1)+" "+"%"+" "+str(num2)+" "+"="" "+str(modulus)+"\n\n" #variable to print entire modulus equation with spaces
print(answer5)

#Create variable and print end message of program
ending="This is the end of the program!"
print(ending)