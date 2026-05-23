import os
import random


def gen():
	os.makedirs("data",exist_ok=True)
	random.seed(7)
	for i in range(1,101):
		n=random.randint(100,10000)
		a=[]
		for _ in range(n):
			a.append(random.randint(-10000,10000))
		with open(f"data/in_{i:03}.txt","w",encoding="utf-8") as f:
			f.write(" ".join(map(str,a)))


if __name__=="__main__":
	gen()
