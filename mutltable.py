#function to print the multiplication table of the given number

def table(num):
    print("Multiplication Table of", num)
    for i in range(1, 11):
        print(num,"X",i,"=",num * i)


num = int(input("Enter the number: "))
result=table(num)

