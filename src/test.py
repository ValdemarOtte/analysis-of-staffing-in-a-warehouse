import numpy as np
import matplotlib.pyplot as plt

data = [
    {5: 906, 7: 41, 6: 33},
    {1: 1195, 3: 1025, 2: 1019, 4: 972, 5: 820, 7: 181},
    {1: 1123, 2: 1113, 3: 1089, 4: 1086, 5: 925, 7: 247},
    {1: 1230, 2: 1147, 3: 1111, 4: 1077, 5: 954, 7: 180},
    {1: 1182, 3: 1161, 2: 1148, 4: 1107, 5: 978, 7: 176, 6: 129},
    {1: 1263, 2: 1164, 3: 1120, 4: 1034, 5: 923, 7: 164, 6: 58},
    {1: 1168, 3: 1167, 2: 1117, 4: 1021, 5: 890, 7: 152},
    {1: 1193, 3: 1028, 2: 1027, 4: 930, 5: 451, 6: 5}
]


u = {
    1: "mand",
    2: "tir",
    3: "ons",
    4: "tors",
    5: "fre",
    6: "lr",
    7: "sn",
}


days = {u[day]: [] for day in range(1, 8)}
for value in data:
    for day in range(1, 8):
        try:
            days[u[day]].append(value[day])
        except KeyError:
            pass

data = {}
for key, value in days.items():
    data[key] = np.mean(value)


categories = list(data.keys())
values = list(data.values())
plt.bar(categories, values)

plt.title('Histogram af dictionary')
plt.xlabel('Dato')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


