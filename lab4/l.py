from datetime import date, timedelta

today = date.today()

cherez_100_dney = today + timedelta(days = 100)

print(cherez_100_dney.strftime("%A"))
