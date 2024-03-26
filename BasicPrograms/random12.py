import random
'''n=random.randbytes(1)
print(n)

print(random.randrange(8,10))

mylist=("Jadeja","Ashwin","Rahane","Shami","Dhoni","Virat")
mylist1=["Jadeja","Ashwin","Rahane","Shami","Dhoni","Virat"]
mylist2={"Jadeja","Ashwin","Rahane","Shami","Dhoni","Virat"}
print(random.choice(mylist))
print(random.shuffle(mylist1))'''
import string
S=10
ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=S))
s1=4
ran1=''.join(random.sample(string.digits,k=6))
print(ran)