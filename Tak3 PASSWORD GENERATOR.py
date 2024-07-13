import random
import string

def gen_password(length, complexity):
    if complexity == 'simple':
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choices(characters, k=length))
    elif complexity == 'strong':
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
    else:
        raise ValueError("\nChoose 'simple' or 'strong'.")
    
    return password

def save(password, filename="passwords.txt"):
    with open(filename, "a") as file:
        file.write(password + "\n")

def password_generator():
    print("\n*-*-*-*- Welcome to Password Generator! -*-*-*-*")
    while True:
        try:
            length = int(input("\nEnter the length of the password: "))
            if length <= 0:
                print("\n Invalid length. Please enter a positive integer.")
                continue
            
            complexity = input("\nEnter the password complexity (simple/strong): ").lower()
            password = gen_password(length, complexity)
            print(f"\n Generated password: {password}")

            if input("\nDo you want to save this password? (yes/no): ").lower() == "yes":
                save(password)
                print("\nPassword saved successfully!")

            if input("\nDo you want to generate another password (yes/no): ").lower() != "yes":
                print("\n we are Exiting Password Generator. Goodbye!")
                break

        except ValueError as e:
            print(f"\nInvalid input. {e}")

password_generator()
