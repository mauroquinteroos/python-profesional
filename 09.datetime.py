import datetime


# Si la computadora tiene una zona horaria configurada, te traerá la hora y la fecha configurada.
# Si la computadora no tiene una zona horaria configurada, traerá la hora en formato UTC.
my_time = datetime.datetime.now()
print("datetime now: ", my_time)

my_time_utc = datetime.datetime.utcnow()
print("datetime utcnow: ", my_time_utc)

my_day = datetime.date.today()
print("date today: ", my_day)
print(f"year: {my_day.year}")
print(f"month: {my_day.month}")
print(f"day: {my_day.day}")

format_str1 = my_time.strftime("%d/%m/%Y")
print(f"Formato Latam: {format_str1}")

format_str2 = my_time.strftime("%m/%d/%Y")
print(f"Formato USA: {format_str2}")

format_str3 = my_time.strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha y Hora: {format_str3}")

format_str4 = my_time.strftime("%d/%m/%Y %I:%M:%S %p")
print(f"Fecha y Hora (12 horas): {format_str4}")

format_str5 = my_time.strftime("%d %B %Y")
print(f"Fecha: {format_str5}")
