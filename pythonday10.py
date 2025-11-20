def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Error: Oops, you can't divide by zero, buddy."
    return n1 // n2 

def giant_calc_function():
    # this holds the result so we can keep going
    last_answer = None

    # this lets us look up the function we need
    ops_map = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div
    }

    print("--- Let's do some math ---")

    while True:
        print("\n--- Next Calculation ---")
        
        # Figure out the first number
        if last_answer is None:
            # New start
            try:
                num1 = float(input("First number: "))
            except ValueError:
                print("Bad number, try again.")
                continue
        else:
            # Use the old result
            num1 = last_answer
            print(f"First number is the last answer: {num1}")

        # Get the second number
        try:
            num2 = float(input("Second number: "))
        except ValueError:
            print("Bad number, try again.")
            if last_answer is not None:
                last_answer = None
            continue

        # Get the operation
        op_input = input("What op? (add, sub, mult, div): ").lower()
        
        # Find the function in the map
        chosen_func = ops_map.get(op_input)
        
        current_result = None
        if chosen_func:
            current_result = chosen_func(num1, num2)
        else:
            current_result = "Error: That's not a real op."

        print(f"\nAnswer is: {current_result}")

        # Save the result if it wasn't an error
        if isinstance(current_result, (int, float)):
            last_answer = current_result
        else:
            last_answer = None

        # Do you want to keep going?
        while True:
            # We don't need all those prints, just one for the loop
            go_on = input("Keep going with the answer (y), new numbers (n), or quit (q)? ").lower()
            if go_on in ['y', 'n', 'q']:
                break
            print("Just 'y', 'n', or 'q'.")

        if go_on == 'q':
            print("Bye!")
            return

        if go_on == 'n':
            last_answer = None # Forget the last answer and start over

# run the whole giant thing
giant_calc_function()