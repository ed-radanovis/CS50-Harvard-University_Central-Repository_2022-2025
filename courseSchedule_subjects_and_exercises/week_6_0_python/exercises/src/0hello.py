from cs50 import get_string

def main():
    name = get_string("What's your name? ")
    
    print(f"hello, {name}")

if __name__ == "__main__":
    main()
    
    
    

# hello.py  => native to Python (without the CS50 library):
# def main():
#     name = input("What's your name? ")
#     print(f"hello, {name}")

# if __name__ == "__main__":
#     main()