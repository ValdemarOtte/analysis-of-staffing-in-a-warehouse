### Imports
# Standard library
from pathlib import Path
import csv
from datetime import datetime
from collections import Counter

# Third-party libraries
import matplotlib.pyplot as plt
import pandas as pd

# Local files


DATA_PATH: Path = Path("data\\datasample.csv")
# Det ses i `datasample.csv` at der er følgende kolumner
# Year                  : År
# Month                 : Måned
# Week                  : Ugenummer
# Weekday               : Ugesdag (0 = mandag, ..., 6 = søndag)
# Frigivelsesdato       : Dato for modtagelse af bestillingen. Format (DD-MM-YYYY)
# Lager                 : Hvilket lager varen findes i
# Lagerområde           : Hvilket lagerområde varen findes i
# KO/DO                 :
# Hour                  : Hvilket tidspunkt bestilling er modtaget
# Afgangstid            :
# Antal_linjer          :
# Teoretisk_bemandning  :




def his(rows, index):
    pass




def count_weekdays(df):
    df = df.value_counts()
        # Plot histogram for the 'values' column
    df.plot.hist()

    # Add labels and title
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Values')

    # Show the plot
    plt.show() 

def main():
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(DATA_PATH, delimiter=";")
    df["Frigivelsesdato"] =  pd.to_datetime(df["Frigivelsesdato"], format="%d-%m-%Y")
    a = df["Frigivelsesdato"].to_list()
    data = Counter(a)


    # Vis resultatet
    # Ekstraher nøgler (kategorier) og værdier (hyppigheder)
    categories = list(data.keys())
    values = list(data.values())

    # Lav et barplot (histogram for diskrete data)
    plt.bar(categories, values, color='skyblue', edgecolor='black')

    # Tilføj titler og labels
    plt.title('Histogram af dictionary')
    plt.xlabel('Dato')
    plt.ylabel('Count')
    plt.xticks(rotation=45)  # Rotér x-aksens labels for bedre læsbarhed
    plt.tight_layout()

    # Vis plot
    plt.show()
    return
    # Display the first few rows
    #print(df.head())
    #count_weekdays(df["Frigivelsesdato"])
    
    # Opret DataFrame
    data = {"d": ["11-11-2024", "12-11-2024", "14-11-2024", "17-11-2024"], "count": [1, 0, 4, 2]}
    df = pd.DataFrame(data)
    df['d'] = pd.to_datetime(df['d'], format='%d-%m-%Y')
    
    df.set_index('d', inplace=True)

    # Konverter 'd' kolonnen til datetime

    # Plot histogram
    df.plot(kind='bar', width=1,  y='count', legend=False)

    # Tilføj titler og labels
    plt.title('Histogram over count pr. dato')
    plt.xlabel('Dato')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Vis plot
    plt.show()



if __name__ == "__main__":
    main()
