a=int(input("Enter mark tamil"))
b=int(input("Enter mark english"))
c=int(input("Enter mark maths"))
d=int(input("Enter mark biology"))
e=int(input("Enter mark chemistry"))

sum=a+b+c+d+e
print(sum)
Total=sum/5
print(Total)

if Total>91:
    print("A grade")
elif Total>=80 and Total<=90:
    print("B grade")
elif Total>=70 and Total <= 79:
    print("C grade")
elif Total>=60 and Total <=69:
    print("D grade")
else:
    print("FAil")
