from datetime import datetime, timedelta

def isLeap(orbweek):
    return (orbweek + 1) % 5 == 0

def daysInMonth(orbweek, month):
    monthDays = [16, 11, 16, 15, 16, 15, 16, 16, 15, 16, 15, 16]
    if isLeap(orbweek) and month == 2:
        return 12
    return monthDays[month - 1]

def daysInYear(orbweek):
    return 183 if isLeap(orbweek) else 182

def greg2orb(date):
    totalDays = date
    orbweek = 0

    while totalDays >= daysInYear(orbweek):
        totalDays -= daysInYear(orbweek)
        orbweek += 1
    
    month = 1
    while totalDays >= daysInMonth(orbweek, month):
        totalDays -= daysInMonth(orbweek, month)
        month += 1
    
    day = totalDays + 1
    return orbweek, month, day

def orb2greg(orbweek, month, day):
    totalDays = 0

    for week in range(orbweek):
        totalDays += daysInYear(week)

    for m in range(1, month):
        totalDays += daysInMonth(orbweek, m)
    
    totalDays += day - 1
    return totalDays

def input2days(inputDate):
    baseDate = datetime(2070, 1, 1)
    targetDate = datetime.strptime(inputDate, "%Y-%m-%d")
    delta = targetDate - baseDate
    return delta.days

def days2greg(daysFromBase):
    baseDate = datetime(2070, 1, 1)
    targetDate = baseDate + timedelta(days=daysFromBase)
    return targetDate

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
        inputDate = input("Enter an Gregorian date (format: YYYY-MM-DD):")
        gregDays = input2days(inputDate)
        orbDate = greg2orb(gregDays)
        print("")
        print(f"Gregorian {inputDate} correspond to: Orbweek {orbDate[0]} month {orbDate[1]} date {orbDate[2]}")
    elif choice == "2":
        print("Enter an Orbweek date")
        orbweek = int(input("Orbweek:"))
        month = int(input("month:"))
        day = int(input("date:"))
        daysFromBase = orb2greg(orbweek, month, day)
        gregDate = days2greg(daysFromBase)
        print("")
        print(f"Orbweek {orbweek} month {month} date {day} correspond to: {gregDate.strftime('%Y-%m-%d')}")
    else:
        print("Invalid option, please run again.")

if __name__ == "__main__":
    main()
    print("\n")
    input("Press return/enter to exit")
