H, M = map(int, input().split())
if H>0:
    a = int((H*60+M)-45)
    print (a//60, end=' ')   # 몫 = 시간
    print (a%60, end=' ')    # 나머지 = 분
else:
    b = int((H+1440+M)-45)
    print (b//60, end=' ')    
    print (b%60, end=' ')
