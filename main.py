def average(array):
    s=set(arr)
    a=sum(s)/len(s)
    return a

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)