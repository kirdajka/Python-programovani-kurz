import requests
import json

ico = input("Zadejte IČO subjektu: ")

url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"

response = requests.get(url)

data = response.json()
with open("data_zapis.json", "w", encoding="utf-8") as soubor:
    json.dump(data, soubor, indent=4)  

with open('data_zapis.json', encoding='utf-8') as soubor:
    data = json.load(soubor)

print(data["obchodniJmeno"])
print(data["sidlo"]["textovaAdresa"])



