### Imports
# Standard library
from pathlib import Path

# Third-party libraries
import numpy as np
import pandas as pd

# Local files
from src.plots import plot_histogram, plot_lineplot


DATA_PATH: Path = Path("data\\datasample.csv")
COLOR_SCHEME: list[str] = [
    "#4169E1",
    "#bb342f",
    "#218380",
    "#ead94c",
]

  
def convert_to_float(string: str) -> float:
    """
    Convert a string to a float.
    
    e.x. given the strin `"0,282"`, then `convert_to_float` will return the float `0.282`.
    
    Parameters
    ----------
    string : str
        The string which will be converted to a float
        
    Returns
    -------
    float
        The converted string
    
    Raises
    ------
    ValueError
        If the input string cannot be converted to a float.
    """
    try:
        return float(string.replace(",", "."))
    except ValueError:
        raise ValueError(f"Could not convert '{string}' to float.")


def step_1() -> None:
    """
    Load data and plot frequency of `Frigivelsesdato` as a histogram.
    """
    df = pd.read_csv(DATA_PATH, delimiter=";")
    
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    data = df["Frigivelsesdato"].value_counts().to_dict()
    plot_histogram(data, "Histogram over frigivelser af bestillinger over datoer", "Frigivelsesdatoer", "Frekvens")


def step_2() -> None:
    """
    Load data and plot frequency of `Frigivelsesdato` as a histogram, excluding weeks 52 and 53.
    """
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    
    data = df["Frigivelsesdato"].value_counts().to_dict()
    plot_histogram(data, "Histogram over frigivelser af bestillinger over datoer (minus uge 52/53)", "Frigivelsesdatoer", "Frekvens")
    

def step_3() -> None:
    """
    Calculate the smallest and greatest value of `Antal_linjer`, as well as its mean, variance, and median.
    """
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    
    min_val = df["Antal_linjer"].min()
    max_val = df["Antal_linjer"].max()
    mean_val = df["Antal_linjer"].mean()
    var_val = df["Antal_linjer"].var()
    median_val = df["Antal_linjer"].median()

    print(f"Mindste værdi   : {min_val}")
    print(f"Største værdi   : {max_val}")
    print(f"mean      : {mean_val:.2f}")
    print(f"Varians         : {var_val:.2f}")
    print(f"Median          : {median_val:.2f}")


def step_4():
    """
    Plot and view the relationship between `Antal_linjer` and `Teoretisk_bemandning`.
    """
    df = pd.read_csv(DATA_PATH, delimiter=";")
    data = dict(zip(df["Antal_linjer"], df["Teoretisk_bemandning"]))

    for key, value in data.items():
        data[key] = convert_to_float(value)
    plot_lineplot_(data, "Sammenhæng mellem \"teoretisk bemandning\" og \"Antal linjer\"", "Teoretisk bemandning", "Antal linjer",)



def step_5(column: str, title: str) -> None:
    """
    Load and plot data for every unique warehouse in the dataset.
    
    This function is called twice:
    - Once with `column="Frigivelsesdato"`
    - Once with `column="Lagerområde"`
    
    Parameters
    ----------
    column : str
        The column name in the dataset to analyze.
    title : str
        The title for the histogram.
    """
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")

    for warehouse in df["Lager"].unique():
        temp_df = df[df["Lager"] == warehouse]
        data = temp_df[column].value_counts().to_dict()
        plot_histogram(data, f"{title} for {warehouse}", column, "Frekvens")


def find_values(df, column) -> tuple[dict[int, list[int]], int, int]:
    elements = []
    values = df["Week"].unique()
    for week in values:
        temp_df = df[df["Week"] == week]
        elements.append(temp_df[column].value_counts().to_dict())
    return elements


def func(elements):
    keys = [key for element in elements for key in element.keys()]
    min_val = min(keys)
    max_val = max(keys)
    a = {key: [] for key in range(min_val, max_val+1)}
    for element in elements:
        for key, value in element.items():
            try:
                a[key].append(value)
            except KeyError:
                pass
    return a

