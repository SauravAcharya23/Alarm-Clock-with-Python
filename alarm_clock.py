from datetime import datetime
from playsound import playsound


alarm_time = input("Enter the time of alarm in HH:MM:SS \n")

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]

alarm_period = alarm_time[9:].upper()

print(f"Your alarm is set to {alarm_time}.....")



while True:
    now = datetime.now()
    current_hour = now.strftime("%I") # 12-hour format
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    current_period = now.strftime("%p")
    
    if(alarm_period == current_period):
        if(alarm_hour == current_hour):
            if(alarm_minute == current_minute):
                if(alarm_second == current_second):
                    print("Wake Up!!")
                    playsound("alarm.mp3")
                    break
                    
                    