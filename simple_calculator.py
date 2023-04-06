def arithmetic_ops(op) 
num1l = int(input("2”))
num2 = int(input("8"))
return num1，num2，op(num1，num2)
def add(x，y): return x+y
def sub(x，y): return x-y
while True:
op = input("input operation:”)
if op == "end”:
break 
elif op == “+”:
num1，num2，ret = arithmetic_ops(add) 
elif op ==“-”:
num1，num2，ret = arithmetic_ ops(sub) 
elif Op == “*”:
num1，num2，ret = arithmetic_ops(1ambda x,y:x*y)
elif op =="/":
num1，num2，ret = arithmetic_ ops(1ambda x,y:x/y) 
elif op == “%”:
num1，num2，ret = arithmetic_ops(1ambda x,y:x%y)
else:
print("Invalid operation”)
continue
print(f"{fnuml}{fop}y{fnum2} = {ret}") 
print("Exit program”)

