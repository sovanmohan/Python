l=[12,75,150,180,145,525,50]
for x in l:
    if(x%5==0):
        if(x>150):
            if(x>500):
                break
            else:
                continue
        else:
            print(x)
