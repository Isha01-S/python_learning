'''Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of
the exception'''

def main():
    try:
        a = int(input("Hey, Enter a number : "))
        print(a)
        return
    except ValueError as v:
        print("Heyy")
        print(v)
        return

    finally:
        print("I am inside finally.") #excecutes regardless of the error

main()

