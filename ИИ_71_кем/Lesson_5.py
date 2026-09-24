thirty_days = {4, 9, 6, 11}
thirty_one_days = {1 ,3, 5, 7, 8, 10, 12}

def check_date(date):
    date = date.strip()
    day, month, year = date.split(".")

    day = int(day)
    month = int(month)
    year = int(year)

    if day <= 31 and month <= 12 and year <= 9999:
        if month in thirty_days:
            if day <= 30:
                return "Date good"
            else:
                return "Date is bad"
        elif month in thirty_one_days:
            return "Date good"
        elif month == 2:
            if day <= 28:
                return "Date good"
            elif day == 29 and year % 4 == 0:
                return "Date good"
            else:
                return "Date is bad"
        else:
            return "Date is bad"

    else:
        return "Неверный формат даты"

def main():
    input_date = input("Введите дату: ")
    print(check_date(input_date))

main()
