from sqlalchemy import ForeignKey


A=int(input())
for i in range(1,A+1):
    
    print(" "*(A-i)+"*"*i)
    i=i+1