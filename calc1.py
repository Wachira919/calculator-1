def calc():
    print("Simple calculator.\n Enter `quit` to exit.")
    while True:
        user_input = input("Enter the calculations:  ")
        if user_input.lower() == 'quit':
            print("Bye Bye see you later.")
            break
        try:
            components = user_input.replace(" ", "").replace("+=","+").replace("-=", '-')
            if '+' in components:
                result = sum(float(n) for n in components.split('+'))
            elif '-' in components:
                components = components.split("-")
                result = float(components[0])
                for n in components[1:]:
                    result -= float(n)
            elif '*' in components:
                components = components.split('*')
                result = float(components[0])
                for n in components[1:]:
                    result *= float(n)
            elif "/" in components:
                components = components.split('/')
                result = float(components[0])
                for n in components[1:]:
                    result /= float(n)
            elif "pow" in components:
                components = components.split('pow')
                result = pow(components)
            else:
                print('Please enter a valid input. \n Example 2+3 2-4')

            
            print(f"result: {result}")   
        except Exception as e:
            print(f'The following was the error: {e}')







if __name__ == "__main__":
    calc()