#!/usr/bin/python
import matrix_module as mm

obj = mm.Matrix()

matrix1 = []
matrix2 =[]

print 'Give the elements of the 1st matrix'

for i in range(4):
	j = int(raw_input('%d element : ' %i))
	matrix1.append(j)
	
print 'Give the elements of the 2nd matrix'

for i in range(4):
	j = int(raw_input('%d element : ' %i))
	matrix2.append(j)

print matrix1
print matrix2

operation = int(raw_input('Choose 1 for "add" or 2 for "product" : '))

if operation == 1:
	print 'You chose addition'
	matrix3 = obj.addition(matrix1 , matrix2)
	print matrix3
