from datetime import datetime

def leapyear(a, b):
    a = datetime.strptime(a, '%d-%m-%Y')
    b = datetime.strptime(b, '%d-%m-%Y')
    leap = []
    notleap = []
    for year in range(a.year,b.year+1):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap.append(year)
                else:
                    notleap.append(year)
            else:
                leap.append(year)
        else:
            notleap.append(year)
    print("Leap years:", leap)
    print("Non-leap years:", notleap)


a = input()
b = input()
leapyear(a,b)