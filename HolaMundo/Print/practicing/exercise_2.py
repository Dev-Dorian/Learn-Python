from multiprocessing.sharedctypes import Value
DAYS_MONTHS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def how_many_days(first_date: str, second_date: str):

    if (first_date.count("/") < 2) or (second_date.count("/") < 2):
        raise ValueError("El formato de la fecha no es la correcta, faltan datos o no se utilizaron los separadores"
                         " correctos.")

    day_one, month_one, year_one = first_date.split("/")
    day_two, month_two, year_two = second_date.split("/")

    try:

        day_one = int(day_one)
        month_one = int(month_one)
        year_one = int(year_one)

        day_two = int(day_two)
        month_two = int(month_two)
        year_two = int(year_two)
    except:
        raise ValueError("Los valores ingresados en la fecha, no son del tipo necesitado o no son del tipo entero. \n"
                         "\tVerifique que las fechas están en el formato dd/MM/yyyy, por ejemplo 24/12/2000.")

    if not (0 < day_one <= 31) or not (0 < month_one <= 12) or not (0 < year_one):
        raise TypeError(f"El valor ingresado {
                        first_date} no está en el formato especificado.")

    if not (0 < day_two <= 31) or not (0 < month_two <= 12) or not (0 < year_two):
        raise TypeError(f"El valor ingresado {
                        second_date} no está en el formato especificado.")

    print(day_one, month_one, year_one)
    print(day_two, month_two, year_two)


how_many_days("-1/-m2/-3", "4/6/7")
