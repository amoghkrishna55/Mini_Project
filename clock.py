#defining the main component
def clock_angle(time):
  hours, minutes = time.split(":")
  hours = int(hours)
  minutes = int(minutes)
  hour_angle = (hours / 12 + minutes / 60 / 12) * 360
  minute_angle = (minutes / 60) * 360
  angle = abs(hour_angle - minute_angle)
  if angle > 180:
    angle = 360 - angle
  print("Angle between hour({0}) and minute({1}) hand is {2} degrees".format(hours, minutes, angle))

#To run program while its true
def main():
    while True:
        user = input("Enter the time in Hour:Minute format: ")
        hours, minutes = user.split(":")
        hours = int(hours)
        minutes = int(minutes)
        if hours >0 and hours <=12 and minutes >= 0 and minutes <= 59:
            clock_angle(user)
            loop = input("Do you want to continue Y/N: ").upper()
            if loop == 'N':
                break
        else:
            print ("Enter valid time")

#executing the function
main()