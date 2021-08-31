def main():
    password = input("Please type your password: ")

    if len(password) <= 4:
        print("Your password is too short.")

    else:
        astrist = len(password) * "*"
        print(stars)
main()