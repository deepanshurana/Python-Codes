#=== Program for finding the total targets from pair difference===
def pairs(k, arr,n):
    i,j = 0,1
    count = 0
    sorted(arr, reverse = True)
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i] - arr[j] == k or arr[j] - arr[i] == k):
                count += 1
    return count


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr,n)
    print(result)
