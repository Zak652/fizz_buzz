n = 100
num_count = 0

print ("Fizz buzz counting up to",n)

while num_count < n:
    num_count += 1
    
    if num_count % 3 == 0 and num_count % 5 == 0:
        print ("FizzBuzz")
    
    elif num_count % 3 == 0:
        print ("Fizz")
        
    elif num_count % 5 == 0:
        print ("Buzz")
            
    else:
        print (num_count)