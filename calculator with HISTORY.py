HISTORY_FILE = "history.txt"

def show_history():
    file=open(HISTORY_FILE,'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("NO History Found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file=open(HISTORY_FILE,'w')
    file.close()
    print("History Cleared")

def Save_to_history(equation,result):
    file=open(HISTORY_FILE,'a')
    file.write(equation + "=" + str(result) + "\n") # we cannot add text + number
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid Input... use below format (e.g 12 + 30)")
        return  
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2 
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2 
    else:
        print("Invalid Operator .. Use only + - * /")
        return

    if int(result) == result:
        result = int(result)
        """if result == 10.0
        int(10.0) => 10
        10 == 10.0 =>true,because python consider them in equal in value
        if result == 10.5
        int(10.5) => 10
        10 == 10.5 =>false"""
        print("Result:",result)
        Save_to_history(user_input,result)
    
def main():
    print("---SIMPLE CALCULATOR with History---")
    while True:
        user_input = input("Enter calculation(+ - * /) or command (History,Clear or Exit) = ")
        if user_input == "Exit":
            print("Goodbye")
        elif user_input == "History":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()


     

    


  