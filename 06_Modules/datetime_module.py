from datetime import datetime, timedelta
now = datetime.now()
print("Now:", now)
print("Formatted:", now.strftime("%d-%m-%Y %H:%M"))
print("Tomorrow:", (now + timedelta(days=1)).date())
