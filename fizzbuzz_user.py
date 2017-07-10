n = input ("Please input a number we shall be counting to: ")

while not isinstance(n, int):
    try:
        n = int(n)
    except(ValueError):
        n = input("You've not provided a digit, please provide the number again: ")

print ("Fizz buzz counting up to",n)

for i in range(0, n):
    if i % 15 == 0:
        print ("FizzBuzz")
    
    elif i % 3 == 0:
        print ("Fizz")
        
    elif i % 5 == 0:
        print ("Buzz")
            
    else:
        print (i)