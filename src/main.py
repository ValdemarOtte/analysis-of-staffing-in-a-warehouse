### Imports
# Standard library
from pathlib import Path

# Third-party libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Local files


DATA_PATH: Path = Path("data\\datasample.csv")
WEEKDAYS: dict[int, str] = {
    1: "mandag",
    2: "tirdag",
    3: "onsdag",
    4: "torsdag",
    5: "fredag",
    6: "lørdag",
    7: "søndag",
}


# Matplotlib style config
plt.style.use("ggplot")

  
def convert_to_float(strin):
    """
    
    e.x. iven te strin `"0,282"`, ten te function will return te float `0.282`.
    
    """
    return float(strin.replace(",", "."))


def plot_histogram(
        data: dict[str, list[int | float]],
        title: str = "Histogram", 
        xlabel: str = "X label",
        ylabel: str = "Y label"
    ) -> None:
    """
    Plots a histogram from a dictionary of keys and their corresponding values.

    Args:
    ----
        data: A dictionary object.
        title: The title of the histogram. Defaults to `Histogram`.
        xlabel: The label for the x-axis. Defaults to `X label`.
        ylabel: The label for the y-axis. Defaults to `Y label`.

    """
    keys = list(data.keys())
    values = list(data.values())
    plt.bar(keys, values, color="#4169E1")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    
def plot_lineplot(
        data: dict[str, list[int | float]],
        title: str = "Line-plot", 
        xlabel: str = "X label",
        ylabel: str = "Y label"
    ) -> None:
    """
    Plots a line-plot from a dictionary of keys and their corresponding values.

    Args:
    ----
        data: A dictionary object.
        title: The title of the line-plot. Defaults to `Line-plot`.
        xlabel: The label for the x-axis. Defaults to `X label`.
        ylabel: The label for the y-axis. Defaults to `Y label`.

    """
    keys = list(data.keys())
    values = list(data.values())
    plt.plot(keys, values, color="#4169E1", marker='o', linestyle='-', linewidth=2)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def step_1() -> None:
    """
    Load data in and plot frequenli of `Frigivelsesdato` as a histogram.
    """
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    data = df["Frigivelsesdato"].value_counts().to_dict()
    plot_histogram(data, "Histogram over friveks af bestillin over datoer", "Frigivelsesdatoer", "frequns")


def step_2() -> None:
    # Vi fratage uge 52 og 53 (uge 01 i år 2025), da det er midt i juleferien,
    # hvilket ikke er med til at give et retvisende billede for en vagtplan.
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    data = df["Frigivelsesdato"].value_counts().to_dict()
    plot_histogram(data)
    
    

def step_3() -> None:
    """
    
    """
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    print(f"Mindste værdi : {df['Antal_linjer'].min()}")
    print(f"Største værdi : {df['Antal_linjer'].max()}")
    print(f"Gennemsnit    : {df['Antal_linjer'].mean():.2f}")
    print(f"Spredning     : {df['Antal_linjer'].var():.2f}")
    print(f"Median        : {df['Antal_linjer'].median()}")

    


def step_4():
    df = pd.read_csv(DATA_PATH, delimiter=";")
    data = dict(zip(df["Antal_linjer"], df["Teoretisk_bemandning"]))

    for key, value in data.items():
        data[key] = convert_to_float(value)
    plot_lineplot(data)



def step_5(column: str) -> None:
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")

    for warehouse in df["Lager"].unique():
        temp_df = df[df["Lager"] == warehouse]
        data = temp_df[column].value_counts().to_dict()
        plot_histogram(data)





def step_4_():
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    for warehouse in df["Lager"].unique():
        temp_df = df[df["Lager"] == warehouse]
        data = []
        for week in temp_df["Week"].unique():
            a = temp_df[temp_df["Week"] == week]
            data.append(a["Weekday"].value_counts().to_dict())

        days = {WEEKDAYS[day]: [0] for day in range(1, 8)}
        for value in data:
            for day in range(1, 8):
                try:
                    days[WEEKDAYS[day]].append(value[day])
                except KeyError:
                    pass

        data = {}
        for key, value in days.items():
            data[key] = np.mean(value)
        plot_histogram(data)


