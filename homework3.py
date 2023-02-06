from datetime import datetime, date, timedelta


users = [{"name": "Tanya", "birthday": date(1960, 2, 11)},
         {"name": "Sonya", "birthday": date(2015, 5, 5)},
         {"name": "Bill", "birthday": date(1965, 2, 8)},
         {"name": "Jill", "birthday": date(1978, 2, 7)},
         {"name": "Kim", "birthday": date(1989, 2, 9)},
         {"name": "Nastya", "birthday": date(1990, 10, 9)}]

weekdays = {
    0: 'Monday',
    1: 'Tuesday', 
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

def birthday(users):
    now = str(datetime.now()).split(' ')
    now = now[0].split('-')
    for it in users:
        birthday_date = str(it['birthday']).split('-')
        birthday_date_now = datetime(year=int(now[0]), month=int(birthday_date[1]), day=int(birthday_date[2]))
        diff = birthday_date_now - datetime.now()
        if timedelta(days=0) < diff < timedelta(days=7):
            weekday = datetime.weekday(birthday_date_now)
            if weekday == 5 or weekday == 6:
                weekday = 0
                print(f"Next {weekdays[weekday]}: {it['name']}")
                continue
            print(f"{weekdays[weekday]}: {it['name']}")

birthday(users)