#function to reverse the given string
def my_reverse(name):
    string2 = ''
    for i in string:
        string2 = i + string2 
    return string2
string=input("Enter the name to be reversed")
print("The original string is: ",string)  
rever_name=my_reverse(string)
print("The reverse string is",rever_name)