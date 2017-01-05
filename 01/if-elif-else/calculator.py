a = input("Enter a: ")
a = int(a)
b = input("Enter b: ")
b = int(b)
oper = input("Enter operation: ")


if oper == "+":
    result = a + b
elif oper == "-":
    result = a - b
elif oper == "*":
    result = a * b
elif oper == "/":
    result = a / b
else:
	print "Error" 
	result = False

if result != False:
    print("Result is:")
    print(result)

