# Problem 1: Library Borrowing Records

# Number of books borrowed by each library member
member_borrows = [3, 0, 5, 2, 0, 7, 5, 1, 5, 0]

# Number of times each book has been borrowed
book_borrows = {
    "Python Basics": 12,
    "Data Structures": 25,
    "Algorithms": 18,
    "Operating Systems": 5,
    "DBMS": 25,
    "Networks": 3,
}


def average_borrowed(counts):
    """Average number of books borrowed per member."""
    if not counts:
        return 0
    total = 0
    for c in counts:
        total += c
    return total / len(counts)


def highest_lowest_book(books):
    """Return (highest_book, highest_count, lowest_book, lowest_count)."""
    high_book = low_book = None
    high = float("-inf")
    low = float("inf")
    for title, count in books.items():
        if count > high:
            high, high_book = count, title
        if count < low:
            low, low_book = count, title
    return high_book, high, low_book, low


def count_zero_borrowers(counts):
    """Number of members who borrowed no books."""
    zeros = 0
    for c in counts:
        if c == 0:
            zeros += 1
    return zeros


def mode_of_borrow_counts(counts):
    """Most frequent borrow count (mode) and how many members have it."""
    freq = {}
    for c in counts:
        freq[c] = freq.get(c, 0) + 1
    mode_value, mode_freq = None, 0
    for value, f in freq.items():
        if f > mode_freq:
            mode_value, mode_freq = value, f
    return mode_value, mode_freq


def most_borrowed_book(books):
    """Book with the most borrowings."""
    return max(books, key=books.get)


if __name__ == "__main__":
    print("Average books borrowed per member:", average_borrowed(member_borrows))

    hb, hc, lb, lc = highest_lowest_book(book_borrows)
    print(f"Highest borrowed book: {hb} ({hc} times)")
    print(f"Lowest borrowed book : {lb} ({lc} times)")

    print("Members with 0 borrowings:", count_zero_borrowers(member_borrows))

    mode_val, mode_f = mode_of_borrow_counts(member_borrows)
    print(f"Mode of borrow counts: {mode_val} (occurs {mode_f} times)")
    print("Most frequently borrowed book:", most_borrowed_book(book_borrows))
Complexity analysis (n = number of members or books, k = number of distinct counts)

Operation	Time	Space
Average	O(n)	O(1)
Highest / Lowest book	O(n)	O(1)
Count members with 0 borrows	O(n)	O(1)
Mode of borrow counts	O(n)	O(k), at most O(n)
Most borrowed book	O(n)	O(1)
# Problem 2: Linear Search and Binary Search on Customer Account IDs

def linear_search(ids, target):
    """Check each ID one by one. Works on unsorted lists."""
    for i in range(len(ids)):
        if ids[i] == target:
            return i          # index where found
    return -1                 # not found


