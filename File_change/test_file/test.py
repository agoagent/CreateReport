a = ['1','2','3','4','5','6']
b = {}
for i in range(0 ,len(a), 2):
    b[a[i]] = a[i+1]

print(b)