for i in range(int(input())):

    x,n = map(int, input().split())
    array = list(map(int, input().strip().split()))[:x]
    array = (array[-n:] + array[:-n])

    print(*array)