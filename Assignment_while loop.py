t="HELLO"
l=len(t)
i=0
while(i<l):
    if(t[i]=="E" or t[i]=="O"):
        i+=1
        continue
    else:
        print(t[i])
        i+=1
