def greeting(name):
    if name.lower() == "bond" or name.lower() == "james bond":
        return "Welcome on board 007"
    
    return f"Hello, {name}"
    
    

def main():
    print(greeting(input("Enter your name:\n")))

main()