import random
def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

num = int(input("Enter the total number of elements to be sorted: "))
arr = [random.randint(0, 1000) for _ in range(num)]
print("The randomly generated array is:")
print(" ".join(map(str,arr)))
bubblesort(arr)
print("The sorted array is:")
print(" ".join(map(str,arr)))
