#function to find max of 2 numbers
def maximum(num1, num2): 
      
    if num1 >= num2: 
        return num1 
    else: 
        return num2 
      
 
n1 = int(input("Enter the number:"))
n2 = int(input("Enter the number:"))
print(maximum(n1,n2))