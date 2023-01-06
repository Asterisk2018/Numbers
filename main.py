def sort_number_list(number_list):
    for i in range(len(number_list)):
        for j in range(len(number_list) - i - 1):
            if number_list[j] > number_list[j + 1]:
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
    return number_list


def index_numder(number_list, number):
    first = 0
    last = len(number_list) - 1
    idx = -1
    while (first <= last) and (idx == -1):
        mid = (first + last) // 2
        if number_list[mid] == number:
            idx = mid
        else:
            if number < number_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return idx


def number_max_min(number_list):
    try:
        while True:
            if input_number < max(number_list) and input_number > min(number_list):
                number_list.append(input_number)
                break
    except ValueError:
        print("Нужно ввести число! Попробуйте ещё раз.")


while True:
    try:
        number_list = [int(x) for x in input("Введите числа через пробел: ").split()]
    except ValueError:
        print("Нужно ввести число! Попробуйте ещё раз.")
    else:
        sort_number_list(number_list)
        print(number_list)
        try:
            input_number = int(input(f'Введите число в диапазоне от {number_list[0]} до {number_list[-1]}:'))
        except ValueError:
            print("Нужно ввести число! Попробуйте ещё раз.")
        else:
            number_max_min(number_list)
            sort_number_list(number_list)
            index_numder(number_list, input_number)
            print(f'Список чисел :{number_list}')
            print(f'Индекс числа идущего перед {input_number} = {index_numder(number_list, input_number) - 1}.')
            print(f'Число идущее перед {input_number} = {number_list[index_numder(number_list, input_number) - 1]}.')
            print(
                f'Число {input_number} не больше максимального {number_list[-1]} и не меньше минимального {number_list[0]}.')
            break