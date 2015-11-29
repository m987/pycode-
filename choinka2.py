a=int(input('podaj wielkość choinki '))
def choinka (x):
	for b in range (1, x+1, 2):
		print ((b * '*').center(a))
for i in range (3, a+1,2):
	choinka (a)

# a=int(input('podaj wielkość choinki '))
# for b in range (1, a+1, 2):
	 # print ((b * '*').center(a))