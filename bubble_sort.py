def bubble_sort(arr):
    """
    Сортировка пузырьком (Bubble Sort)

    Сложность:
    - Время: O(n²) в худшем и среднем случае, O(n) в лучшем случае
    - Память: O(1)

    Args:
        arr: список для сортировки

    Returns:
        отсортированный список
    """
    n = len(arr)

    # Проходим по всем элементам массива
    for i in range(n):
        # Флаг для оптимизации - если не было обменов, массив уже отсортирован
        swapped = False

        # Последние i элементов уже на своих местах
        for j in range(0, n - i - 1):
            # Сравниваем соседние элементы
            if arr[j] > arr[j + 1]:
                # Меняем местами, если они в неправильном порядке
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Если не было обменов, массив отсортирован
        if not swapped:
            break

    return arr


if __name__ == "__main__":
    # Примеры использования

    # Пример 1: обычный массив
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", numbers)
    bubble_sort(numbers)
    print("Отсортированный массив:", numbers)
    print()

    # Пример 2: уже отсортированный массив
    sorted_arr = [1, 2, 3, 4, 5]
    print("Уже отсортированный массив:", sorted_arr)
    bubble_sort(sorted_arr)
    print("После сортировки:", sorted_arr)
    print()

    # Пример 3: массив в обратном порядке
    reverse_arr = [5, 4, 3, 2, 1]
    print("Массив в обратном порядке:", reverse_arr)
    bubble_sort(reverse_arr)
    print("После сортировки:", reverse_arr)
    print()

    # Пример 4: массив с одинаковыми элементами
    duplicate_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("Массив с повторяющимися элементами:", duplicate_arr)
    bubble_sort(duplicate_arr)
    print("После сортировки:", duplicate_arr)
