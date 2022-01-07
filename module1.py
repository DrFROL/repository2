f = open('Perepis.txt', 'r')
numb = int(input())
numb1 = int(input())
c = 0
for i in f:
    a = i.split()
    b = a[3].split('.')
    print(a[0])
    if int(b[2]) < 1978:
        c += 1
    if int(b[2]) > numb and int(b[2]) < numb1:
        print(a)
print(c)




