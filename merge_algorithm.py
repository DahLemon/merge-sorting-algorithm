unsorted_array = [5, 3, 2, 7, 4, 6, 1, 8]
print("Unsorted Array:", unsorted_array)


def merge_split(A):

    if len(A) > 1:
        mid = len(A) // 2
        left_half = A[:mid]
        right_half = A[mid:]

        print("Splitting:", A)
        print("Split:", left_half, right_half)

        merge_split(left_half)
        merge_split(right_half)

        merge_order(A, left_half, right_half)


def merge_order(A, left, right):
    i = j = k = 0

    print("Merging:", left, right)

    while i < len(left) and k < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1
    print("Merged:", A)


merge_split(unsorted_array)
