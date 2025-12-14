t=int(input())
for i in range(t):
    n=int(input())
    fruits=list(map(int,input().split()))
    
    basket1=-1
    basket2=-1
    count_basket2=0
    current_len=0
    max_len=0
    
    for f in fruits:
        if f == basket1 or f == basket2:
            current_len +=1
        else:
            current_len =count_basket2 + 1 #3rd fruit encountered
        
        if f == basket2:
            count_basket2 += 1
        else:
            count_basket2 = 1
            basket1 = basket2
            basket2 = f
        if current_len > max_len:
            max_len = current_len
    print(max_len)
