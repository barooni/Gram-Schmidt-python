import math
import numpy as np

def compaire(v1, v2):
	for i in range(len(v1)):
		if(abs(v1[i]-v2[i])>10**(-4)):
			return True
	return False

def normalize(input_vector):
	s = math.sqrt(sum(map(lambda x:x*x,input_vector)))
	return map(lambda x:x/s,input_vector)


def shadow(v1, v2):
    return map((lambda x : x * np.dot(v2, v1) / np.dot(v1, v1)), v1)

def gram_schmidt(X):
    out = []
    for i in range(len(X)):
        temp_vec = list(X[i])
        for base in out :
            proj_vec = shadow(base, X[i])
            temp_vec = map(lambda x, y : x - y, temp_vec, proj_vec)
        if compaire(temp_vec, [0]*n):
        	out.append(normalize(temp_vec))
    return out

if __name__ == '__main__':
	# lines = [line.strip() for line in open("input2_tested_work", 'r')]
	lines = [line.strip() for line in open("input2_floating_point_problem", 'r')]
	# lines = [line.strip() for line in open("input4_floating_point_problem", 'r')]
	k = int(lines[0])
	n = int(lines[1])
	vectorls = []
	for x in range(k):
		tlist =[int(x) for x in lines[2+x].split(" ")]
		vectorls.append(tlist)
	basis = gram_schmidt(vectorls)
	print len(basis)
	print basis
	for i in range(k):
		coff = []
		for j in range(len(basis)):
			coff.append(np.dot(vectorls[i], basis[j]))
		print coff
	