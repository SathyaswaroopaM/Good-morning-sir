import time
timestramp=time.strftime('%H:%M:%S')

if int(time.strftime('%H'))>=2 and int(time.strftime('%H'))<12:
    print("Good morning sir")

elif int(time.strftime('%H'))>=12 and int(time.strftime('%H'))<16:
    print("Good afternoon sir")

elif int(time.strftime('%H'))>=16 and int(time.strftime('%H'))<20:
    print("Good evening sir")

elif int(time.strftime('%H'))>=20 and int(time.strftime('%H')):
    print("Good night sir")
