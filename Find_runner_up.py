if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    max = max(arr)
    print(max)
    new_arr = [i for i in arr if i!=max]
    print(max(new_arr))
    #max = max(new_arr)
    #print(max)
