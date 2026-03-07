from datetime import datetime, timedelta

def is_leap(orbweek):
    return (orbweek + 1) % 5 == 0

def days_in_month(orbweek, month):
    month_days = [16, 11, 16, 15, 16, 15, 16, 16, 15, 16, 15, 16]
    if is_leap(orbweek) and month == 2:
        return 12
    return month_days[month - 1]

def days_in_year(orbweek):
    return 183 if is_leap(orbweek) else 182

def greg2orb(date):
    total_days = date
    orbweek = 0

    while total_days >= days_in_year(orbweek):
        total_days -= days_in_year(orbweek)
        orbweek += 1
    
    month = 1
    while total_days >= days_in_month(orbweek, month):
        total_days -= days_in_month(orbweek, month)
        month += 1
    
    day = total_days + 1
    return orbweek, month, day

def orb2greg(orbweek, month, day):
    total_days = 0

    for week in range(orbweek):
        total_days += days_in_year(week)

    for m in range(1, month):
        total_days += days_in_month(orbweek, m)
    
    total_days += day - 1
    return total_days

def input2days(input_date):
    base_date = datetime(2070, 1, 1)
    target_date = datetime.strptime(input_date, "%Y-%m-%d")
    delta = target_date - base_date
    return delta.days

def days2greg(days_from_base):
    base_date = datetime(2070, 1, 1)
    target_date = base_date + timedelta(days=days_from_base)
    return target_date

def main():
    print("\n")
    print("Orbweek Converter v1.0")
    print("Copyright (c) khangai, 2025-01-08, 2026-01-19")
    print("")
    print("Options:")
    print("    1. Gregorian date => Orbweek date")
    print("    2. Orbweek date => Gregorian date")
    print("\n")

    choice = input("Select an option (1 or 2):")

    if choice == "1":
        input_date = input("Enter an Gregorian date (format: YYYY-MM-DD):")
        greg_days = input2days(input_date)
        orb_date = greg2orb(greg_days)
        print("")
        print(f"Gregorian {input_date} correspond to: Orbweek {orb_date[0]} month {orb_date[1]} date {orb_date[2]}")
    elif choice == "2":
        print("Enter an Orbweek date")
        orbweek = int(input("Orbweek:"))
        month = int(input("month:"))
        day = int(input("date:"))
        days_from_base = orb2greg(orbweek, month, day)
        greg_date = days2greg(days_from_base)
        print("")
        print(f"Orbweek {orbweek} month {month} date {day} correspond to: {greg_date.strftime('%Y-%m-%d')}")
    else:
        print("Invalid option, please run again.")

if __name__ == "__main__":
    main()
    print("\n")
    input("Press return/enter to exit")
