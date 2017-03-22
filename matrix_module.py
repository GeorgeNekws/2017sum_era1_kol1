#!/usr/bin/python

class Matrix(object):

	
	def addition(self,m1,m2):
		m3 = []					#the result matrix
		for i in range(4):
			j = m1[i] + m2[i]
			m3.append(j)
		return m3
		
