def binary_search(arr, target):
    numMin = 0
    numMax = len(arr) - 1
    
    while numMin <= numMax:
        mid = (numMin + numMax) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            numMin = mid + 1
        else:
            numMax = mid - 1
    return -1
    

#ouput (indice del target)
#inputs
print("Ingrese un número del 1 al 10: ")
target = int(input())
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# "Binary Search, buscar un elemento en un arreglo ordenado\nNumero entre 1 y 10"
print(f'índice del numero a buscar: {binary_search(arr, target)}')
