def minimumAbsDifference(arr):
    arr.sort()
    result = []
    min_diff = float("inf")
    for i in range(len(arr) - 1):
        diff = abs(arr[i+1] - arr[i]) 
        if diff < min_diff:
            min_diff = diff
            result.clear()   
        if diff == min_diff:
            result.append((arr[i], arr[i+1]))
    return result

print(minimumAbsDifference([4,2,1,3]))