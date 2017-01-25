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

def firstFunction():
	print('inside function')

firstFunction()

x = 9

if x<4:
	print(x)

