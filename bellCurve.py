import random
import plotly.figure_factory as pf
import plotly.express as px
import pandas as pd
from collections import Counter

dataFrame = pd.read_csv("HeightAndWeightInformation.csv")


dice_results = []
count = []

for i in range(1, 100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_results.append(dice1 + dice2)
    count.append(i)

data = Counter(dice_results)
mode_data_for_range = {
    "1-4": 0,
    "4-6": 0,
    "6-8": 0,
    "8-10": 0,
    "10-12": 0
}

for diceData, occurence in data.items():
    if 1 < int(diceData) < 4:
        mode_data_for_range["1-4"] += occurence
    elif 4 < int(diceData) < 6:
        mode_data_for_range["4-6"] += occurence
    elif 6 < int(diceData) < 8:
        mode_data_for_range["6-8"] += occurence
    elif 8 < int(diceData) < 10:
        mode_data_for_range["8-10"] += occurence
    elif 10 < int(diceData) < 12:
        mode_data_for_range["10-12"] += occurence

mode_range, mode_occurence = 0, 0

for rang, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = rang, occurence

print(mode_range)

# print(mode_data_for_range)

# print(data)

for x in range(1, 100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_results.append(dice1 + dice2)
    count.append(x)

for y in range(1, 100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_results.append(dice1 + dice2)
    count.append(y)


# graph = pf.create_distplot(["Results"], [dice_results])
# graph.show()

# graph = pf.create_distplot([dataFrame["Weight(Pounds)"].tolist()], ["Height"])
# graph.show()

# graph = px.bar(x=count, y=dice_results)
# graph.show()

print(dice_results)
