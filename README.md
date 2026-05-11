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