def step_5_():
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    for warehouse in df["Lager"].unique():
        temp_df = df[df["Lager"] == warehouse]
        data = []
        for week in temp_df["Week"].unique():
            a = temp_df[temp_df["Week"] == week]
            data.append(a["Hour"].value_counts().to_dict())

        days = {day: [0] for day in range(0, 25)}
        for value in data:
            for day in range(0, 25):
                try:
                    days[day].append(value[day])
                except KeyError:
                    pass

        data = {}
        for key, value in days.items():
            data[key] = np.mean(value)
        plot_histogram(data)




def step_6():
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    data = []
    for week in df["Week"].unique():
        temp_df = df[df["Week"] == week]
        data.append(temp_df["Weekday"].value_counts().to_dict())

    a = {key: [] for key in range(1, 8)}
    for d in data:
        for key, value in d.items():
            try:
                a[key].append(value)
            except KeyError:
                pass
    di = {
        "gennemsnit": [],
        "max": [],
        "min": [],
    }
    for key, value in a.items():
        di["gennemsnit"].append(np.mean(value))
        di["max"].append(max(value))
        di["min"].append(min(value))
        
        
    for key, value in di.items():
        plt.plot(value, label=key)

    # Add labels and legend
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Plot of Lists in Dictionary")
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()
    #data = df["Weekday"].value_counts().to_dict()
    #plot_histogram(data, "Histogram over friveks af bestillin over datoer", "Frigivelsesdatoer", "frequns")



def step_7():
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[(df["Week"] <= 51) & (df["Weekday"] <= 5)]
    data = []
    for week in df["Week"].unique():
        temp_df = df[df["Week"] == week]
        data.append(temp_df["Hour"].value_counts().to_dict())
    

    a = {key: [] for key in range(0, 19)}
    for d in data:
        for key, value in d.items():
            try:
                a[key].append(value)
            except KeyError:
                pass
    di = {
        "gennemsnit": [],
        "max": [],
        "min": [],
    }
    for key, value in a.items():
        di["gennemsnit"].append(np.mean(value))
        di["max"].append(max(value))
        di["min"].append(min(value))

        
    for key, value in di.items():
        plt.plot(value, label=key)

    # Add labels and legend
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Plot of Lists in Dictionary")
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()
    #data = df["Weekday"].value_counts().to_dict()
    #plot_histogram(data, "Histogram over friveks af bestillin over datoer", "Frigivelsesdatoer", "frequns")


def step_8():
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[(df["Week"] <= 51) & (df["Weekday"] <= 5)]
    data = []
    for week in df["Week"].unique():
        temp_df = df[df["Week"] == week]
        data.append(temp_df["Hour"].value_counts().to_dict())
    

    a = {key: [0] for key in range(0, 23)}
    for d in data:
        for key, value in d.items():
            try:
                a[key].append(value)
            except KeyError:
                pass
    di = []
    for key, value in a.items():
        di.append(np.mean(value))
    
    a = [0 for i in range(0, 23)]
    for i in range(0, 23):
        if 6 <= i and i <= 14:
            a[i] += 35 * 6
        if 8 <= i and i <= 16:
            a[i] += 35 * 9
        if 15 <= i and i <= 23:
            a[i] += 35 * 2

    c = [0]
    d = []
    for b, bb in zip(di, a):
        if b - bb + c[-1] < 0:
            d.append(-1 * (b - bb + c[-1]))
            value = - c[-1]
        else:
            d.append(0)
            value = b - bb
        c.append(value + c[-1])
    c = c[1:]
    plt.plot(np.cumsum(di).tolist())
    plt.plot(np.cumsum(a).tolist())
    plt.plot(np.cumsum(d).tolist())
    plt.plot(c)
    
    # Add labels and legend
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Plot of Lists in Dictionary")
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()


def main():
    # step_1()
    # step_2()
    # step_3()
    # step_4()
    # step_5("Frigivelsesdato")
    # step_5("Lagerområde")
    # step_6()
    # step_7()
    step_8()

if __name__ == "__main__":
    main()
