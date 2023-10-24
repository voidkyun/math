def heap(n):
	"""
	heapのアルゴリズムでSnを生成
	"""
	A=[i for i in range(n)]
	S=[]
	def swap(a,b):
		temp=A[b]
		A[b]=A[a]
		A[a]=temp
	def generate(m):
		if m==1:
			_A=A.copy()
			S.append(_A)
		else:
			for i in range(m):
				generate(m-1)
				if m%2==0:
					swap(i,m-1)
				else:
					swap(0,m-1)
	generate(n)
	return(S)

def sgn(l):
	count=0
	for c,i in enumerate(l):
		for j in l[:c]:
			if j>i:
				count+=1
	return((-1)**count)

def det(A):
	n=len(A[0])
	Sn=heap(n)
	determinant=0
	for s in Sn:
		temp=sgn(s)
		for i in range(n):
			temp=temp*A[i][s[i]]
		determinant+=temp
	return(determinant)