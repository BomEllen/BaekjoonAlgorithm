A, B = map(int, input().split())
C = int(input())
x = (A*60+B+C)

if (x//60 <= 23):
    print (x//60, end = ' ')
    print (x%60, end = ' ')
else: 
    print ((x-1440)//60, end = ' ')
    print ((x-1440)%60, end = ' ')