import math
from decimal import Decimal,getcontext

getcontext().prec = 5

def innerproduct(vectorA,vectorB):
	tempv = [i*j for i,j in zip(vectorA,vectorB)]
	return sum(tempv)

def normalize(input_vector):
	s = math.sqrt(sum(map(lambda x:x*x,input_vector)))
	return map(lambda x:x/s,input_vector)


if __name__ == '__main__':
	lines = [line.strip() for line in open("input2_tested_work", 'r')]
	k = int(lines[0])
	n = int(lines[1])
	vectorls = []
	for x in range(k):
		tlist =[int(x) for x in lines[2+x].split(" ")]
		vectorls.append(tlist)
	
	m=0
	basis = []
	for vector in vectorls:
		# print "##########################################"
		# print "iteration on ",vector
		# print "basis:",basis
		# print ".........................................."
		sumonbasis = [0]*n
		for base in basis:
			inp = innerproduct(vector,base)
			# print "inp",inp
			shadow_on_base = [x * inp for x in base]
			# print "shadow_on_base:",shadow_on_base
			sumonbasis = [x + y for x, y in zip(sumonbasis, shadow_on_base)]
			# print "sumonbasis (in):",sumonbasis
		# print ".........................................."
		# print "sumonbasis :",sumonbasis
		vector2 = [round(x - y,6) for x, y in zip(vector, sumonbasis)]
		# print "vector2 :",vector2
		# print "normalize(vector2) :",normalize(vector2)
		if not vector2 == [0]*n:
			m = m + 1
			basis.append(normalize(vector2))
		
	print m
	print basis
	for i in range(k):
		coff = []
		for j in range(m):
			coff.append(innerproduct(vectorls[i],basis[j]))
		print coff
