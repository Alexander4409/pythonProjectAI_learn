import  math

def ask(sim_count, pass_count, users_count):
    bait_on_token = math.sqrt(sim_count)

    pass_len = bait_on_token * pass_count
    result = pass_len * users_count

    result = round(result)

    return f"bits: {result}"

def main():
    sim = int(input("Введите кол-во символов алфавита: "))
    pas = int(input("Введите кол-во символов пароля: "))
    users = int(input("Введите кол-во пользователей:"))

    print(ask(sim, pas, users))

main()

