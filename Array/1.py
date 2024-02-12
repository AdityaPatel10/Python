from array import array
type_code = 'i'   #Define the type of array
arr = array(type_code, [1, 2, 3, 4, 5])
print("Created Array: ", arr)
for i in range(len(arr)):
    print(arr[i])