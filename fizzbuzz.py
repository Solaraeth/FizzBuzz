def fizzbuzz():
    # create variable for user input
    i = None
    # validate user input
    while i is None:
        try:
            # ask user for input
            i = int(input("Pick a number: "))
        except ValueError: 
            print("Error: Value is not an integer.")
    
    # iterate through each value between 1 and the user input
    for x in range(i):
        # increase the value of i by 1 to ensure first value is 1
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

# execute function
fizzbuzz()