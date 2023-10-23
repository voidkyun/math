def heap(n):
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

heap(3)
print(heap(3))	#[[0, 1, 2], [1, 0, 2], [2, 0, 1], [0, 2, 1], [1, 2, 0], [2, 1, 0]]