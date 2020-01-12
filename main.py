import os
import time
import pandas as pd
from termcolor import colored
from tqdm import tqdm

interval_s = 8
dir_path = os.path.dirname(os.path.realpath(__file__))
workouts_df = pd.read_csv(os.path.join(dir_path, 'workouts.csv'))

for _, row in workouts_df.iterrows():
    print(colored(row.workout, 'green'), colored(row.description, 'magenta'))
    for i in tqdm(range(interval_s)):
        time.sleep(1)
    os.system('say "Next"')
