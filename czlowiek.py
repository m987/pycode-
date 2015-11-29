class czlowiek:
	wzrost=0
	waga=0

	def __init__(self, imie, waga, wzrost):
		self.imie = imie
		self.waga = waga
		self.wzrost = wzrost

	def jesc(self):
		self.waga=self.waga+1

	def wisiec(self):
		self.wzrost=self.wzrost+1

	def __str__(self):
		return "to jest %s o wadze %d i wzroscie %d" % (self.imie, self.waga, self.wzrost)

imiona = ['aga', 'ala', 'tomek']
ludzie =  {}

for i in imiona:
	ludzie[i] = czlowiek(
		i,
		int(input('podaj ilość jedzenia w kg dla %s:' % i)),
		int(input('podaj ilość godz. dla %s:' % i)),
		)

 for i in imiona:
	# ludzie[i] = czlowiek(
		# # i,
		# int(input('podaj wage dla %s:' % i)),
		# int(input('podaj wzrost dla %s:' % i)),
	# )

ludzie['aga'].waga=50

for i in ludzie:
	print(ludzie[i])