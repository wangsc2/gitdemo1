Ist=int(input())
num=int (input())
sq=[]
for i in range(1,Ist+1):
	sq.append(i)
while len(sq)>1:
	for i in range(num-1):
		sq.append(sq.pop(0))
		sq.pop(0)
print(sq.pop(0))
for i in range(len(sq)-1):
	print(sq(i))
print(len(sq))

		
