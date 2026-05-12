# 


### Case
- Trin 1)
   - Lav histogram
   - Fjern helligdage
- Trin 2)
   - Kig på lager
   - Kig på lagerområder
   - Plot det
- Trin 3)
   - Opdel i time baset og uge baset
   - Find middelværdi og variance
   - Fordeling
   - Plot det
   - Er dae o time udfæniede af laerområde?
- Trin 4)
   - Kan vi lave en timeplan herpå?

# Problemstilling

# Analyse
## Hvordan ser dataet ud?
| Kolonne               | Beskrivelse                                                |
| --------------------- | ---------------------------------------------------------- |
| Year                  | År                                                         |
| Month                 | Måned                                                      |
| Week                  | Ugenummer                                                  |
| Weekday               | Ugesdag (1 = mandag, ..., 7 = søndag)                      |
| Frigivelsesdato       | Dato for modtagelse af bestillingen. Format (DD-MM-YYYY)   |
| Lager                 | Hvilket lager varen findes i                               |
| Lagerområde           | Hvilket lagerområde varen findes i                         |
| KO/DO                 | Hvilken slas bestilling det er                             |
| Hour                  | Hvilket tidspunkt bestilling er modtaget                   |
| Afgangstid            | vornår bestillingen forlader lageret                       |
| Antal_linjer          | Hvor mange varer der er i en given bestilling              |
| Teoretisk_bemandning  | Den teorietiske tid som medarbejderen bruger på bestilling |

## Hvornår bliver en bestilling lavet?
Billede af histogram 1

Billede af histogram 2


## I hvilket lager og lageområde findes bestillingen i?

Billede af histogram 1 for lager 1 og lager 2

Billede af histogram 3 for lagerområder for lager 1

Billede af histogram 4 for lagerområder for lager 2



### vor urti pakker medarbejdede?


Dermed ses det, at en medarbejder teoretisk vil kunne pakke 35 enstande pr. time.




# Analyse
## Hvordan ser dataet ud?
| Kolonne               | Beskrivelse                                                |
| --------------------- | ---------------------------------------------------------- |
| Year                  | År                                                         |
| Month                 | Måned                                                      |
| Week                  | Ugenummer                                                  |
| Weekday               | Ugesdag (1 = mandag, ..., 7 = søndag)                      |
| Frigivelsesdato       | Dato for modtagelse af bestillingen. Format (DD-MM-YYYY)   |
| Lager                 | Hvilket lager varen findes i                               |
| Lagerområde           | Hvilket lagerområde varen findes i                         |
| KO/DO                 | Hvilken slas bestilling det er                             |
| Hour                  | Hvilket tidspunkt bestilling er modtaget                   |
| Afgangstid            | vornår bestillingen forlader lageret                       |
| Antal_linjer          | Hvor mange genstande der er i en given bestilling          |
| Teoretisk_bemandning  | Den teorietiske tid som medarbejderen bruger på bestilling |


## Hvornår bliver en bestilling lavet?
Først plotter vi et histogram over hvilke datoer bestillingerne bliver lavet på.
Herunder på fig. 1 ses det tydeligt, at der fremgår et fast mønster for hver uge.
Der bliver lavet flest bestillinger i hverdagene, mens i weekenenden er der fåtalige. 

Billede af histogram 1

Vi bemærker også, at vi har data fra uge 52 og uge 53.
Vi vælger at fratage disse to uge fra datasættet, da det er ferie uger og dermed vil ikke kunne bidrage til en normal ugeplan.

Billede af histogram 2


## Størrelsen på en bestilling
Størrelsen på en bestilling er bestemt af variablen `Antal_linjer`.

| Test          | Værdi |
| ------------- | ----- |
| Mindst værdi  |     1 | 
| Største værdi |       | 
| Gennemsnit    |       | 
| Variance      |       |
| Median        |       |

[FIG: Billede af histogram 2 med antal_linje]


## Hvor hurtigt pakker en medarbejder en bestilling?
Det er en variablet variabel, da det det 

Vi ser dog i datasættet, at der er et lineært sammenhæng mellem `Antal_linjer` og `Teoretisk_bemandning`.

[FIG: Det lineære sammenhæng mellem `Antal_linjer` og `Teoretisk_bemandning`]

Dermed ses det, at en medarbejder teoretisk vil kunne pakke 35 genstande pr. time.


## I hvilket lager og lageområde findes bestillingen i?

Billede af histogram 1 for lager 1 og lager 2

