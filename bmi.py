waga= int(input('prosze wpisać wagę '))
wzrost= float(input('proszę wpisać wzrost w metrach '))
plec= input('podaj płeć M/F ')
bmi= waga/wzrost**2
if plec=='F':
	if bmi<=19:
		print ('Niedowaga')
	elif bmi<=22:
		print ('Waga prawidłowa')
	else:
		print ('Nadwaga')
else:
	if bmi<=20:
		print ('Niedowaga')
	elif bmi<=25:
		print ('Waga prawidłowa')
	else:
		print ('Nadwaga')
print ('%s %.2f ' % ('Twoje bmi wynosi ',bmi))