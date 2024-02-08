def unique(numbers):
    list = []
    for number in numbers:
        if(number not in list):
            list.append(number)
    return list

print(unique([0, 0, 2, 1, 7, 7, 9]))