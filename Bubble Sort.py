def bubble_sort(elements):

    size = len(elements)
    for j in range(size-1):
        swapped = False
        for i in range(size-1-j):
            if elements[i] > elements[i+1]:
                temp = elements[i]
                elements[i] = elements[i + 1]
                elements[i + 1] = temp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    #elements = [12, 1,13, 2, 14, 3, 15]
    #elements = [1, 2, 3, 4]
    elements = ["Shivam", "Ravi", "Bansi", "Krishna"]
    bubble_sort(elements)
    print(elements)