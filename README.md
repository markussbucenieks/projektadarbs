# Sludinājumu Monitorēšanas Projekts

## Projekta Uzdevums

Šis projekts ir izstrādāts sludinājumu monitorēšanai vietnē SS.LV. Tā galvenais uzdevums ir automātiski iegūt un saglabāt sludinājumu saites, kas atbilst noteiktiem filtriem. 
Tā kā uzdevums bija automatizēt kaut ko no ikdienas, tad ar šī koda palīdzību es monitorēju SS.LV vietnē automašīnu sludinājumus katras 3 stundas pēc manis noteiktajiem kritērijem, kurus nepieciešamības pēc kodā arī elementāri samainīt.

## Python Bibliotēkas

Projekta izstrādes laikā tiek izmantotas šādas Python bibliotēkas:

- **Selenium**: Tiek izmantots automātiskai pārlūka vadīšanai un sludinājumu lapas pārlūkošanai.
- **time**: Tiek izmantots laika aizturei un ciklu kontrolei.

## Programmatūras Izstrādes Metodes

1. Pirms darbības sākuma, jāinstalē nepieciešamās bibliotēkas, izmantojot `pip install -r requirements.txt`.

2. Projekta izpildei jānodrošina, ka ir instalēts Google Chrome un atbilstošā versija `chromedriver`. 

3. Darbības laikā programma:

    - Atver vietni "https://www.ss.lv/" un iestata filtra kritērijus.
    - Automātiski noklikšķina uz pogas "Meklēt".
    - Iegūst visus sludinājumu URL, kuri atbilst filtra kritērijiem un saglabā tos text failā.
    - Katras 3h kods salīdzina jauno sludinājumu URL ar iepriekšējo ciklu iegūtajiem URL.
    - Ja pēdējā ciklā parādās kādi jauni URL tad tos attiecīgi saglabā text failā.
