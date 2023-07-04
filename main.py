# write a function calculate the 2nd power of a number
# return thr result from the function and print the result

a = int(input("enter your value:"))
n = int(input("enter the power:"))

def power(a,n):
    pow = a**n
    print(pow)
    return power

power(a,n)
