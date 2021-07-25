
from sys import stdin

def isEmpty(s):
	return len(s)==0

def stockSpan(price, n) :
	
	if n==0:
		return 
	
	s=[]
	span=[]

	for i in range(len(price)):
		while not isEmpty(s) and price[s[-1]]<price[i]:
			s.pop()

		if isEmpty(s):
			span.append(i+1)

		else:
			span.append(i-s[-1])
		
		s.append(i)
	return span
 


'''-------------- Utility Functions --------------'''




def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
