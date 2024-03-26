'''
Example1
n = int(input("Enter a number"))
if n == 0:
    print("Number id Invalid")
else:
    for i in range(n, n + 1):
        val = n * (n * 1)
        print(val)


Example2
x = 0
n = int(input("Enter the no of stars"))
for i in range(1,n+1):
    str=''.join('*')
    print(str)
# str1 = "thisismycountryindia"
for i in str:
    x = x - 1
    print(str[0:x])
for j in str:
    x = x + 1
    print(str[0:x])'''
# Example
a1 = 1045
a2 = "101000"
a3 = int(format(int(a2, 3), "d"))
print(a3)
