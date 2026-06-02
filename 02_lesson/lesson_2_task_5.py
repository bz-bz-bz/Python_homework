def month_to_season(m):

    if m == 12 or m == 1 or m == 2:
        return "Зима"
    elif m <= 3 or m <= 5:
        return "Весна"
    elif m <= 6 or m <= 8:
        return "Лето"
    elif m <= 9 or m <= 11:
        return "Осень"
    else:
        return "Несуществующий номер месяца"


print(month_to_season(13))
