import datetime

def get_upcoming_birthdays(users):

    current_date = datetime.datetime.today().date()
    birthday_list = []

    for user in users: 
        user_birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=current_date.year)

        if user_birthday < current_date:
            user_birthday = user_birthday.replace(year= current_date.year + 1)
        else: 
            days_before_birthday = (user_birthday - current_date).days
            if 0 <= days_before_birthday < 7 and user_birthday.weekday() < 5: 
                    birthday_list.append(
                        {
                          f'name': user['name'] , 'congratulation_date': user_birthday.strftime('%Y.%m.%d')
                        }
                    )
            else: 
                 monday_date = 7 + days_before_birthday - user_birthday.weekday()
                 user_birthday = user_birthday.replace(day= current_date.day + monday_date)
                 birthday_list.append(
                        {
                          f'name': user['name'] , 'congratulation_date': user_birthday.strftime('%Y.%m.%d')
                        }
                    )
                    
                
    return birthday_list




users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1993.01.27"},
    {"name": "Alex Smith", "birthday": "1996.04.24"},
    {"name": "Julie Smith", "birthday": "1993.04.25"},
    {"name": "Max Smith", "birthday": "1998.04.26"},
    {"name": "Daniel Smith", "birthday": "1991.04.28"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)


