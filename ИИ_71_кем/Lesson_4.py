def main():
    password = input("Enter user password: ")
    password_bytes = password.encode("utf-8")
    byte_count = len(password_bytes)
    print("Choose unit to convert to:")
    print("1. KB")
    print("2. MB")
    print("3. GB")
    print("4. TB")

    try:
        user_choice = int(input("Your choice (1-4): "))
    except ValueError:
        print("Error: please enter a number between 1 and 4.")
        return

    units = {
        1: (1024, "KB"),
        2: (1024**2, "MB"),
        3: (1024**3, "GB"),
        4: (1024**4, "TB")
    }

    if user_choice in units:
        divider, unit_name = units[user_choice]
        res = byte_count / divider
        print(f"Result: {byte_count} bytes = {round(res, 4)} {unit_name}")
    else:
        print("Error: invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
