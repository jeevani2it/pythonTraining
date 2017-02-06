#First Program
print('Execution started')

#variable assigning
tax = 12.5 / 100
price = 100.50
#variable calculation
data = price * tax
print(data)

hello = "This is a rather long string containing\n\
several lines of text just as you would do in C.\n\
    Note that whitespace at the beginning of the line is\
 significant."

print(hello)

word = 'Help' + 'A'
print(word)
print('<' + word*5 + '>')
textChar = 'helloDude'
print(textChar[3])
print(textChar[:3])
print(textChar[3:])


def firstFunction():
	print('inside fibonacci function')
	countVal=0
	a=0
	b=1
	print(b)
	while countVal < 10: 
		c = a+b
		print(c)
		a=b
		b=c
		countVal = countVal+1

firstFunction()

x = 9

if x<4:
	print(x)
else:
	print('ssssssss')

def functionWithParams(param1, param2='Hello'):
	print(param1 +'. '+  param2)

functionWithParams('Hi')

a = [66, 333, 1, 1234]
a.append(5)
print(a)

a.remove(5)
print(a)

a.insert(1,5)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

b = {'a': 66, 'b': 333, 'c': 1, 'd': 1234}
print(b)