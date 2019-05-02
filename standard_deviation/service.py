import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
from django.conf import settings


def calculate_standard_deviation_for_days():

    df = pd.read_csv(settings.BASE_DIR +
                     "/standard_deviation/bike_sharing_dataset/day.csv")

    weekday_dfs = []
    for i in range(len(df["weekday"].unique())):
        temp_df = df[df["weekday"] == i]
        weekday_dfs.append(temp_df)

    registered_users = {}
    casual_users = {}
    for i, weekday in enumerate(weekday_dfs):

        registered_users[i] = weekday["registered"].std()
        casual_users[i] = weekday["casual"].std()

    weekdays_map = {
        '1': "Monday",
        '2': "Tuesday",
        '3': "Wednesday",
        '4': "Thursday",
        '5': " Friday"
    }
    print(weekdays_map.get("1",'fdsf'))
    temp = {weekdays_map.get(k,k): v for k, v in registered_users.items()}
    print(temp)
    # return registered_users, casual_users
    return temp, casual_users
