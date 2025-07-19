from datetime import datetime, timedelta
import time
import pygame

# alarm setting, allow the user to set a alarm clock and ring when the user's time is reach, allow also the user to snozze the alarm for 5s
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def set_alarm_time():

    # ask for the hour
    while True:
        hour = input("Enter the hour (0h-23h): ")
        if hour.isdigit() and 0 <= int(hour) <= 23:
            hour = f"{int(hour):02d}"
            break
        else:
            print("Invalid input! Enter a number between 0-23")
    # ask for the minutes
    print('-'*50)
    while True:
        minute = input("Enter the minute (0-59): ")
        if minute.isdigit() and 0 <= int(minute) <= 59:
            minute = f"{int(minute):02d}"
            break
        else:
            print("Invalid character! Enter a number between 0-23")

    # ask for the seconds
    print('-'*50)
    while True:
        second = input("Enter the second (0-59): ")
        if second.isdigit() and 0 <= int(second) <= 59:
            second = f"{int(second):02d}"
            break
        else:
            print("Invalid input! Enter a number between 0-59")

    return f"{hour}:{minute}:{second}"


def clock_ringing():
    pygame.mixer.init()
    pygame.mixer_music.load("mp3.mp3")
    pygame.mixer_music.play()
    time.sleep(10)
    pygame.mixer_music.stop()


def current_time_and_ringing(alarm_time):
    print(CLEAR)
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(
            f"{CLEAR_AND_RETURN}|Alarm set for: {alarm_time} |The current time is: {current_time}|")

        if current_time == alarm_time:
            print(f"\n ⏰ GET UP ⏰ It's {current_time}")
            clock_ringing()
            break
        time.sleep(1)


def main():
    alarm_time = set_alarm_time()
    current_time_and_ringing(alarm_time)
    # SNOZZE
    while True:
        snooze = input("Type 's' to snozze or 'q' to quit:  ")
        if snooze.isalpha() and snooze.lower()[0] == 's':
            snooze_second = input("Enter the second you want to add: ")
            if snooze_second.isdigit() and 0 <= int(snooze_second) <= 59:
                current_time = datetime.now() + timedelta(seconds=int(snooze_second))
                alarm_time = current_time.strftime("%H:%M:%S")
                current_time_and_ringing(alarm_time)
                continue
            else:
                print("Enter a number between 0 and 59")
        else:
            print("BYE")
            break


main()
