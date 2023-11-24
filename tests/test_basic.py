# content of test_sample.py

import pandas as pd


def test_check_dataframe_size():
    df = pd.read_csv("../formulaone/Data/TidyData/tidydata.csv")
    iron_man_3 = "Iron Man 3" in df["title"].values
    parkland = "Parkland" in df["title"].values

    if iron_man_3:
        print("Iron Man 3 ist in dem Datensatz vorhanden!")
    else:
        print("Iron Man 3 ist NICHT in dem Datensatz vorhanden!")
    
    if parkland:
        print("Parkland ist in dem Datensatz vorhanden!")
    else:
        print("Parkland ist NICHT in dem Datensatz vorhanden!")


test_check_dataframe_size()