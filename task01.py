import datetime

def get_days_from_today(date): 
    try:
        current_time = datetime.datetime.today()

        date = datetime.datetime.strptime(date,"%Y-%m-%d")

        difference = current_time - date 

        return difference.days
    
    except ValueError: 
        return "Enter date in ""YYYY-MM-DD"" format only"                         

res = get_days_from_today("2024-04-23")

print(res)