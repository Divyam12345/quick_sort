
def function(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quick_Sort(arr, low, high):
     if low < high:
         pi = function(arr, low, high)
         quick_Sort(arr, low, pi - 1)
         quick_Sort(arr, pi + 1, high)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)

quick_Sort(arr, 0, n - 1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" % arr[i]),
   '''  
   time execution = .71 sec
   time complexity :  average and best-case performance = O(n logn)
   Worst-case = O(n^2)
        
   
   '''