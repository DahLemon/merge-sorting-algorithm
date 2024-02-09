! Basic knowledge of Python and unittest are required.

What is Merge Sorting?
Merge sorting is when you have an Array of values, which you continue to split into 2 sub arrays, until each value is
it's own subarray, after which each single element sub array gets merged into ascending value. After that each
next subarray gets merged and the values put into ascending value.

Example:
Array [5,3,2,7,4,6,1,8]

                    [5,3,2,7,4,6,1,8]
                        ↙       ↘
                 [5,3,2,7]      [4,6,1,8]
                  ↙     ↘         ↙    ↘
               [5,3]   [2,7]   [4,6]   [1,8]
               ↙  ↘     ↙  ↘    ↙  ↘    ↙  ↘
              [5] [3] [2] [7] [4] [6] [1] [8]
               ↘  ↙    ↘  ↙    ↘  ↙    ↘  ↙
               [3,5]   [2,7]   [4,6]   [1,8]
                 ↘      ↙        ↘      ↙
                 [2,3,5,7]      [1,4,6,8]
                        ↘        ↙
                    [1,2,3,4,5,6,7,8]

Coding this:
1. Define the array that needs sorting:
    `unsorted_array = [5,3,2,7,4,6,1,8]` ➡ we define the array as "unsorted_array"
2. We add a print function to keep track in the logs:
    `print("Unsorted Array:", unsorted_array)`
3. We create the Splitting Loop to split the array until each subarray contains only one element.
    ```
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
    ```
    We add `print("Splitting:", A)` and `print("Split:", left_half, right_half)` to keep track
    of what happens during the splitting.

    `if len(A) > 1:` ➡ as long as the subarray has more than one element, it will continue the
    Secondary Splitting Loop.

    ```
    mid = len(A) // 2
            left_half = A[:mid]
            right_half = A[mid:]
    ```
    ⤷ establish the middle of the array/subarray that's getting split, then establish the left and right
    halves using the middle split as reference.

    ```
    merge_sort(left_half)
            merge_sort(right_half)

            merge_order(A, left_half, right_half)
    ```
    ⤷ Call upon the Merging Loop to start merging + sorting in ascending order,
      which we will add next.

4. We create the Main Merging Loop:
    ```
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
    ```
    We define that left_half and right_half are left and right and give them and the main array/subarray
    a key to use for checking if the subarray/array is sorted.
    `i = j = k = 0`

    We also add `print("Merging:", left, right)` & `print("Merged:", A)` to keep track of what's actually happening during the merging.

    `while i < len(left) and k < len(right):`
    ⤷ If the key of left is smaller in value than the length of left's subarray and the key of right is
    smaller than in value than the length or right's subarray then start the 1st Secondary Merging Loop.

    1st Secondary Merging Loop:
   ```
   if left[i] <= right[j]:
        A[k] = left[i]
        i += 1
   else:
         A[k] = right[j]
         j += 1
   k += 1
   ```
   ⤷ Elements of 'left[i]' and 'right[j]' get compared, if 'left[i]' is less or equal to 'right[j]' then the element of
   the left subarray is placed in the merged array A at position key 'k'. Then the keys 'i' and 'k' are incremented by 1.

    2nd & 3rd Secondary Merging Loop:
   ```
   while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1

   while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1
   ```
   ⤷ This checks whether there are any elements left in the left and right subarrays, if so they will be sent through the
   1st Secondary Merging Loop again.

5. We can check what the algorithm actually does when looking in our logs:
    ```
    Unsorted Array: [5, 3, 2, 7, 4, 6, 1, 8]
    Splitting: [5, 3, 2, 7, 4, 6, 1, 8]
    Split: [5, 3, 2, 7] [4, 6, 1, 8]
    Splitting: [5, 3, 2, 7]
    Split: [5, 3] [2, 7]
    Splitting: [5, 3]
    Split: [5] [3]
    Splitting: [5]
    Splitting: [3]
    Merging: [5] [3]
    Merged: [3, 5]
    Splitting: [2, 7]
    Split: [2] [7]
    Splitting: [2]
    Splitting: [7]
    Merging: [2] [7]
    Merged: [2, 7]
    Merging: [3, 5] [2, 7]
    Merged: [2, 3, 5, 7]
    Splitting: [4, 6, 1, 8]
    Split: [4, 6] [1, 8]
    Splitting: [4, 6]
    Split: [4] [6]
    Splitting: [4]
    Splitting: [6]
    Merging: [4] [6]
    Merged: [4, 6]
    Splitting: [1, 8]
    Split: [1] [8]
    Splitting: [1]
    Splitting: [8]
    Merging: [1] [8]
    Merged: [1, 8]
    Merging: [4, 6] [1, 8]
    Merged: [1, 4, 6, 8]
    Merging: [2, 3, 5, 7] [1, 4, 6, 8]
    Merged: [1, 2, 3, 4, 5, 7, 6, 8]
    ```

    We can see that the last "Merged:" print is our Array that's been fully sorted and correct.