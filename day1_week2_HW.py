# Question 1
        
def calculator():
    a = int(input("First number: "))
    b = int(input("Second number: "))

    operator = input("What would you like to use? +, -, *, /: ")

    if operator == '+':
        results = a + b 
    elif operator == '-':
        results = a - b
    elif operator == '*':
        results = a * b 
    elif operator == '/':
        if b != 0:
            results = a / b
        else:
            print("Not allowed to use 0")
            return
    print(f"The results of {a} {operator} {b} is: {results}")




calculator()



#--------------------------------------------------------------------------------#
# Question 2

shopping_cart = []
flag = True

while flag:
    user_input = int(input('''What would you like to do?
    1 - Add to list
    2 - View list
    3 - Delete item
    4 - End
    '''))
    if user_input == 1:
        add = input("What would you like to add?")
        shopping_cart.append(add)
        done = input("add or back to options: ")
        if done == 'add':
            add_more = input("What else?: ")
            shopping_cart.append(add_more)
        elif done == 'back':
            continue 
    elif user_input == 2:
        print(shopping_cart)
    elif user_input == 3:
        print(shopping_cart)
        remove = input("What would you like to remove?")
        shopping_cart.remove(remove)
    elif user_input == 4:
        flag = False
        print(f"This is your shopping cart: {shopping_cart}")