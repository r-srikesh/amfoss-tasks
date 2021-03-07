while True:
    h = int(input("Height: "))
    if h < 1 or h > 8:
        h = int(input("Height: "))
    elif h >= 1 or h <= 8:
        break

for x in range(1,h+1):
    for y in range(h-x,0,-1):
        print(" ",end=" ")
    for z in range(1,x+1):
        print("#",end=" ")
    print()
