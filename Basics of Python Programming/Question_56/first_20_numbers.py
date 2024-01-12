n = 0
count = 0
list_even = []
while(count != 20):
    if(n%2 == 0):
        list_even.append(n)
        count = count + 1
    n=n+1
c = 0
for i in range(len(list_even)-1,-1,-1):
    print(list_even[i],end=' ')

