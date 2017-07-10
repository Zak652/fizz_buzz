import sys

while len (sys.argv) < 2:
    print ("you provided nothing")

print ("Fizz buzz counting range")

for arg in sys.argv[1: ]:
    if arg % 15 == 0:
        print ("FizzBuzz")
    
    elif arg % 3 == 0:
        print ("Fizz")
        
    elif arg % 5 == 0:
        print ("Buzz")
            
    else:
        print (arg)