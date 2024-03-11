from datetime import datetime

date_1 = "2024-03-04"
date_2 = "2024-03-10"
formatDate = '%Y-%m-%d'

start_datetime = datetime.strptime(date_1, formatDate)
end_datetime = datetime.strptime(date_2, formatDate)


def Fdays():
    # start_datetime

    try:
        day = end_datetime - start_datetime
        print(day)
    except:
        raise ValueError("No es una fecha")


Fdays()
