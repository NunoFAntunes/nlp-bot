import re
import os

hour_regex = r'[0-9]+ *(hour|h)' # 1 or more 0-9, 0 or 1 spaces and hour or h
minutes_regex = r'[0-9]+ *(minute|min)'
seconds_regex = r'[0-9]+ *(seconds|sec)'
value_regex = r'[0-9]+'

def find_timer_time(text):
    timer_type = 0 # 0 is seconds, 1 is minutes, 2 is hours.
    hours = re.search(hour_regex, text)
    minutes = re.search(minutes_regex, text)
    seconds = re.search(seconds_regex, text)
    
    total_seconds = 0 
    if hours is not None:
        print("Entered hours")
        hours = int(re.search(value_regex, hours.group()).group())
        total_seconds += hours * 3600
    if minutes is not None:
        print("Entered minutes")
        minutes = int(re.search(value_regex, minutes.group()).group())
        total_seconds += minutes * 60
    if seconds is not None:
        print("Entered seconds")
        seconds = int(re.search(value_regex, seconds.group()).group())
        total_seconds += seconds
    print("I'm in time finder")
    print(total_seconds)
    return total_seconds, timer_type