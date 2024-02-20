def greeting(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

def count_characters(name):
    return len(name)

def main():
    full_name = input("Enter your full name:\n")
    name_arr = full_name.split(" ")
    name_greeting = greeting(name_arr[0], name_arr[1])
    print(name_greeting)
    print(f"Your full name has {count_characters(full_name)} characters!")

# main()
