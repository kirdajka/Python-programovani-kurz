import json
import requests

nazev_subjektu = input("Zadej název subjektu, který chceš vyhledat: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = '{"obchodniJmeno": "'+ nazev_subjektu +'"}'
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)

if res.status_code == 200:
    response_data = res.json()
    pocet_nalezenych_subjektu = response_data['pocetCelkem']
    nalezene_subjekty = response_data['ekonomickeSubjekty']

    print(f"Nalezeno subjektů: {pocet_nalezenych_subjektu}")
    for subjekt in nalezene_subjekty:
        obchodni_jmeno = subjekt['obchodniJmeno']
        identifikacni_cislo = subjekt['ico']
        print(f"{obchodni_jmeno}, {identifikacni_cislo}")
else:
    print("Nepodařilo se získat data.")