def binary_search(ids, target):
    """Repeatedly halve the search range. The list MUST be sorted."""
    low, high = 0, len(ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == target:
            return mid
        elif ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    customer_ids = [1045, 1002, 1090, 1033, 1076, 1011, 1058, 1099]

    target = int(input("Enter customer account ID to search: "))

    # Linear search (no sorting needed)
    pos = linear_search(customer_ids, target)
    if pos != -1:
        print(f"[Linear Search] ID {target} found at index {pos}")
    else:
        print(f"[Linear Search] ID {target} not found")

    # Binary search (sort first)
    sorted_ids = sorted(customer_ids)
    print("Sorted IDs:", sorted_ids)
    pos = binary_search(sorted_ids, target)
    if pos != -1:
        print(f"[Binary Search] ID {target} found at index {pos} (sorted list)")
    else:
        print(f"[Binary Search] ID {target} not found")
Complexity analysis

Algorithm	Best	Average / Worst	Space
Linear search	O(1)	O(n)	O(1)
Binary search (iterative)	O(1)	O(log n)	O(1)

Binary search needs sorted data. Sorting costs O(n log n) once, so it pays off when you do many searches on the same list. For a single search on an unsorted list, linear search is cheaper overall.

Let me know if you'd like these as .py files, or want the recursive binary search version too.
# Problem 1: Library Borrowing Records

member_borrows = [3, 0, 5, 2, 0, 7, 5, 1, 5, 0]

book_borrows = {
    "Python Basics": 12,
    "Data Structures": 25,
    "Algorithms": 18,
    "Operating Systems": 5,
    "DBMS": 25,
    "Networks": 3,
}


def average_borrowed(counts):
    if not counts:
        return 0
    total = 0
    for c in counts:
        total += c
    return total / len(counts)


def highest_lowest_book(books):
    high_book = low_book = None
    high = float("-inf")
    low = float("inf")
    for title, count in books.items():
        if count > high:
            high, high_book = count, title
        if count < low:
            low, low_book = count, title
    return high_book, high, low_book, low


def count_zero_borrowers(counts):
    zeros = 0
    for c in counts:
        if c == 0:
            zeros += 1
    return zeros


def mode_of_borrow_counts(counts):
    freq = {}
    for c in counts:
        freq[c] = freq.get(c, 0) + 1
    mode_value, mode_freq = None, 0
    for value, f in freq.items():
        if f > mode_freq:
            mode_value, mode_freq = value, f
    return mode_value, mode_freq


def most_borrowed_book(books):
    return max(books, key=books.get)


print("Average books borrowed per member:", average_borrowed(member_borrows))

hb, hc, lb, lc = highest_lowest_book(book_borrows)
print(f"Highest borrowed book: {hb} ({hc} times)")
print(f"Lowest borrowed book : {lb} ({lc} times)")

print("Members with 0 borrowings:", count_zero_borrowers(member_borrows))

mode_val, mode_f = mode_of_borrow_counts(member_borrows)
print(f"Mode of borrow counts: {mode_val} (occurs {mode_f} times)")
print("Most frequently borrowed book:", most_borrowed_book(book_borrows))
Complexity analysis

Operation	Time	Space
Average	O(n)	O(1)
Highest / Lowest book	O(n)	O(1)
Count members with 0 borrows	O(n)	O(1)
Mode of borrow counts	O(n)	O(k), at most O(n)
Most borrowed book	O(n)	O(1)
# Problem 2: Linear Search and Binary Search on Customer Account IDs

def linear_search(ids, target):
    for i in range(len(ids)):
        if ids[i] == target:
            return i
    return -1


def binary_search(ids, target):
    low, high = 0, len(ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == target:
            return mid
        elif ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


customer_ids = [1045, 1002, 1090, 1033, 1076, 1011, 1058, 1099]
target = int(input("Enter customer account ID to search: "))

pos = linear_search(customer_ids, target)
if pos != -1:
    print(f"[Linear Search] ID {target} found at index {pos}")
else:
    print(f"[Linear Search] ID {target} not found")

sorted_ids = sorted(customer_ids)
print("Sorted IDs:", sorted_ids)
pos = binary_search(sorted_ids, target)
if pos != -1:
    print(f"[Binary Search] ID {target} found at index {pos} (sorted list)")
else:
    print(f"[Binary Search] ID {target} not found")
Complexity analysis

Algorithm	Best	Average / Worst	Space
Linear search	O(1)	O(n)	O(1)
Binary search (iterative)	O(1)	O(log n)	O(1)

Binary search requires a sorted list, which is why the code sorts the IDs first.
# Problem 1: Library Borrowing Records

# Input: borrow counts of members
n = int(input("Enter number of members: "))
members = []
for i in range(n):
    members.append(int(input("Books borrowed by member " + str(i + 1) + ": ")))

# Input: books and their borrow counts
m = int(input("Enter number of books: "))
book_names = []
book_counts = []
for i in range(m):
    book_names.append(input("Book name " + str(i + 1) + ": "))
    book_counts.append(int(input("Times borrowed: ")))

# 1. Average books borrowed
total = 0
for x in members:
    total = total + x
average = total / n
print("Average books borrowed:", average)

# 2. Highest and lowest borrowed book
high = 0
low = 0
for i in range(m):
    if book_counts[i] > book_counts[high]:
        high = i
    if book_counts[i] < book_counts[low]:
        low = i
print("Highest borrowed book:", book_names[high], "-", book_counts[high])
print("Lowest borrowed book:", book_names[low], "-", book_counts[low])

# 3. Members who borrowed 0 books
zero = 0
for x in members:
    if x == 0:
        zero = zero + 1
print("Members with 0 borrowings:", zero)

# 4. Mode of borrow counts
mode = members[0]
max_freq = 0
for x in members:
    freq = 0
    for y in members:
        if x == y:
            freq = freq + 1
    if freq > max_freq:
        max_freq = freq
        mode = x
print("Mode of borrow counts:", mode, "(appears", max_freq, "times)")
Complexity analysis

Operation	Time	Space
Average	O(n)	O(1)
Highest / Lowest book	O(m)	O(1)
Count members with 0 borrows	O(n)	O(1)
Mode (nested loops)	O(n²)	O(1)

Here n is the number of members and m is the number of books.
# Problem 2: Linear Search and Binary Search

n = int(input("Enter number of customer IDs: "))
ids = []
for i in range(n):
    ids.append(int(input("Enter ID: ")))

key = int(input("Enter ID to search: "))

# Linear Search
found = False
for i in range(n):
    if ids[i] == key:
        print("Linear Search: ID found at index", i)
        found = True
        break
if not found:
    print("Linear Search: ID not found")

# Binary Search (list must be sorted)
ids.sort()
print("Sorted list:", ids)

low = 0
high = n - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if ids[mid] == key:
        print("Binary Search: ID found at index", mid)
        found = True
        break
    elif ids[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
if not found:
    print("Binary Search: ID not found")
Complexity analysis

Algorithm	Time (worst)	Space
Linear search	O(n)	O(1)
Binary search	O(log n)	O(1)

Binary search works only on a sorted list, so the code sorts the IDs before searching.
# Problem 1: Library Borrowing Records

def average_borrowed(members):
    total = 0
    for x in members:
        total = total + x
    return total / len(members)


def highest_book(book_names, book_counts):
    high = 0
    for i in range(len(book_counts)):
        if book_counts[i] > book_counts[high]:
            high = i
    return book_names[high], book_counts[high]


def lowest_book(book_names, book_counts):
    low = 0
    for i in range(len(book_counts)):
        if book_counts[i] < book_counts[low]:
            low = i
    return book_names[low], book_counts[low]


def count_zero(members):
    zero = 0
    for x in members:
        if x == 0:
            zero = zero + 1
    return zero


def find_mode(members):
    mode = members[0]
    max_freq = 0
    for x in members:
        freq = 0
        for y in members:
            if x == y:
                freq = freq + 1
        if freq > max_freq:
            max_freq = freq
            mode = x
    return mode, max_freq


# Input: borrow counts of members
n = int(input("Enter number of members: "))
members = []
for i in range(n):
    members.append(int(input("Books borrowed by member " + str(i + 1) + ": ")))

# Input: books and their borrow counts
m = int(input("Enter number of books: "))
book_names = []
book_counts = []
for i in range(m):
    book_names.append(input("Book name " + str(i + 1) + ": "))
    book_counts.append(int(input("Times borrowed: ")))

# Calling the functions
print("Average books borrowed:", average_borrowed(members))

name, count = highest_book(book_names, book_counts)
print("Highest borrowed book:", name, "-", count)

name, count = lowest_book(book_names, book_counts)
print("Lowest borrowed book:", name, "-", count)

print("Members with 0 borrowings:", count_zero(members))

mode, freq = find_mode(members)
print("Mode of borrow counts:", mode, "(appears", freq, "times)")
Complexity analysis

Function	Time	Space
average_borrowed	O(n)	O(1)
highest_book	O(m)	O(1)
lowest_book	O(m)	O(1)
count_zero	O(n)	O(1)
find_mode	O(n²)	O(1)

Here n is the number of members and m is the number of books.
# Problem 2: Linear Search and Binary Search

def linear_search(ids, key):
    for i in range(len(ids)):
        if ids[i] == key:
            return i
    return -1


def binary_search(ids, key):
    low = 0
    high = len(ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == key:
            return mid
        elif ids[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Input
n = int(input("Enter number of customer IDs: "))
ids = []
for i in range(n):
    ids.append(int(input("Enter ID: ")))

key = int(input("Enter ID to search: "))

# Linear search
pos = linear_search(ids, key)
if pos != -1:
    print("Linear Search: ID found at index", pos)
else:
    print("Linear Search: ID not found")

# Binary search (list must be sorted)
ids.sort()
print("Sorted list:", ids)

pos = binary_search(ids, key)
if pos != -1:
    print("Binary Search: ID found at index", pos)
else:
    print("Binary Search: ID not found")
Complexity analysis

Function	Time (worst)	Space
linear_search	O(n)	O(1)
binary_search	O(log n)	O(1)

Binary search works only on a sorted list, so the code sorts the IDs before calling it.
# Problem 2: Linear Search and Binary Search on Customer Account IDs

def read_ids(n):
    ids = []
    for i in range(n):
        ids.append(int(input("Enter ID: ")))
    return ids


def linear_search(ids, key):
    for i in range(len(ids)):
        if ids[i] == key:
            return i
    return -1


def binary_search(ids, key):
    low = 0
    high = len(ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == key:
            return mid
        elif ids[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Input
n = int(input("Enter number of customer IDs: "))
ids = read_ids(n)
key = int(input("Enter ID to search: "))

# Linear search (works on unsorted list)
pos = linear_search(ids, key)
if pos != -1:
    print("Linear Search: ID found at index", pos)
else:
    print("Linear Search: ID not found")

# Binary search (list must be sorted)
ids.sort()
print("Sorted list:", ids)

pos = binary_search(ids, key)
if pos != -1:
    print("Binary Search: ID found at index", pos)
else:
    print("Binary Search: ID not found")
Enter number of customer IDs: 5
Enter ID: 105
Enter ID: 102
Enter ID: 109
Enter ID: 101
Enter ID: 107
Enter ID to search: 109
Linear Search: ID found at index 2
Sorted list: [101, 102, 105, 107, 109]
Binary Search: ID found at index 4
The indexes differ because linear search runs on the original list and binary search runs on the sorted list.

Complexity analysis

Function	Best	Worst	Space
read_ids	O(n)	O(n)	O(n)
linear_search	O(1)	O(n)	O(1)
binary_search	O(1)	O(log n)	O(1)

Binary search is faster because it halves the search range at every step. For 1,000,000 IDs, linear search may need up to 1,000,000 comparisons, while binary search needs about 20.
# Problem 3: Sorting Employee Salaries (Selection Sort and Bubble Sort)

def read_salaries(n):
    salaries = []
    for i in range(n):
        salaries.append(float(input("Enter salary " + str(i + 1) + ": ")))
    return salaries


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap the smallest element into position i
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True
        if not swapped:
            break
    return arr


def top_five(sorted_arr):
    print("Top five highest salaries:")
    count = 0
    i = len(sorted_arr) - 1
    while i >= 0 and count < 5:
        print(count + 1, ".", sorted_arr[i])
        count = count + 1
        i = i - 1


# Input
n = int(input("Enter number of employees: "))
salaries = read_salaries(n)

# Selection sort (on a copy, so the original list stays unchanged)
selection_result = selection_sort(salaries[:])
print("Selection Sort (ascending):", selection_result)

# Bubble sort (on another copy)
bubble_result = bubble_sort(salaries[:])
print("Bubble Sort (ascending):", bubble_result)

# Top five highest salaries
top_five(bubble_result)
Enter number of employees: 7
Enter salary 1: 45000.50
Enter salary 2: 72000.0
Enter salary 3: 38000.75
Enter salary 4: 91000.25
Enter salary 5: 56000.0
Enter salary 6: 67000.5
Enter salary 7: 83000.0
Selection Sort (ascending): [38000.75, 45000.5, 56000.0, 67000.5, 72000.0, 83000.0, 91000.25]
Bubble Sort (ascending): [38000.75, 45000.5, 56000.0, 67000.5, 72000.0, 83000.0, 91000.25]
Top five highest salaries:
1 . 91000.25
2 . 83000.0
3 . 72000.0
4 . 67000.5
5 . 56000.0
If fewer than five employees are entered, the program simply prints all the salaries it has.

Complexity analysis

Function	Best	Worst	Space
read_salaries	O(n)	O(n)	O(n)
selection_sort	O(n²)	O(n²)	O(1)
bubble_sort	O(n) (already sorted, with the swapped flag)	O(n²)	O(1)
top_five	O(1)	O(1)	O(1)

Selection sort always makes about n²/2 comparisons, even on sorted data, but it does at most n swaps. Bubble sort can stop early when no swaps happen, so it is faster on nearly sorted lists. The top_five function prints at most five items, so it is constant time once the list is sorted.
# Group B - Problem 1: Undo/Redo System using Stack

class Stack:
    def __init__(self, size):
        self.items = [None] * size
        self.size = size
        self.top = -1                      # -1 means the stack is empty

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def push(self, value):
        if self.is_full():
            print("Stack Overflow")
            return False
        self.top = self.top + 1
        self.items[self.top] = value
        return True

    def pop(self):
        if self.is_empty():
            return None
        value = self.items[self.top]
        self.top = self.top - 1
        return value


def make_change(undo_stack, redo_stack, text):
    if undo_stack.push(text):
        redo_stack.top = -1                # a new change clears the redo history
        print("Change made:", text)


def undo_action(undo_stack, redo_stack):
    if undo_stack.is_empty():
        print("Nothing to undo")
    else:
        change = undo_stack.pop()
        redo_stack.push(change)
        print("Undone:", change)


def redo_action(undo_stack, redo_stack):
    if redo_stack.is_empty():
        print("Nothing to redo")
    else:
        change = redo_stack.pop()
        undo_stack.push(change)
        print("Redone:", change)


def display_document(undo_stack):
    if undo_stack.is_empty():
        print("Document is empty")
    else:
        text = ""
        for i in range(undo_stack.top + 1):
            text = text + undo_stack.items[i] + " "
        print("Document state:", text)


# Main program
undo_stack = Stack(50)
redo_stack = Stack(50)

while True:
    print("\n1. Make a Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        text = input("Enter the text to add: ")
        make_change(undo_stack, redo_stack, text)
    elif choice == 2:
        undo_action(undo_stack, redo_stack)
    elif choice == 3:
        redo_action(undo_stack, redo_stack)
    elif choice == 4:
        display_document(undo_stack)
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
1. Make a Change  2. Undo  3. Redo  4. Display Document  5. Exit

Enter your choice: 1
Enter the text to add: Hello
Change made: Hello
Enter your choice: 1
Enter the text to add: World
Change made: World
Enter your choice: 4
Document state: Hello World
Enter your choice: 2
Undone: World
Enter your choice: 4
Document state: Hello
Enter your choice: 3
Redone: World
Enter your choice: 4
Document state: Hello World
Enter your choice: 5
Exiting...
How it works

undo_stack holds the changes currently in the document. The latest change sits at top.
redo_stack holds the changes that were undone.
Undo pops from undo_stack and pushes to redo_stack. Redo does the reverse.
Making a new change resets redo_stack.top = -1, because redo history is no longer valid after a fresh edit.
Complexity analysis (n = number of changes in the document)

Function	Time	Space
push / pop	O(1)	O(1)
make_change	O(1)	O(1)
undo_action	O(1)	O(1)
redo_action	O(1)	O(1)
display_document	O(n)	O(n) (builds the text string)

Overall space for the two stacks is O(size), which is fixed at creation.
Here are just the user-defined functions, with no class and no menu. The stacks use a top variable.

python
# Group B - Problem 1: Undo/Redo using Stack (functions only)

size = 50
undo_stack = [None] * size
redo_stack = [None] * size
undo_top = -1          # -1 means the undo stack is empty
redo_top = -1          # -1 means the redo stack is empty


def make_change(text):
    global undo_top, redo_top
    if undo_top == size - 1:
        print("Stack Overflow")
    else:
        undo_top = undo_top + 1
        undo_stack[undo_top] = text
        redo_top = -1                      # new change clears redo history
        print("Change made:", text)


def undo_action():
    global undo_top, redo_top
    if undo_top == -1:
        print("Nothing to undo")
    else:
        change = undo_stack[undo_top]
        undo_top = undo_top - 1
        redo_top = redo_top + 1
        redo_stack[redo_top] = change
        print("Undone:", change)


def redo_action():
    global undo_top, redo_top
    if redo_top == -1:
        print("Nothing to redo")
    else:
        change = redo_stack[redo_top]
        redo_top = redo_top - 1
        undo_top = undo_top + 1
        undo_stack[undo_top] = change
        print("Redone:", change)


def display_document():
    if undo_top == -1:
        print("Document is empty")
    else:
        text = ""
        for i in range(undo_top + 1):
            text = text + undo_stack[i] + " "
        print("Document state:", text)
How to call them

python
make_change("Hello")
make_change("World")
display_document()     # Document state: Hello World
undo_action()          # Undone: World
display_document()     # Document state: Hello
redo_action()          # Redone: World
display_document()     # Document state: Hello World
Complexity analysis (n = number of changes in the document)

Function	Time	Space
make_change	O(1)	O(1)
undo_action	O(1)	O(1)
redo_action	O(1)	O(1)
display_document	O(n)	O(n)

just
Here it is with a single stack and only one top variable. Undo moves top down, and redo moves it back up. Undone items stay in the list above top until a new change replaces them.

python
# Group B - Problem 1: Undo/Redo using a single Stack and one top

stack = []
top = -1               # points to the latest change; -1 means empty


def make_change(text):
    global top
    # remove undone changes above top, since redo is no longer valid
    while len(stack) > top + 1:
        stack.pop()
    stack.append(text)
    top = top + 1
    print("Change made:", text)


def undo_action():
    global top
    if top == -1:
        print("Nothing to undo")
    else:
        print("Undone:", stack[top])
        top = top - 1


def redo_action():
    global top
    if top == len(stack) - 1:
        print("Nothing to redo")
    else:
        top = top + 1
        print("Redone:", stack[top])


def display_document():
    if top == -1:
        print("Document is empty")
    else:
        text = ""
        for i in range(top + 1):
            text = text + stack[i] + " "
        print("Document state:", text)
How to call them
make_change("Hello")
make_change("World")
display_document()     # Document state: Hello World
undo_action()          # Undone: World
display_document()     # Document state: Hello
redo_action()          # Redone: World
display_document()     # Document state: Hello World
How it works

stack[0] to stack[top] is the current document.
Items after top are undone changes waiting for redo.
A new change removes those items, so redo history is cleared.

Complexity analysis (n = number of changes in the document)
Complexity analysis (n = number of changes in the document)

Function	Time	Space
make_change	O(1) amortized (O(k) if k undone items are removed)	O(1)
undo_action	O(1)	O(1)
redo_action	O(1)	O(1)
display_document	O(n)	O(n)
Files hidden when shared

give me code using front and rear keyword in queue

Here is Question 2 in the same style: one queue with front and rear, and a user-defined function for each feature.

python
# Group B - Problem 2: Event Processing System using Queue

size = 50
queue = [None] * size
front = -1             # -1 means the queue is empty
rear = -1


def add_event(event):
    global front, rear
    if rear == size - 1:
        print("Queue is full")
    else:
        if front == -1:
            front = 0
        rear = rear + 1
        queue[rear] = event
        print("Event added:", event)


def process_event():
    global front, rear
    if front == -1:
        print("No events to process")
    else:
        event = queue[front]
        print("Processed event:", event)
        if front == rear:          # last event was removed
            front = -1
            rear = -1
        else:
            front = front + 1


def display_events():
    if front == -1:
        print("No pending events")
    else:
        print("Pending events:")
        for i in range(front, rear + 1):
            print(i - front + 1, ".", queue[i])


def cancel_event(event):
    global front, rear
    if front == -1:
        print("No events to cancel")
        return
    pos = -1
    for i in range(front, rear + 1):
        if queue[i] == event:
            pos = i
            break
    if pos == -1:
        print("Event not found (already processed or never added)")
    else:
        # shift later events one step left to fill the gap
        for i in range(pos, rear):
            queue[i] = queue[i + 1]
        rear = rear - 1
        if rear < front:           # queue became empty
            front = -1
            rear = -1
        print("Event cancelled:", event)

How to call them
add_event("Login")
add_event("Upload File")
add_event("Send Email")
display_events()
process_event()          # Processed event: Login
cancel_event("Send Email")
display_events()         # Pending events: 1 . Upload File
Event added: Login
Event added: Upload File
Event added: Send Email
Pending events:
1 . Login
2 . Upload File
3 . Send Email
Processed event: Login
Event cancelled: Send Email
Pending events:
1 . Upload File
How it works

rear points to the newest event, where new events are added.
front points to the oldest event, which is processed first (FIFO).
When front == rear and that event is removed, both go back to -1.
Cancel finds the event, shifts the later events left, and moves rear back by one.

Complexity analysis (n = number of pending events)

Function	Time	Space
add_event	O(1)	O(1)
process_event	O(1)	O(1)
display_events	O(n)	O(1)
cancel_event	O(n)	O(1)

The queue itself uses fixed space of O(size).
Here is Question 3 in the same style: one queue with front and rear, and a user-defined function for each operation. Each call stores its customer ID and call time together. Customer IDs must be unique, so addCall rejects a duplicate.
# Group B - Problem 3: Call Center Queue using Queue

size = 50
id_queue = [None] * size       # customer IDs
time_queue = [None] * size     # call times (in minutes)
front = -1                     # -1 means the queue is empty
rear = -1


def isQueueEmpty():
    return front == -1


def addCall(customerID, callTime):
    global front, rear
    if rear == size - 1:
        print("Queue is full")
        return
    # customer IDs must be unique
    if front != -1:
        for i in range(front, rear + 1):
            if id_queue[i] == customerID:
                print("Customer ID", customerID, "is already in the queue")
                return
    if front == -1:
        front = 0
    rear = rear + 1
    id_queue[rear] = customerID
    time_queue[rear] = callTime
    print("Call added: Customer", customerID, "-", callTime, "minutes")


def answerCall():
    global front, rear
    if isQueueEmpty():
        print("No calls to answer")
    else:
        print("Answered call: Customer", id_queue[front], "-", time_queue[front], "minutes")
        if front == rear:          # last call was removed
            front = -1
            rear = -1
        else:
            front = front + 1


def viewQueue():
    if isQueueEmpty():
        print("No calls in the queue")
    else:
        print("Calls in the queue:")
        for i in range(front, rear + 1):
            print(i - front + 1, ". Customer", id_queue[i], "-", time_queue[i], "minutes")
How to call them

python
addCall(101, 5)
addCall(102, 3)
addCall(103, 8)
viewQueue()
answerCall()                  # Answered call: Customer 101 - 5 minutes
viewQueue()
print(isQueueEmpty())         # False
Call added: Customer 101 - 5 minutes
Call added: Customer 102 - 3 minutes
Call added: Customer 103 - 8 minutes
Calls in the queue:
1 . Customer 101 - 5 minutes
2 . Customer 102 - 3 minutes
3 . Customer 103 - 8 minutes
Answered call: Customer 101 - 5 minutes
Calls in the queue:
1 . Customer 102 - 3 minutes
2 . Customer 103 - 8 minutes
False
How it works

rear points to the newest call, where new calls are added.
front points to the oldest call, which is answered first (FIFO).
id_queue and time_queue use the same index, so position i holds one call's ID and its time.
When the last call is answered, front and rear go back to -1, which makes isQueueEmpty() return True.

Complexity analysis (n = number of calls in the queue)

Function	Time	Space
addCall	O(n) (checks for duplicate ID)	O(1)
answerCall	O(1)	O(1)
viewQueue	O(n)	O(1)
isQueueEmpty	O(1)	O(1)

If you remove the duplicate ID check, addCall becomes O(1).

Here is Question 4 in the same style: a singly linked list with a user-defined function for each operation. A small Node class is needed because a linked list is built from nodes.

python
# Group B - Problem 4: Student Record Management using Singly Linked List

class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


head = None            # None means the list is empty


def find_node(roll):
    temp = head
    while temp is not None:
        if temp.roll == roll:
            return temp
        temp = temp.next
    return None


def add_student(roll, name, marks):
    global head
    if find_node(roll) is not None:
        print("Roll No", roll, "already exists")
        return
    new_node = Node(roll, name, marks)
    if head is None:
        head = new_node
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    print("Student added:", name)


def delete_student(roll):
    global head
    if head is None:
        print("List is empty")
        return
    if head.roll == roll:              # deleting the first node
        head = head.next
        print("Student deleted: Roll No", roll)
        return
    prev = head
    curr = head.next
    while curr is not None:
        if curr.roll == roll:
            prev.next = curr.next
            print("Student deleted: Roll No", roll)
            return
        prev = curr
        curr = curr.next
    print("Roll No", roll, "not found")


def update_student(roll, new_name, new_marks):
    node = find_node(roll)
    if node is None:
        print("Roll No", roll, "not found")
    else:
        node.name = new_name
        node.marks = new_marks
        print("Student updated: Roll No", roll)


def search_student(roll):
    node = find_node(roll)
    if node is None:
        print("Roll No", roll, "not found")
    else:
        print("Found -> Roll:", node.roll, "| Name:", node.name, "| Marks:", node.marks)


def sort_students(by, order):
    # by = "roll" or "marks", order = "asc" or "desc"
    if head is None or head.next is None:
        return
    swapped = True
    while swapped:
        swapped = False
        temp = head
        while temp.next is not None:
            if by == "roll":
                a = temp.roll
                b = temp.next.roll
            else:
                a = temp.marks
                b = temp.next.marks
            if (order == "asc" and a > b) or (order == "desc" and a < b):
                # swap the data of the two nodes
                temp.roll, temp.next.roll = temp.next.roll, temp.roll
                temp.name, temp.next.name = temp.next.name, temp.name
                temp.marks, temp.next.marks = temp.next.marks, temp.marks
                swapped = True
            temp = temp.next
    print("Sorted by", by, "in", order, "order")


def display_students():
    if head is None:
        print("No student records")
        return
    temp = head
    while temp is not None:
        print("Roll:", temp.roll, "| Name:", temp.name, "| Marks:", temp.marks)
        temp = temp.next
How to call them
add_student(102, "Amit", 78)
add_student(101, "Neha", 91)
add_student(103, "Ravi", 65)
display_students()

sort_students("marks", "desc")
display_students()

sort_students("roll", "asc")
display_students()

update_student(102, "Amit", 85)
search_student(102)
delete_student(101)
display_students()
Student added: Amit
Student added: Neha
Student added: Ravi
Roll: 102 | Name: Amit | Marks: 78
Roll: 101 | Name: Neha | Marks: 91
Roll: 103 | Name: Ravi | Marks: 65
Sorted by marks in desc order
Roll: 101 | Name: Neha | Marks: 91
Roll: 102 | Name: Amit | Marks: 78
Roll: 103 | Name: Ravi | Marks: 65
Sorted by roll in asc order
Roll: 101 | Name: Neha | Marks: 91
Roll: 102 | Name: Amit | Marks: 78
Roll: 103 | Name: Ravi | Marks: 65
Student updated: Roll No 102
Found -> Roll: 102 | Name: Amit | Marks: 85
Student deleted: Roll No 101
Roll: 102 | Name: Amit | Marks: 85
Roll: 103 | Name: Ravi | Marks: 65
How it works

head points to the first node, and each node's next points to the following node. The last node's next is None.
add_student walks to the last node and attaches the new node there. It rejects a duplicate roll number.
delete_student handles the first node separately, then uses prev and curr to unlink a node from the middle or end.
sort_students uses bubble sort and swaps the data inside nodes, not the links, which keeps it simple. Changing by and order gives all four display orders: marks or roll number, ascending or descending.

Complexity analysis (n = number of students)

Function	Time	Space
add_student	O(n) (duplicate check and walk to end)	O(1)
delete_student	O(n)	O(1)
update_student	O(n)	O(1)
search_student	O(n)	O(1)
sort_students	O(n²)	O(1)
display_students	O(n)	O(1)

The list itself takes O(n) space, since each student is one node
Here is a simpler version with the same operations. I removed the helper function and the duplicate check, so each function is short and does one job.

python
# Group B - Problem 4: Student Records using Singly Linked List

class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


head = None


def add_student(roll, name, marks):
    global head
    new_node = Node(roll, name, marks)
    if head is None:
        head = new_node
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    print("Student added")


def delete_student(roll):
    global head
    if head is None:
        print("List is empty")
        return
    if head.roll == roll:
        head = head.next
        print("Student deleted")
        return
    temp = head
    while temp.next is not None:
        if temp.next.roll == roll:
            temp.next = temp.next.next
            print("Student deleted")
            return
        temp = temp.next
    print("Student not found")


def update_student(roll, new_name, new_marks):
    temp = head
    while temp is not None:
        if temp.roll == roll:
            temp.name = new_name
            temp.marks = new_marks
            print("Student updated")
            return
        temp = temp.next
    print("Student not found")


def search_student(roll):
    temp = head
    while temp is not None:
        if temp.roll == roll:
            print("Found:", temp.roll, temp.name, temp.marks)
            return
        temp = temp.next
    print("Student not found")


def sort_students(by, order):
    # by = "roll" or "marks", order = "asc" or "desc"
    i = head
    while i is not None:
        j = i.next
        while j is not None:
            if by == "roll":
                a = i.roll
                b = j.roll
            else:
                a = i.marks
                b = j.marks

            if (order == "asc" and a > b) or (order == "desc" and a < b):
                # swap the data of the two nodes
                i.roll, j.roll = j.roll, i.roll
                i.name, j.name = j.name, i.name
                i.marks, j.marks = j.marks, i.marks
            j = j.next
        i = i.next
    print("Sorted by", by, "in", order, "order")


def display_students():
    if head is None:
        print("No records")
        return
    temp = head
    while temp is not None:
        print(temp.roll, temp.name, temp.marks)
        temp = temp.next
# Group B - Problem 4: Student Records using Singly Linked List

class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


head = None


def add_student(roll, name, marks):
    global head
    new_node = Node(roll, name, marks)
    if head is None:
        head = new_node
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    print("Student added")


def delete_student(roll):
    global head
    if head is None:
        print("List is empty")
        return
    if head.roll == roll:
        head = head.next
        print("Student deleted")
        return
    temp = head
    while temp.next is not None:
        if temp.next.roll == roll:
            temp.next = temp.next.next
            print("Student deleted")
            return
        temp = temp.next
    print("Student not found")


def update_student(roll, new_name, new_marks):
    temp = head
    while temp is not None:
        if temp.roll == roll:
            temp.name = new_name
            temp.marks = new_marks
            print("Student updated")
            return
        temp = temp.next
    print("Student not found")


def search_student(roll):
    temp = head
    while temp is not None:
        if temp.roll == roll:
            print("Found:", temp.roll, temp.name, temp.marks)
            return
        temp = temp.next
    print("Student not found")


def sort_students(by, order):
    # by = "roll" or "marks", order = "asc" or "desc"
    i = head
    while i is not None:
        j = i.next
        while j is not None:
            if by == "roll":
                a = i.roll
                b = j.roll
            else:
                a = i.marks
                b = j.marks

            if (order == "asc" and a > b) or (order == "desc" and a < b):
                # swap the data of the two nodes
                i.roll, j.roll = j.roll, i.roll
                i.name, j.name = j.name, i.name
                i.marks, j.marks = j.marks, i.marks
            j = j.next
        i = i.next
    print("Sorted by", by, "in", order, "order")


def display_students():
    if head is None:
        print("No records")
        return
    temp = head
    while temp is not None:
        print(temp.roll, temp.name, temp.marks)
        temp = temp.next
How to call them
add_student(102, "Amit", 78)
add_student(101, "Neha", 91)
add_student(103, "Ravi", 65)
display_students()

sort_students("marks", "desc")
display_students()

sort_students("roll", "asc")
display_students()

update_student(102, "Amit", 85)
search_student(102)
delete_student(101)
display_students()
Student added
Student added
Student added
102 Amit 78
101 Neha 91
103 Ravi 65
Sorted by marks in desc order
101 Neha 91
102 Amit 78
103 Ravi 65
Sorted by roll in asc order
101 Neha 91
102 Amit 78
103 Ravi 65
Student updated
Found: 102 Amit 85
Student deleted
102 Amit 85
103 Ravi 65
How it works

head points to the first node, and each node's next points to the following one. The last node's next is None.
Add goes to the end of the list. Delete changes the next link to skip the removed node.
Sort compares every pair of nodes and swaps their data when they are out of order. Use by for roll or marks, and order for asc or desc.

Complexity analysis (n = number of students)

Function	Time	Space
add_student	O(n)	O(1)
delete_student	O(n)	O(1)
update_student	O(n)	O(1)
search_student	O(n)	O(1)
sort_students	O(n²)	O(1)
display_students	O(n)	O(1)
Files hidden when shared

Here is Group C, Question 1 in the same simple style: a hash table of size 10, the division method (key % 10) as the hash function, and chaining for collisions. Each bucket is a list, and every key-value pair is stored in the bucket for its hash index. Keys are integers. A display_table function is included so you can see the chains.

python
# Group C - Problem 1: Hash Table using Division Method and Chaining

size = 10
table = []
for i in range(size):
    table.append([])           # each bucket is an empty list (the chain)


def hash_function(key):
    return key % size          # division method


def insert(key, value):
    index = hash_function(key)
    # if the key already exists, update its value
    for pair in table[index]:
        if pair[0] == key:
            pair[1] = value
            print("Key", key, "updated")
            return
    table[index].append([key, value])
    print("Inserted:", key, "->", value, "at index", index)


def search(key):
    index = hash_function(key)
    for pair in table[index]:
        if pair[0] == key:
            print("Found:", key, "->", pair[1])
            return
    print("Key", key, "not found")


def delete(key):
    index = hash_function(key)
    for i in range(len(table[index])):
        if table[index][i][0] == key:
            table[index].pop(i)
            print("Deleted key", key)
            return
    print("Key", key, "not found")


def display_table():
    for i in range(size):
        print(i, ":", table[i])

How to call them

python
insert(15, "Amit")
insert(25, "Neha")        # collision with 15 (both go to index 5)
insert(7, "Ravi")
insert(32, "Priya")
display_table()

search(25)
search(99)

delete(15)
display_table()

Sample output
Inserted: 15 -> Amit at index 5
Inserted: 25 -> Neha at index 5
Inserted: 7 -> Ravi at index 7
Inserted: 32 -> Priya at index 2
0 : []
1 : []
2 : [[32, 'Priya']]
3 : []
4 : []
5 : [[15, 'Amit'], [25, 'Neha']]
6 : []
7 : [[7, 'Ravi']]
8 : []
9 : []
Found: 25 -> Neha
Key 99 not found
Deleted key 15
0 : []
1 : []
2 : [[32, 'Priya']]
3 : []
4 : []
5 : [[25, 'Neha']]
6 : []
7 : [[7, 'Ravi']]
8 : []
9 : []
How it works

The hash function is key % 10, so every key maps to an index from 0 to 9.
Each index holds a list (the chain). When two keys land on the same index, like 15 and 25, both are stored in that list. This is chaining.
Search and delete compute the index first, then look only inside that one chain.

Complexity analysis (n = number of keys stored, size = 10)

Function	Average	Worst	Space
insert	O(1)	O(n)	O(1)
search	O(1)	O(n)	O(1)
delete	O(1)	O(n)	O(1)
display_table	O(size + n)	O(size + n)	O(1)

The worst case happens when all keys land in the same bucket, so one chain holds everything. The table itself takes O(size + n) space.

Files hidden when shared

Here is Problem Statement 10 in the same simple style: a fixed-size hash table, the division method key % table_size as the hash function, and linear probing for collisions. If the slot is taken, the program checks the next slot, wrapping around to the start, until it finds an empty one. A display_table function is included so you can see where each key lands.

python
# Group C - Problem 10: Hash Table using Division Method and Linear Probing

table_size = 10
table = [None] * table_size        # None means the slot is empty


def hash_function(key):
    return key % table_size        # division method


def insert(key):
    index = hash_function(key)
    start = index
    while table[index] is not None:
        if table[index] == key:
            print("Key", key, "already exists")
            return
        index = (index + 1) % table_size       # linear probing, wraps around
        if index == start:                     # came back to the start
            print("Hash table is full")
            return
    table[index] = key
    print("Inserted:", key, "at index", index)


def display_table():
    for i in range(table_size):
        print(i, ":", table[i])

How to call them

python
insert(15)
insert(25)         # collision with 15, goes to the next free slot
insert(35)         # collides again
insert(7)
insert(19)
insert(29)         # collision with 19, wraps around to index 0
display_table()

Sample output

Inserted: 15 at index 5
Inserted: 25 at index 6
Inserted: 35 at index 7
Inserted: 7 at index 8
Inserted: 19 at index 9
Inserted: 29 at index 0
0 : 29
1 : None
2 : None
3 : None
4 : None
5 : 15
6 : 25
7 : 35
8 : 7
9 : 19

Key 7 hashes to index 7, but that slot is already taken by 35, so linear probing moves it to index 8. Key 29 hashes to index 9, which holds 19, so it wraps around to index 0.

How it works

The hash function is key % table_size, so each key gets a starting index from 0 to 9.
If that slot is not empty, the program tries index + 1, then index + 2, and so on. The % table_size makes it wrap from the last slot back to slot 0.
If the probe returns to the starting index, every slot has been checked, so the table is full.

Complexity analysis (n = number of keys stored, table_size = 10)

Function	Average	Worst	Space
insert	O(1)	O(table_size)	O(1)
display_table	O(table_size)	O(table_size)	O(1)

The worst case happens when many keys cluster together, so insert must probe through most of the table. The table itself takes O(table_size) space.
Here is Problem Statement 11 in the same simple style. It builds on the previous program, so insert and display are included. Deleting a key in linear probing can break searches: if you just set the slot to empty, a search for a later key in the same probe chain stops at that gap and wrongly says "not found". To avoid this, a deleted slot is marked "DELETED" instead of being emptied. Search skips over "DELETED" slots and stops only at a truly empty slot.

python
# Group C - Problem 11: Search and Delete in Hash Table using Linear Probing

table_size = 10
table = [None] * table_size        # None means the slot was never used
DELETED = "DELETED"                # marks a slot whose key was removed


def hash_function(key):
    return key % table_size        # division method


def find(key):
    index = hash_function(key)
    for i in range(table_size):
        pos = (index + i) % table_size
        if table[pos] is None:     # empty slot: key cannot be further ahead
            return -1
        if table[pos] == key:
            return pos
    return -1


def insert(key):
    if find(key) != -1:
        print("Key", key, "already exists")
        return
    index = hash_function(key)
    for i in range(table_size):
        pos = (index + i) % table_size
        if table[pos] is None or table[pos] == DELETED:
            table[pos] = key
            print("Inserted:", key, "at index", pos)
            return
    print("Hash table is full")


def search(key):
    pos = find(key)
    if pos == -1:
        print("Key", key, "not found")
    else:
        print("Found:", key, "at index", pos)


def delete(key):
    pos = find(key)
    if pos == -1:
        print("Key", key, "not found")
    else:
        table[pos] = DELETED
        print("Deleted key", key, "from index", pos)


def display_table():
    for i in range(table_size):
        print(i, ":", table[i])

How to call them

python
insert(15)
insert(25)         # collides with 15, goes to index 6
insert(35)         # collides again, goes to index 7
insert(7)          # slot 7 is taken, goes to index 8

delete(25)         # index 6 becomes DELETED
display_table()

search(35)         # still found, even though 25 was deleted before it
search(99)
insert(45)         # reuses the DELETED slot at index 6

Sample output

Inserted: 15 at index 5
Inserted: 25 at index 6
Inserted: 35 at index 7
Inserted: 7 at index 8
Deleted key 25 from index 6
0 : None
1 : None
2 : None
3 : None
4 : None
5 : 15
6 : DELETED
7 : 35
8 : 7
9 : None
Found: 35 at index 7
Key 99 not found
Inserted: 45 at index 6

Key 35 hashes to index 5 and was placed at index 7 after probing past 15 and 25. After 25 is deleted, the search for 35 still works because it moves past the DELETED marker at index 6 and continues to index 7. If index 6 had been set to None, the search would have stopped there and missed 35.

How it works

find starts at key % table_size and checks the next slots one by one, wrapping around at the end.
It stops with "not found" only at a None slot, since a key can never be stored beyond a never-used slot in its probe chain. A DELETED slot does not stop it.
delete finds the key and marks that slot DELETED, so other keys in the chain stay reachable.
insert checks for a duplicate first, then uses the first None or DELETED slot it meets, so deleted space is reused.

Complexity analysis (table_size = 10)

Function	Average	Worst	Space
find	O(1)	O(table_size)	O(1)
insert	O(1)	O(table_size)	O(1)
search	O(1)	O(table_size)	O(1)
delete	O(1)	O(table_size)	O(1)
display_table	O(table_size)	O(table_size)	O(1)

The worst case happens when many keys cluster together, or when most slots are marked DELETED, so a lookup must probe through most of the table.

Files hidden when shared

Here is Problem Statement 12 in the same simple style. It combines everything from Problems 10 and 11 into one menu-driven program: division method hashing, linear probing, duplicate key handling, and table overflow handling. Deleted slots are marked "DELETED" so searches keep working after a deletion.

python
# Group C - Problem 12: Complete Hash Table Management System

table_size = 10
table = [None] * table_size        # None means the slot was never used
DELETED = "DELETED"                # marks a slot whose key was removed


def hash_function(key):
    return key % table_size        # division method


def find(key):
    index = hash_function(key)
    for i in range(table_size):
        pos = (index + i) % table_size
        if table[pos] is None:     # empty slot: key cannot be further ahead
            return -1
        if table[pos] == key:
            return pos
    return -1


def insert(key):
    if find(key) != -1:
        print("Duplicate key:", key, "already exists")
        return
    index = hash_function(key)
    for i in range(table_size):
        pos = (index + i) % table_size
        if table[pos] is None or table[pos] == DELETED:
            table[pos] = key
            print("Inserted:", key, "at index", pos)
            return
    print("Table overflow: no free slot for key", key)


def search(key):
    pos = find(key)
    if pos == -1:
        print("Key", key, "not found")
    else:
        print("Found:", key, "at index", pos)


def delete(key):
    pos = find(key)
    if pos == -1:
        print("Key", key, "not found")
    else:
        table[pos] = DELETED
        print("Deleted key", key, "from index", pos)


def display_table():
    for i in range(table_size):
        print(i, ":", table[i])


# Menu
while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        insert(key)
    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(key)
    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(key)
    elif choice == 4:
        display_table()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")

Sample run

1. Insert  2. Search  3. Delete  4. Display  5. Exit

Enter your choice: 1
Enter key to insert: 15
Inserted: 15 at index 5
Enter your choice: 1
Enter key to insert: 25
Inserted: 25 at index 6
Enter your choice: 1
Enter key to insert: 15
Duplicate key: 15 already exists
Enter your choice: 2
Enter key to search: 25
Found: 25 at index 6
Enter your choice: 3
Enter key to delete: 15
Deleted key 15 from index 5
Enter your choice: 2
Enter key to search: 25
Found: 25 at index 6
Enter your choice: 4
0 : None
1 : None
2 : None
3 : None
4 : None
5 : DELETED
6 : 25
7 : None
8 : None
9 : None
Enter your choice: 5
Exiting...

Table overflow looks like this when all 10 slots are filled and you insert another key:

Table overflow: no free slot for key 99

How it works

insert first calls find to reject duplicates, then uses the first None or DELETED slot along the probe path. If it checks all 10 slots without finding one, it reports overflow.
search and delete both use find, which stops only at a None slot, so a DELETED marker never hides a key that sits after it.
The menu loop keeps running until the user chooses Exit.

Complexity analysis (table_size = 10)

Function	Average	Worst	Space
find	O(1)	O(table_size)	O(1)
insert	O(1)	O(table_size)	O(1)
search	O(1)	O(table_size)	O(1)
delete	O(1)	O(table_size)	O(1)
display_table	O(table_size)	O(table_size)	O(1)

The worst case happens when keys cluster together or most slots are marked DELETED, so a lookup must probe through most of the table.

Files hidden when shared

Here is Problem Statement 13 in the same simple style. The graph is stored as an adjacency matrix, where matrix[i][j] = 1 means there is a route between location i and location j. The routes are two-way, so adding an edge sets both matrix[i][j] and matrix[j][i]. DFS starts from a given vertex (such as A), visits it, then goes deeper into an unvisited neighbour before backtracking.

python
# Group D - Problem 13: Graph using Adjacency Matrix and DFS

locations = ["A", "B", "C", "D", "E", "F"]
n = len(locations)

matrix = []
for i in range(n):
    matrix.append([0] * n)

visited = [False] * n


def get_index(name):
    for i in range(n):
        if locations[i] == name:
            return i
    return -1


def add_edge(u, v):
    i = get_index(u)
    j = get_index(v)
    if i == -1 or j == -1:
        print("Invalid location")
        return
    matrix[i][j] = 1
    matrix[j][i] = 1               # route works in both directions


def display_matrix():
    print("  ", end="")
    for name in locations:
        print(name, end=" ")
    print()
    for i in range(n):
        print(locations[i], end=" ")
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()


def dfs(v):
    visited[v] = True
    print(locations[v], end=" ")
    for j in range(n):
        if matrix[v][j] == 1 and not visited[j]:
            dfs(j)


def start_dfs(start):
    s = get_index(start)
    if s == -1:
        print("Invalid starting location")
        return
    for i in range(n):
        visited[i] = False
    print("DFS traversal from", start, ":", end=" ")
    dfs(s)
    print()

How to call them

python
add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "D")
add_edge("C", "E")
add_edge("D", "F")
add_edge("E", "F")

display_matrix()
start_dfs("A")

Sample output

  A B C D E F
A 0 1 1 0 0 0
B 1 0 0 1 0 0
C 1 0 0 0 1 0
D 0 1 0 0 0 1
E 0 0 1 0 0 1
F 0 0 0 1 1 0
DFS traversal from A : A B D F E C

How the DFS runs

Start at A and mark it visited. A's first unvisited neighbour is B, so go to B.
From B, the first unvisited neighbour is D. From D, go to F.
From F, D is already visited, so the next unvisited neighbour is E. From E, go to C.
C's only other neighbour is A, which is visited, so the search backtracks and ends.

The order is A, B, D, F, E, C. Neighbours are checked in the order of the matrix columns (A to F), so a different edge order or location order can give a different but still valid DFS sequence.

Complexity analysis (V = number of vertices)

Function	Time	Space
add_edge	O(V) (finding the indexes)	O(1)
display_matrix	O(V²)	O(1)
dfs / start_dfs	O(V²)	O(V) (visited list and recursion stack)

DFS takes O(V²) with an adjacency matrix because every vertex scans a full row of V entries to find its neighbours. The matrix itself uses O(V²) space.
Here is Problem Statement 14 in the same simple style. It uses the same city-area graph as Problem 13 (A to F with the same six routes), but stored as an adjacency list: each location has a list of its neighbours. BFS starts from a given vertex, visits it, then visits all its neighbours before going to the next level. A queue with front and rear keeps track of what to visit next.

python
# Group D - Problem 14: Graph using Adjacency List and BFS

locations = ["A", "B", "C", "D", "E", "F"]
n = len(locations)

adj_list = []
for i in range(n):
    adj_list.append([])            # each location has an empty neighbour list


def get_index(name):
    for i in range(n):
        if locations[i] == name:
            return i
    return -1


def add_edge(u, v):
    i = get_index(u)
    j = get_index(v)
    if i == -1 or j == -1:
        print("Invalid location")
        return
    adj_list[i].append(j)
    adj_list[j].append(i)          # route works in both directions


def display_list():
    for i in range(n):
        print(locations[i], "->", end=" ")
        for j in adj_list[i]:
            print(locations[j], end=" ")
        print()


def bfs(start):
    s = get_index(start)
    if s == -1:
        print("Invalid starting location")
        return

    visited = [False] * n
    queue = [None] * n             # each vertex enters the queue only once
    front = 0
    rear = -1

    rear = rear + 1                # enqueue the start vertex
    queue[rear] = s
    visited[s] = True

    print("BFS traversal from", start, ":", end=" ")
    while front <= rear:
        v = queue[front]           # dequeue
        front = front + 1
        print(locations[v], end=" ")
        for j in adj_list[v]:
            if not visited[j]:
                visited[j] = True
                rear = rear + 1    # enqueue the neighbour
                queue[rear] = j
    print()

How to call them

python
add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "D")
add_edge("C", "E")
add_edge("D", "F")
add_edge("E", "F")

display_list()
bfs("A")

Sample output

A -> B C 
B -> A D 
C -> A E 
D -> B F 
E -> C F 
F -> D E 
BFS traversal from A : A B C D E F

How the BFS runs

Start by putting A in the queue and marking it visited.
Remove A, print it, and add its unvisited neighbours B and C. Queue: B, C.
Remove B, print it, and add D. Queue: C, D.
Remove C, print it, and add E. Queue: D, E.
Remove D, print it, and add F. Queue: E, F.
Remove E, then F. Their neighbours are all visited, so the queue becomes empty and BFS ends.

The order is A, B, C, D, E, F. BFS visits all locations one step away from A (B, C) first, then two steps away (D, E), then three steps away (F).

Complexity analysis (V = number of vertices, E = number of edges)

Function	Time	Space
add_edge	O(V) (finding the indexes)	O(1)
display_list	O(V + E)	O(1)
bfs	O(V + E)	O(V) (visited list and queue)

BFS takes O(V + E) with an adjacency list because each vertex is removed from the queue once and each edge is checked a constant number of times. This is faster than the O(V²) DFS in Problem 13, which scanned a full matrix row for every vertex. The adjacency list itself uses O(V + E) space.
Here is the second Problem Statement 14 in the same simple style. It combines Problems 13 and 14: one city-area graph (A to F, same six routes) stored in both forms. add_edge fills the adjacency matrix and the adjacency list together. BFS uses the adjacency list with a queue (front and rear), and DFS uses the adjacency matrix.

python
# Group D - Problem 14: Comparison of BFS and DFS Traversals

locations = ["A", "B", "C", "D", "E", "F"]
n = len(locations)

# adjacency matrix (used for DFS)
matrix = []
for i in range(n):
    matrix.append([0] * n)

# adjacency list (used for BFS)
adj_list = []
for i in range(n):
    adj_list.append([])

visited = [False] * n


def get_index(name):
    for i in range(n):
        if locations[i] == name:
            return i
    return -1


def add_edge(u, v):
    i = get_index(u)
    j = get_index(v)
    if i == -1 or j == -1:
        print("Invalid location")
        return
    matrix[i][j] = 1               # matrix, both directions
    matrix[j][i] = 1
    adj_list[i].append(j)          # list, both directions
    adj_list[j].append(i)


def display_graph():
    print("Adjacency Matrix:")
    print("  ", end="")
    for name in locations:
        print(name, end=" ")
    print()
    for i in range(n):
        print(locations[i], end=" ")
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()

    print("Adjacency List:")
    for i in range(n):
        print(locations[i], "->", end=" ")
        for j in adj_list[i]:
            print(locations[j], end=" ")
        print()


def dfs(v):
    visited[v] = True
    print(locations[v], end=" ")
    for j in range(n):
        if matrix[v][j] == 1 and not visited[j]:
            dfs(j)


def start_dfs(start):
    s = get_index(start)
    if s == -1:
        print("Invalid starting location")
        return
    for i in range(n):
        visited[i] = False
    print("DFS traversal from", start, ":", end=" ")
    dfs(s)
    print()


def bfs(start):
    s = get_index(start)
    if s == -1:
        print("Invalid starting location")
        return

    seen = [False] * n
    queue = [None] * n
    front = 0
    rear = -1

    rear = rear + 1                # enqueue the start vertex
    queue[rear] = s
    seen[s] = True

    print("BFS traversal from", start, ":", end=" ")
    while front <= rear:
        v = queue[front]           # dequeue
        front = front + 1
        print(locations[v], end=" ")
        for j in adj_list[v]:
            if not seen[j]:
                seen[j] = True
                rear = rear + 1    # enqueue the neighbour
                queue[rear] = j
    print()

How to call them

python
add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "D")
add_edge("C", "E")
add_edge("D", "F")
add_edge("E", "F")

display_graph()
bfs("A")
start_dfs("A")

Sample output

Adjacency Matrix:
  A B C D E F
A 0 1 1 0 0 0
B 1 0 0 1 0 0
C 1 0 0 0 1 0
D 0 1 0 0 0 1
E 0 0 1 0 0 1
F 0 0 0 1 1 0
Adjacency List:
A -> B C 
B -> A D 
C -> A E 
D -> B F 
E -> C F 
F -> D E 
BFS traversal from A : A B C D E F
DFS traversal from A : A B D F E C

Comparison of BFS and DFS

Point	BFS	DFS
Visiting order	Level by level: all locations one step away, then two steps, and so on	Goes as deep as possible along one path, then backtracks
Data structure	Queue (first in, first out)	Stack (recursion uses the call stack)
Order here	A, B, C, D, E, F	A, B, D, F, E, C
Graph form used	Adjacency list	Adjacency matrix
Time	O(V + E)	O(V²) with a matrix (O(V + E) with a list)
Space	O(V) for the queue and visited list	O(V) for the recursion stack and visited list
Best used for	Shortest path in an unweighted graph, nearest locations first	Exploring all paths, checking connectivity, detecting cycles

Working principle in short

BFS finishes everything near the start before going farther. From A it visits B and C first, then D and E, then F.
DFS picks one neighbour and keeps going. From A it goes to B, then D, then F, then E, then C, and only backtracks when it has no unvisited neighbour left.

Complexity analysis (V = number of vertices, E = number of edges)

Function	Time	Space
add_edge	O(V) (finding the indexes)	O(1)
display_graph	O(V²)	O(1)
bfs	O(V + E)	O(V)
start_dfs / dfs	O(V²)	O(V)

The DFS is slower here only because of the matrix. The graph itself takes O(V²) space for the matrix plus O(V + E) for the list.
Here is Problem Statement 15 in the same simple style. A BST keeps smaller values in the left subtree and larger values in the right subtree. A small Node class is needed, as in the linked list problem. Duplicate values are ignored. Insert, inorder, preorder and postorder are separate user-defined functions.

python
# Group D - Problem 15: Insertion and Display in a Binary Search Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = None            # None means the tree is empty


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    else:
        print("Duplicate value", data, "ignored")
    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

How to call them

python
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    root = insert(root, value)

print("Inorder   :", end=" ")
inorder(root)
print()

print("Preorder  :", end=" ")
preorder(root)
print()

print("Postorder :", end=" ")
postorder(root)
print()

Sample run

Enter number of elements: 7
Enter element: 50
Enter element: 30
Enter element: 70
Enter element: 20
Enter element: 40
Enter element: 60
Enter element: 80
Inorder   : 20 30 40 50 60 70 80 
Preorder  : 50 30 20 40 70 60 80 
Postorder : 20 40 30 60 80 70 50

The tree built from this input looks like this:

        50
       /  \
     30    70
    /  \   / \
  20   40 60  80

How it works

insert compares the new value with the current node. It goes left if smaller, right if larger, and creates a new node when it reaches an empty spot.
Inorder (left, root, right) prints the values in ascending order, which is a useful check that the BST is correct.
Preorder (root, left, right) visits the root first. It is used to copy a tree.
Postorder (left, right, root) visits the root last. It is used to delete a tree.

Complexity analysis (n = number of nodes, h = height of the tree)

Function	Average (balanced)	Worst (skewed)	Space
insert	O(log n)	O(n)	O(h) (recursion stack)
inorder	O(n)	O(n)	O(h)
preorder	O(n)	O(n)	O(h)
postorder	O(n)	O(n)	O(h)

The worst case happens when values are inserted in sorted order (like 10, 20, 30, 40), because the tree becomes a straight line with height n. Building the whole tree from n values takes O(n log n) on average and O(n²) in the worst case. The tree itself takes O(n) space.

Files hidden when shared

Here is Problem Statement 16 in the same simple style. It builds on Problem 15, so Node, insert and inorder are included to build the tree and check the result. Search walks left or right by comparing values. Delete handles all three cases:

Leaf node: remove it by returning None.
One child: replace the node with its child.
Two children: copy the inorder successor (the smallest value in the right subtree) into the node, then delete that successor from the right subtree.
python
# Group D - Problem 16: Searching and Deletion in a Binary Search Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = None


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    else:
        print("Duplicate value", data, "ignored")
    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def search(root, key):
    if root is None:
        return False
    if key == root.data:
        return True
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)


def find_min(root):
    while root.left is not None:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        print("Value", key, "not found")
        return root

    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # Case 1: leaf node
        if root.left is None and root.right is None:
            print("Deleted leaf node", key)
            return None
        # Case 2: one child
        if root.left is None:
            print("Deleted node", key, "with one child")
            return root.right
        if root.right is None:
            print("Deleted node", key, "with one child")
            return root.left
        # Case 3: two children
        successor = find_min(root.right)
        print("Deleted node", key, "with two children, replaced by", successor.data)
        root.data = successor.data
        root.right = delete(root.right, successor.data)
    return root

How to call them

python
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    root = insert(root, v)

print("Inorder:", end=" ")
inorder(root)
print()

print("Search 60:", search(root, 60))
print("Search 99:", search(root, 99))

root = delete(root, 20)        # leaf node
root = delete(root, 30)        # one child
root = delete(root, 50)        # two children (the root)
root = delete(root, 99)        # not present

print("Inorder:", end=" ")
inorder(root)
print()

Sample output

Inorder: 20 30 40 50 60 70 80 
Search 60: True
Search 99: False
Deleted leaf node 20
Deleted node 30 with one child
Deleted node 50 with two children, replaced by 60
Value 99 not found
Inorder: 40 60 70 80

How the three deletions work on this tree

Start:       50            After 20:     50           After 30:     50
            /  \                        /  \                       /  \
          30    70                    30    70                   40    70
         /  \   / \                     \   / \                       / \
       20   40 60  80                   40 60  80                   60  80

After 50 (two children): the inorder successor is 60, the smallest value in the right subtree.
60 is copied into the root, and the old 60 node is deleted.

            60
           /  \
         40    70
                 \
                  80

How it works

search compares the key with the current node and goes left or right, so it never checks the other half of the tree.
Deleting a leaf just removes it. Deleting a node with one child connects its parent directly to that child.
Deleting a node with two children cannot simply remove it, because two subtrees would be left without a parent. Using the inorder successor keeps the BST order correct, since it is larger than everything on the left and smaller than everything else on the right.
The final inorder output stays sorted, which confirms the tree is still a valid BST.

Complexity analysis (n = number of nodes, h = height of the tree)

Function	Average (balanced)	Worst (skewed)	Space
search	O(log n)	O(n)	O(h) (recursion stack)
find_min	O(log n)	O(n)	O(1)
delete	O(log n)	O(n)	O(h)

The worst case happens when the tree is a straight line, so the height is n. The tree itself takes O(n) space.
Here is Problem Statement 17 in the same simple style. It combines Problems 15 and 16 into one menu-driven program: insert, delete, search and display. The display option shows all three traversals (inorder, preorder, postorder), and the tree is shown after every insert and delete so you can see the updated elements.

python
# Group D - Problem 17: Complete Binary Search Tree Management System

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = None            # None means the tree is empty


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    else:
        print("Duplicate value", data, "ignored")
    return root


def search(root, key):
    if root is None:
        return False
    if key == root.data:
        return True
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)


def find_min(root):
    while root.left is not None:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        print("Value", key, "not found")
        return root

    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # Case 1: leaf node
        if root.left is None and root.right is None:
            print("Deleted leaf node", key)
            return None
        # Case 2: one child
        if root.left is None:
            print("Deleted node", key, "with one child")
            return root.right
        if root.right is None:
            print("Deleted node", key, "with one child")
            return root.left
        # Case 3: two children
        successor = find_min(root.right)
        print("Deleted node", key, "with two children, replaced by", successor.data)
        root.data = successor.data
        root.right = delete(root.right, successor.data)
    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def display(root):
    if root is None:
        print("Tree is empty")
        return
    print("Inorder   :", end=" ")
    inorder(root)
    print()
    print("Preorder  :", end=" ")
    preorder(root)
    print()
    print("Postorder :", end=" ")
    postorder(root)
    print()


# Menu
while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter value to insert: "))
        root = insert(root, key)
        display(root)
    elif choice == 2:
        key = int(input("Enter value to delete: "))
        root = delete(root, key)
        display(root)
    elif choice == 3:
        key = int(input("Enter value to search: "))
        if search(root, key):
            print("Value", key, "found in the tree")
        else:
            print("Value", key, "not found in the tree")
    elif choice == 4:
        display(root)
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")

Sample run

1. Insert  2. Delete  3. Search  4. Display  5. Exit

Enter your choice: 1
Enter value to insert: 50
Inorder   : 50 
Preorder  : 50 
Postorder : 50 
Enter your choice: 1
Enter value to insert: 30
Inorder   : 30 50 
Preorder  : 50 30 
Postorder : 30 50 
Enter your choice: 1
Enter value to insert: 70
Inorder   : 30 50 70 
Preorder  : 50 30 70 
Postorder : 30 70 50 
Enter your choice: 1
Enter value to insert: 50
Duplicate value 50 ignored
Inorder   : 30 50 70 
Preorder  : 50 30 70 
Postorder : 30 70 50 
Enter your choice: 3
Enter value to search: 70
Value 70 found in the tree
Enter your choice: 2
Enter value to delete: 50
Deleted node 50 with two children, replaced by 70
Inorder   : 30 70 
Preorder  : 70 30 
Postorder : 30 70 
Enter your choice: 3
Enter value to search: 50
Value 50 not found in the tree
Enter your choice: 5
Exiting...

How it works

Insert and delete return the (possibly new) root, so the menu does root = insert(root, key) and root = delete(root, key). This matters when the root itself is deleted.
Delete handles all three cases: a leaf is removed, a node with one child is replaced by that child, and a node with two children takes the value of its inorder successor (the smallest value in the right subtree).
Display prints all three traversals. Inorder always gives sorted order, which is a quick check that the tree is still a valid BST.
Duplicates are ignored, and deleting a missing value prints "not found".

Complexity analysis (n = number of nodes, h = height of the tree)

Function	Average (balanced)	Worst (skewed)	Space
insert	O(log n)	O(n)	O(h)
search	O(log n)	O(n)	O(h)
delete	O(log n)	O(n)	O(h)
inorder / preorder / postorder / display	O(n)	O(n)	O(h)

The worst case happens when values are inserted in sorted order, because the tree becomes a straight line with height n.

