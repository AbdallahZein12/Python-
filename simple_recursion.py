def main():
    print("\033[32m", "Welcome!", "\033[0m")
    print()
    print()

    while True:
        try:
            input1 = input("Input your number> ")

            int(input1)

            break

        except:
            print()
            print("\033[31m", "Error please try again!", "\033[0m")
            print()
            continue

    def factorial(i):
        if i == 1:
            return 1
        else:
            return i * factorial(i - 1)

    i = int(input1)

    result = factorial(i)

    print()
    print(f"The factorial of {input1} is {result}")
    print()


main()
