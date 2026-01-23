n=int(input())
if n<=30:
    for i in range(0,n+1):
        if i==0:
            print(1, end=" ")
        else:
            print(2**i, end=" ")
else:
    print("30 이하의 수를 입력해주세요.")
