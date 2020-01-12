import os
import time
import pandas as pd
from termcolor import colored

interval_s = 1
dir_path = os.path.dirname(os.path.realpath(__file__))
workouts_df = pd.read_csv(os.path.join(dir_path, 'workouts.csv'))
# os.system('say "Get ready to get your booty worked"')
for _, row in workouts_df.iterrows():
    print(colored(row.workout, 'green'), colored(row.description, 'magenta'))
    time.sleep(interval_s)
    os.system('say "Next"')