def create_data_for_mean_min_max(a) -> dict[str, list[int | float]]:
    data = {
        "mean": [],
        "max": [],
        "min": [],
    }
    for value in a.values():
        data["mean"].append(np.mean(value))
        data["max"].append(max(value))
        data["min"].append(min(value))
    return data


def step_6() -> None:
    
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[df["Week"] <= 51]
    
    elements = find_values(df, "Weekday")
    a = func(elements)
    data = create_data_for_mean_min_max(a)
    plot_lineplot(data, "Graf over frekvens af bestillinger over ugedage", "Ugedage", "Frekvens")


def step_7() -> None:
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[(df["Week"] <= 51) & (df["Weekday"] <= 5)]
    
    elements = find_values(df, "Hour")
    a = func(elements)
    data = create_data_for_mean_min_max(a)
    plot_lineplot(data, "Graf over frekvens af bestillinger over timer", "Tid", "Frekvens")



def find_packages_left_and_wasted_time(mean, schedule):
    packages_left = [0]
    wasted_time = []
    for x, y in zip(mean, schedule):
        if x - y + packages_left[-1] < 0:
            wasted_time.append(-1 * (x - y + packages_left[-1]))
            value = - packages_left[-1]
        else:
            wasted_time.append(0)
            value = x - y
        packages_left.append(value + packages_left[-1])
    packages_left = packages_left[1:]
    return packages_left, wasted_time


def create_schedule(work_schedules: list[dict[str, int]]) -> list[int]:
    schedule = [0 for _ in range(0, 24)]
    for i in range(0, 23):
        for work_schedule in work_schedules:
            if work_schedule["start"] <= i and i <= work_schedule["end"]:
                schedule[i] += 35 * work_schedule["amount"]                     # 35 is the number of lines each worker can do in a hour
    return schedule


def step_8(work_schedules: list[dict[str, int]]) -> None:
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df = df[(df["Week"] <= 51) & (df["Weekday"] <= 5)]
        
    elements = find_values(df, "Hour")
    a = func(elements)
    # Because the median size of a package 
    scalar = 2
    a = {key: [value * scalar for value in values] for key, values in a.items()}
    
    mean = create_data_for_mean_min_max(a)["mean"]
    # Extent the mean to be 24 hours
    mean.extend([0 for _ in range(0, 24 - len(mean))])

    schedule = create_schedule(work_schedules)
    packages_left, wasted_time = find_packages_left_and_wasted_time(mean, schedule)

    data = {
        "Mean of confirmed order": np.cumsum(mean).tolist(),
        "Schedule": np.cumsum(schedule).tolist(),
        "Wasted time": np.cumsum(wasted_time).tolist(),
        "Packages left": packages_left
    }
    plot_lineplot(data, "Graf over forventet pakker, pakket pakker af medarbejde, spildtid og pakker tilbage", "Tid", "Antal linjer")


def main():
    # Brugt under "2.2) Hvornår bliver en bestilling lavet?"
    #step_1()
    #step_2()
    
    # Brugt under "2.3) Størrelsen på en bestilling"
    #step_3()
    
    # Brugt under "2.4) Hvor hurtigt pakker en medarbejder en bestilling?"
    #step_4()
    
    # Brugt under "2.5) I hvilket lager og lageområde findes bestillingen i?"
    #step_5("Frigivelsesdato", "Histogram over frigivelser af bestillinger over datoer (minus uge 52/53)")
    #step_5("Lagerområde", "Lagerområder")

    # Brugt under "2.6) Observeret fordeling på dagsbaseret"
    #step_6()
    
    # Brugt under "2.7) Observeret fordeling på timebaseret"
    #step_7()
    
    # Brugt under "2.8) Time"
    work_schedules = [
        {
            "start": 6,
            "end": 14,
            "amount": 12
        },
        {
            "start": 8,
            "end": 16,
            "amount": 20
        },
        {
            "start": 15,
            "end": 23,
            "amount": 8
        },
    ]
    step_8(work_schedules)


if __name__ == "__main__":
    main()
