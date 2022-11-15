# #Python Basic
# """
# # loop through list
# #

# """
# #A25
# # numbers = [12, 75, 150, 180, 145, 525, 50]

# # for num in numbers:  
 
# #     if num % 5 == 0:  #The number must be divisible by five      
# #         if num > 150  and num < 500 : #If the number is greater than 150, then skip it and move to the next number
# #             continue                       
# #         elif num > 500 : #If the number is greater than 500, then stop the loop
# #             print ("Number is greater than 500, loop terminated") 
# #             break
# #         else:
# #             print(num) 
# # print("**************************")

# # name = input("What is your name ?" ).strip().title()
# # print ("Hello:",name) #Remove white space


# # print("**************************")

# # #A24  
# # numOne =  int(input("Input first number: ").strip())
# # numTwo =  int(input("Input second number: ").strip())
# # numThree =int(input("Input third number: ").strip())
# # #display the greatest no as output
# # listOfNumber = [numOne,numTwo,numThree]
# # print("Largest number is:", max(listOfNumber))

# # print("**************************")

# #A23 displays the sum of all the even numbers
# numbers = [12, 75, 150, 180, 145, 525, 50]
# sumOfEven = 0
# for num in numbers:
#     if num%2 == 0:
#         sumOfEven +=num

# print(sumOfEven)

# #iterate through list 
# print(sum([val for val in numbers if val%2 == 0]))

# #A22 if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

# # age = int(input("What is your age? ").strip())
# # if age >= 18:
# #     print("I can vote")
# # if age < 18:
# #     print("I can't vote")

# #check if the number is odd or even

# # numOne =  int(input("Input number: ").strip())
# # if numOne % 2 == 0:
# #     print("Even")
# # else    :
# #     print("Odd")

# #Dictionary
# userProfile = {'name': "Keyaan"}
# i = 1
# for num in range(5,0,-1) :
    
#     i = num * i
# print(i) 

