while True:
    N = int(input())
    if N == -1:
        break

    약수 = []

    for i in range(1,N):
        if N % i == 0:
            약수.append(i)

    if sum(약수) != N:
        print(N, "is NOT perfect.")
    else:
        print(N,end=" = ")

        for i in range(len(약수)):
            if len(약수) - 1 == i:
                print(약수[i])
                break
                
            print(약수[i],end=" + ")