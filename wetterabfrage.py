import requests

Stadt = input("Stadt einegeben: ")

#Koordinaten holen
url = f"https://geocoding-api.open-meteo.com/v1/search?name={Stadt}&count=1&language=de"
antwort = requests.get(url)
daten = antwort.json()

#koordinaten aus den Daten ziehen
ergebnis = daten["results"][0]
lat = ergebnis["latitude"]
lon = ergebnis["longitude"]
stadtname = ergebnis["name"]

print(f"Stadt gefunden: {stadtname} ({lat}, {lon})")

#Wetter abrufen
wetter_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
wetter_antwort = requests.get(wetter_url)
wetter_daten = wetter_antwort.json()

#Wetter extrahieren
aktuell = wetter_daten["current_weather"]
temperatur = aktuell["temperature"]
windgeschwindigkeit = aktuell["windspeed"]
weathercode = aktuell["weathercode"]

#Wettercode in Text umwandeln
wettercodes = {
    0: "klar",
    1: "überwiegend klar",
    2: "teilweise bewölkt",
    3: "Bewölkt",
    45: "Nebel",
    61: "Leichter Regen",
    63: "Regen",
    65: "starker Regen",
    71: "leichter Schnee",
    80: "Regenschauer",
    95: "Gewitter",
    }

wetterbeschreibung = wettercodes.get(weathercode, "unbekannt")

#Ausgabe
print(f"\n--- Wetter in {stadtname} ---")
print(f"Zustand:  {wetterbeschreibung}")
print(f"Temperatur: {temperatur} °C")
print(f"Windgeschindwigkeit: {windgeschwindigkeit} km/h")
