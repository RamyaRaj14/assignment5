#function to print odd number up to given number
def odd_numbers(start,end):
    for num in range(start, end + 1): 
        if num % 2 != 0: 
           print(num, end = " ") 

n1 = int(input("Enter the start of range: ")) 
n2 = int(input("Enter the end of range: ")) 
result=odd_numbers(n1,n2)
