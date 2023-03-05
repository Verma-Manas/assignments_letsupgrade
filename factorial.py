def fact(n):
    if n < 0:
        return 'Factorial does not exist'
    elif n == 0:
        return 1
    else:
         fact = 1
    for i in range (1, num + 1):
        fact = fact * i
    return (fact)

num = int(input("Enter a number: "))
print(fact(num))
