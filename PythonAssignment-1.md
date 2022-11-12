## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?

Q2. Why is Python called a dynamically typed language?

Q3. List some pros and cons of Python programming language?

Q4. In what all domains can we use Python?

Q5. What are variable and how can we declare them?
A5. Variable is a name given to specific memory location.
    myName = "Iqbal"
    
Q6. How can we take an input from the user in Python?

input()

Q7. What is the default datatype of the value that has been taken as an input using input() function?

str 

Q8. What is type casting?

Type Casting is the method to convert the variable data type into a certain data type.

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

# Python program to take multiple inputs from the user
a, b = input("Enter two of your lucky number: ").split() 
print("First lucky number is: ", a) 
print("Second lucky number is: ", b) 


Q10. What are keywords?

Python keywords are special reserved words that have specific meanings and purposes and can't be used for anything but those specific purposes.

Q11. Can we use keywords as a variable? Support your answer with reason.

We cannot use a keyword as a variable name, function name, or any other identifier. They are used to define the syntax and structure of the Python language.

Q12. What is indentation? What's the use of indentaion in Python?

Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.

Q13. How can we throw some output in Python?

print() function

Q14. What are operators in Python?

Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators


Q15. What is difference between / and // operators?

Float Division("/") and Integer Division("//") 

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```
print("iNeuron"+"iNeuron"+"iNeuron"+"iNeuron")

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

numOne =  int(input("Input number: ").strip())
if numOne % 2 == 0:
    print("Even")
else    :
    print("Odd")

Q18. What are boolean operator?

Logical operator

Q19. What will the output of the following?
```
1 or 0

0 and 0

True and False and True

1 or 0 or 0
```
1
0
False
0


Q20. What are conditional statements in Python?

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

Q21. What is use of 'if', 'elif' and 'else' keywords?

The if/elif/else structure is a common way to control the flow of a program, allowing us to execute specific blocks of code depending on the value of some data.

Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
#A22
age = int(input("What is your age? ").strip())
if age >= 18:
    print("I can vote")
if age < 18:
    print("I can't vote")


Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
#A23 displays the sum of all the even numbers
numbers = [12, 75, 150, 180, 145, 525, 50]
sumOfEven = 0
for num in numbers:
    if num%2 == 0:
        sumOfEven +=num

print(sumOfEven)


Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

#A24
numOne =  int(input("Input first number: ").strip())
numTwo =  int(input("Input second number: ").strip())
numThree =int(input("Input third number: ").strip())
#display the greatest no as output
listOfNumber = [numOne,numTwo,numThree]
print("Largest number is:", max(listOfNumber))

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
#A25.

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:  
 
    if num % 5 == 0:  #The number must be divisible by five      
        if num > 150  and num < 500 : #If the number is greater than 150, then skip it and move to the next number
            continue                       
        elif num > 500 : #If the number is greater than 500, then stop the loop
            print ("Number is greater than 500, loop terminated") 
            break
        else:
            print(num) 
**********************************************************