def selection_sort(elements):
    for i in range(len(elements)):
        min_index = i
        for j in range(i+1, len(elements)):
            if elements[min_index] > elements[j]:
                min_index = j
        elements[i], elements[min_index] = elements[min_index], elements[i]



if __name__ == '__main__':
    #elements = [25, 12, 12, 10, 28, 28, 16, 21, 5, 5, 5]
    elements = ["Shivam", "Bansi", "Ravi", "Kano"]
    selection_sort(elements)
    print(elements)