from datetime import datetime, timedelta

print(datetime.now())



apollo_pristani = datetime.strptime("21. 7. 1969, 18:54", "%d. %m. %Y, %H:%M")



satelit_solar_orbitel = datetime(2020,2,10,5,3)
satelit_solar_orbitel.weekday()

apolloStart = datetime(1969, 7, 16, 14, 32)
apolloStart = apolloStart.strftime("%m/%d/%Y")
print (apolloStart)


satelit_solar_orbitel = datetime(2020,2,10,5,3)
print(satelit_solar_orbitel.weekday())
kdy = datetime.now() - satelit_solar_orbitel 
print(kdy)

objednavka = datetime.strptime("13. 11. 2020, 19:47", "%d. %m. %Y, %H:%M")
trvani = timedelta(days=0,hours=1,minutes=1,seconds=5)
dodani = objednavka + trvani
print(dodani)
