list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
end = len(list) - 1

for i in range(len(list) // 2):
    aux = list[i]
    list[i] = list[end]
    list[end] = aux
    end -= 1

print(list)