list,sum = [],0
for b in range(int(input())):
    a = int(input())
    sentence = input()
    word = len(sentence.split())
    x = sentence.split()
    if a in range(1,len(x)):
        for y in x[a]:
            sum+=ord(y)
        print(sum)
        sum=0
    else:
        print("-1")
