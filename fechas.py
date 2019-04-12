from datetime import datetime, date, time


#Fecha y hora completos
diayhora = datetime.now()
print(diayhora)

#Fecha
hoy = date.today()
print(hoy)

print(hoy.day)
print(hoy.month)
print(hoy.year)

#Dia de la semana
diaDeLaSemana = hoy.weekday()
print(diaDeLaSemana)
#0 Lunes - 6 Domingo

inputDate = input("Enter the date in format 'dd/mm/yyyy' : ")

day,month,year = inputDate.split('/')


isValidDate = True

if len(year) == 4 and len(month) == 2 and len(day) == 2:
    fecha = date(int(year),int(month),int(day))
    print("La fecha es:",fecha)
else:
    isValidDate = False



if(isValidDate) :
    print ("Fecha valida")
else :
    print ("Fecha invalida")
