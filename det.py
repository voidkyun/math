import heap

def sgn(l):
	count=0
	for c,i in enumerate(l):
		for j in l[:c]:
			if j>i:
				count+=1
	return((-1)**count)

def det(A):
	n=len(A[0])
	Sn=heap.heap(n)
	determinant=0
	for s in Sn:
		temp=sgn(s)
		for i in range(n):
			temp=temp*A[i][s[i]]
		determinant+=temp
	return(determinant)