import os
import time
from termcolor import colored

interval_s = 1

workouts = [
    {'title': 'jumping jacks', 'description': 'blah'},
    {'title': 'pushups', 'description': 'blah'},
]

for workout in workouts:
    print(colored(workout['title'], 'green'), colored(workout['description'], 'magenta'))
    time.sleep(interval_s)
    os.system('say "Next"')
