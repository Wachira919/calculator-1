def calc():
    print("This is a python built calculator.\n Type `quit ` to exit")
    while True:
         user_input = input("Enter you calculations here: ")
         if user_input.lower() == 'quit':
            print("Good bye")
            break
         try:
             operations = {
                 'abs': abs,
                'float': float,
                'int': int,
                'pow': pow,
                'round': round
             }

             result = eval(user_input, {"__builtins__": None}, operations )
             print(f"Result: {result}")
         except Exception as e:
             print("Please enter a valid calculation.\n Example 2+3")



calc()