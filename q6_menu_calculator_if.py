print ("1.Add 2.subtract 3.multiply 4.divide")
choice =int(input("Enter your choice:"))

a=int(input("Enter first choice:"))
b=int(input("Enter second choice:"))

if choice == 1:
    print("sum =", a+b)
elif choice == 2:
    print("difference =", a-b)
elif choice == 3:
    print ("product =", a*b)
elif choice == 4:
    print("division =", a/b)
