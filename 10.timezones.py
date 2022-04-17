import pytz
from datetime import datetime


buenos_aires_timezone = pytz.timezone("America/Argentina/Buenos_Aires")
buenos_aires_date = datetime.now(tz=buenos_aires_timezone)
print(f"Buenos Aires: {buenos_aires_date.strftime('%d/%m/%Y, %H:%M:%S')}")

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(tz=mexico_timezone)
print(f"Ciudad de México: {mexico_date.strftime('%d/%m/%Y, %H:%M:%S')}")

zurich_timezone = pytz.timezone("Europe/Zurich")
zurich_date = datetime.now(tz=zurich_timezone)
print(f"Zurich: {zurich_date.strftime('%d/%m/%Y, %H:%M:%S')}")