### Lagerområder
#### Lager 1
Billede af histogram 3 for lagerområder for lager 1

#### Lager 2
Billede af histogram 4 for lagerområder for lager 2


For at holde analysen mindre kompleksi er der ikke blevet set på en time-baseret for hver ugedag.
Se konklusion for en uddybende diskontion omkring valget.


## Fordeling på dags-baseret og time-basseret
### dags-baseret


### time-basseret


#### Hverdage

#### Weekender



For at holde analysen mindre kompleksi er der ikke blevet set på en time-baseret for hver ugedag.
Se konklusion for en uddybende diskontion omkring valget.


## Timeplan
Vi antager at medarbejderne kan fordeles på
| Vagthold     | Tidsrum       |
| ------------ | ------------- |
| Morgenholdet | 06:00 - 14:00 |
| Dagsholdet   | 08:00 - 16:00 |
| Aftensholdet | 15:00 - 23:00 |


I denne analyse antager vi, at medarbejder ikke kan deles mellem lagerne, men derimod godt imellem lagerområder. 
Vi antager ydligere, at medarbejderne tidlist vil møde ind kl. 06:00 og senest tage fri kl 23:00. Derudover, så må der ikke være en vagt på over 8 timer og mindre end 3 timer.
Som nævnt i problemstillingen, så har virksomheden en frist kl 18:00 med at alle bestillingen før det, skal være pakket og sent afsted senest kl. 23:00.




###



## Konklusion


Hvad kunne ellers har været set på?
- En tidsplan for hvert lager og/eller lagerområde. 
- Da virksomheden har en polik med at alle bestillingen lavet før 18:00 den opgældende dag skal afsted samme dag, så kan man overveje hvorvidt man skal have medarbejde på arbejde mellem 18:00 og 23:00. Det vil sige, at alle bestillinger lavet mellem 18:00 og 23:00 først bliver pakket næste dag.
- Har en vagtplan for hver hverdag, idet der er flest bestillingerne mandag og frest fredag.












# Ændre ingenting
titles_1 = [
    "a #1",
    "a #2",
    "a #3",
]

# Ret forkert nummer
titles_2 = [
    "a #1",
    "a #3",
    "a #4",
]

# Ret default titel væk
titles_3 = [
    "a #1",
    "a #2",
    "abc",
]

# Tilføj nummer til titel uden nummer
titles_4 = [
    "a #1",
    "a #2",
    "bla bla",
]

# Ændre ingenting
titles_5 = [
    "a #1",
    "a #2",
    "bla bla - a #3",
]

#
titles_6 = [
    "a #1",
    "dad #1",
    "dad #2",
]

# Ændre ingenting
titles_7 = [
    "a #1",
    "dad - a #2",
    "dad - a #3",
]

# 
titles_7 = [
    "a #1",
    "a #2",
    "dad - a #4",
]




DEFAULT_TITLES: dict[str, list[str]] = {
    "a": ["abc"]
}


def create_new_title(current_title: str, number: int, activity: str) -> str:
    """
    Create a new title for a given activit with correct numbering.

    Parameters
    ----------
    current_title : str
        The current title for the activity.
    number : int
        The numbering of the activity.
    activity : str
        Type of activity.
    
    Returns
    -------
    str
        The new title for the activity with correct numbering.
    
    Raises
    ------
    ValueError
        If `activity` is not in DEFAULT_TITLES.
    """
    # Case 1: 
    if not current_title:
        return f"{activity} #{number}"
    
    current_title = current_title.strip()

    if activity not in DEFAULT_TITLES:
        raise ValueError(f"Unknown activity: {activity}")
    
    # Case 2:
    if current_title in DEFAULT_TITLES[activity]:
        return f"{activity} #{number}"
    # Case 3:
    if f"{activity} #{number}" in current_title:
        return current_title
    # Case 4:
    if f"{activity} #" in current_title:
        return f"{activity} #{number}"
    # Case 5:
    if "#" in current_title:
        current_title = current_title.split(" #")[0]
    
    return f"{current_title} - {activity} #{number}"


def update_title(title, new_title):
    print(f"{title:<10} -> {new_title}")


def main():
    titles_ = [titles_1, titles_2, titles_3, titles_4, titles_5, titles_6, titles_7]
    for titles in titles_:
        for i, title in enumerate(titles, start=1):
            new_title = create_new_title(title, i, "a")
            if title == new_title:
                continue
            update_title(title, new_title)
        print("\n")



if __name__ == "__main__":
    main()
