
while(1!=0):
    e=int(input("If you want to play the game then press 1 else press 0"))
    if(e==1):
        print("the game is on")
        n=int(input("Enter the number you have to withdraw"))
        c=0
        for x in range(1,n+1):
            if(n%x==0):
                c+=1
        if(c==2):
            print(1)
        else:
            print(0)
    if(e==0):
        print("Then you dont want to play this game")
        break
