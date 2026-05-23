def ins(a,l,r):
	st=0
	for i in range(l+1,r+1):
		x=a[i]
		j=i-1
		st+=1
		while j>=l:
			st+=1
			if a[j]>x:
				a[j+1]=a[j]
				j-=1
				st+=1
			else:
				break
		a[j+1]=x
		st+=1
	return st


def mrg(a,l,m,r):
	st=0
	x=a[l:m+1]
	y=a[m+1:r+1]
	i=0
	j=0
	k=l
	while i<len(x) and j<len(y):
		st+=1
		if x[i]<=y[j]:
			a[k]=x[i]
			i+=1
		else:
			a[k]=y[j]
			j+=1
		k+=1
		st+=1
	while i<len(x):
		a[k]=x[i]
		i+=1
		k+=1
		st+=1
	while j<len(y):
		a[k]=y[j]
		j+=1
		k+=1
		st+=1
	return st


def timsort(a):
	n=len(a)
	run=32
	st=0
	for l in range(0,n,run):
		r=min(l+run-1,n-1)
		st+=ins(a,l,r)
	sz=run
	while sz<n:
		for l in range(0,n,sz*2):
			m=min(n-1,l+sz-1)
			r=min(l+sz*2-1,n-1)
			if m<r:
				st+=mrg(a,l,m,r)
		sz*=2
	return st
