a=int(input())

def hanou(a,fr,bet,to):
    if a==1:
        print(fr,to)#1개면 목적지 1->3
    else:
        hanou(a-1,fr,to,bet)# n-1개를 중간으로 옮기기 1->2
        print(fr,to)#1->3
        hanou(a-1,bet,fr,to)#2->3
s=1
if a==1:
    s=1
else:    
    for i in range (a-1):
        s=s*2-1+2
print(s)
hanou(a,1,2,3)      

#2개일때 3번 3개일때 7번  4개일때 15번 2^-1
