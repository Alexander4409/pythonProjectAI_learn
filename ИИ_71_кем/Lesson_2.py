import sys
def password_question():
    password = input("ведите пароль")
    global byts
    byts = sys.getsizeof(password)
def print_size():
    print(f"kb - {byts / 8 / 1024}\n"
        f"mb - {byts / 8 / 1024 / 1024}\n"
        f"gb - {byts / 8 / 1024 / 1024 / 1024}\n"
        f"tb - {byts / 8 / 1024 / 1024 / 1024 / 1024}\n")
while True:
    password_question()
    print_size()
