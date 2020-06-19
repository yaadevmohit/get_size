import pandas as pd
import numpy as np
df = pd.read_csv('names.csv')


def get_size(number, type):
    min_value = df[(df.type == type)].iloc[0].to_dict()["Min"]  # min value for the type selected
    max_value = df[(df.type == type)].iloc[-1].to_dict()["Max"] # max value for the type selected
    if 0 < (min_value - number) <= 2:
        print(df[(df.type == type)].iloc[0].to_dict()["store_size"])
    elif 0 < (number - max_value) <= 0.5:
        print(df[(df.type == type)].iloc[-1].to_dict()["store_size"])
    elif min_value <= number <= max_value:
        y = df[(df.Min <= number) & (df.Max >= number) & (df.type == type)].iloc[:]
        if len(y) == 2:
            y = df[(df.Min <= number) & (df.Max >= number) & (df.type == type)].iloc[-1].to_dict()
        else:
            y = df[(df.Min <= number) & (df.Max >= number) & (df.type == type)].iloc[0].to_dict()

        print(y["store_size"])
    else:
        return None


get_size(30.6, "WAIST")
