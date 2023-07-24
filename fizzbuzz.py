def fizzbuzz(i):
    for x in range(i):
        x = x+1
        # if x is a multiple of 3 and 5 print fizzbuzz
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
        # if x is a multiple of 3 print fizz  
        elif x % 3 == 0: 
            print("fizz")
        # if x is a multiple of 5 print buzz  
        elif x % 5 == 0:
            print("buzz")
        # else print x
        else: print(x)
# value to count up to
fizzbuzz(15)