# i use numpy but floating point problem still remain

import math
import numpy as np

def normalize(input_vector):
	s = math.sqrt(sum(map(lambda x:x*x,input_vector)))
	return map(lambda x:x/s,input_vector)


def shadow(v1, v2):
    return map((lambda x : x * np.dot(v2, v1) / np.dot(v1, v1)), v1)

def gram_schmidt(X):
    out = []
    for i in range(len(X)):
        temp_vec = X[i]
        for base in out :
            proj_vec = shadow(base, X[i])
            temp_vec = map(lambda x, y : x - y, temp_vec, proj_vec)
        if not temp_vec == [0]*n:
        	out.append(normalize(temp_vec))
    return out

if __name__ == '__main__':
	lines = [line.strip() for line in open("input4", 'r')]
	k = int(lines[0])
	n = int(lines[1])
	vectorls = []
	for x in range(k):
		tlist =[int(x) for x in lines[2+x].split(" ")]
		vectorls.append(tlist)
	print gram_schmidt(vectorls)
	