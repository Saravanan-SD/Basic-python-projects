def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def product(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

print("Select operation\n"
             "1.Add\n"
             "2.sub\n"
             "3.Product\n"
             "4.Divide\n")
select=int(input("Select operation- "))

n1,n2=input("Please enter the value- ").split()

n1=int(n1)
n2=int(n2)

if select==1:
    print(add(n1,n2))

elif select==2:
    print(sub(n1,n2))

elif select==3:
    print(product(n1,n2))
elif select==4:
    print(divide(n1,n2))
else:
    print("invalid")






