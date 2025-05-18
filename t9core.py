# the script is going to become a calculater with 


#declartion
num_1 =0
num_2 = 0
result = 0

#input
num_1 = input ("enter 1st number: ")
num_2 = input ("enter 2nd number: ")
opr = input("select an operation - or + : ")
#process
if opr == "-":
    result = int(num_1)- int(num_2)  # storing subtraction result
elif opr == "+":
    result = int(num_1) + int(num_2)
#output
result = result
print("result is: ", result) 