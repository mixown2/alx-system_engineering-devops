def countingSort(arr):
    frequency = [0] * 100
    
    for i in arr:
        frequency[i] += 1
        
    return frequency
