# Задача 11.120
List = [156, 167, 172, 184, 192, 173, 192, 186]
result = max(List)
print(List.count(result), 'people have a maximum height')

# Задача 11.132
List = [200, 14, 23, 100, 0, 15, 36, 44, 58, 91, 32, 2]
result1 = max(List)
print('Maximum element is', result1, ', its index is', List.index(result1))
index1 = List.index(result1)
List.remove(result1)
result2 = max(List)
List.insert(index1, result1)
print('Second maximum element is', result2, ', its index is', List.index(result2))

List = [100, 14, 23, 200, 0, 15, 36, 44, 58, 91, 32, 2]
result1 = min(List)
print('Minimum element is', result1, ', its index is', List.index(result1))
index1 = List.index(result1)
List.remove(result1)
result2 = min(List)
List.insert(index1, result1)
print('Second minimum element is', result2, ', its index is', List.index(result2))

# Задача 11.145
# а)
someStr = input()
List = list(someStr)
if len(List) % 2 != 0:
    List.pop()
left_part = ''
right_part = ''

for i in range(len(List)):
    if i > (len(List) // 2) - 1:
        left_part += str(List[i])
    else:
        right_part += str(List[i])
result = list(left_part + right_part)
print(List)
print(result)

# б)
someStr = input()
List = list(someStr)
if len(List) % 2 != 0:
    List.pop()

for i in range(1, len(List)):
    if i % 2 == 0:
        continue
    else:
        a = List[i - 1]
        List.remove(List[i - 1])
        List.insert(i, a)
print(list(someStr))
print(List)

# в)
someStr = input()
List = list(someStr)
if len(List) % 2 != 0:
    List.pop()

for i in range(0, len(List) // 2):
    a = List.pop(i)
    a_end = List.pop(-(i + 1))
    List.insert(i, a_end)
    List.insert(len(List) - i, a)

print(list(someStr))
print(List)

# Задача 11.173
someStr = input()
List = list(someStr)

a_end = List.pop(-1)
List.insert(0, a_end)

print(list(someStr))
print(List)

