# В коде находим все пары элементов с минимальной абсолютной разностью любых двух элементов.
# Прогоняем весь полученный массив через два цикла + сортируем при помощи sorted => сложность
# O(nlogn)

def minimumAbsDifference(arr):
    arr = sorted(arr)                           # сортируем
    min_el = 10 ** 6                            # по условию максимальное значение
    result = []
    for i in range(len(arr) - 1):               # прогоняем по циклу, чтобы
        if arr[i + 1] - arr[i] < min_el:        # узнать минимальную разность элементов
            min_el = arr[i + 1] - arr[i]        
    for i in range(len(arr) - 1):               # прогоняем через второй цикл, где ищем элементы
        if arr[i + 1] - arr[i] == min_el:       # разность которых абсолютна минимальна
            result += [[arr[i], arr[i + 1]]]
    return(result)

print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
print(minimumAbsDifference([1,3,6,10,15]))