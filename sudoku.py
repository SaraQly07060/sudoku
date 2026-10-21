
import copy

# جدول اولیه؛ صفر یعنی خانه خالی
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# نگهداری جدول اصلی برای تشخیص خانه های ثابت
original = copy.deepcopy(board)


# نمایش جدول
def show_board():
    print("\n" + "-" * 37)

    for i in range(9):
        for j in range(9):

            if j % 3 == 0:
                print("|", end=" ")

            if board[i][j] == 0:
                print(".", end=" ")
            else:
                print(board[i][j], end=" ")

        print("|")

        if (i + 1) % 3 == 0:
            print("-" * 37)


# بررسی قانونی بودن یک عدد
def is_valid(row, col, num):

    # بررسی سطر
    for j in range(9):
        if board[row][j] == num:
            return False

    # بررسی ستون
    for i in range(9):
        if board[i][col] == num:
            return False

    # پیدا کردن ابتدای مربع 3 در 3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    # بررسی مربع 3 در 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


# پیدا کردن اولین خانه خالی
def find_empty():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

    return None


# حل جدول با الگوریتم Backtracking
def solve():
    empty = find_empty()

    if empty is None:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(row, col, num):
            board[row][col] = num

            if solve():
                return True

            # بازگشت در صورت اشتباه بودن انتخاب
            board[row][col] = 0

    return False


# بررسی کامل بودن و صحت جدول
def is_complete():
    if find_empty() is not None:
        return False

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            board[i][j] = 0
            valid = is_valid(i, j, num)
            board[i][j] = num

            if not valid:
                return False

    return True


# شروع بازی
print("Welcome to Sudoku!")
print("Enter: row column number")
print("Example: 1 3 4")
print("Commands: q = quit, s = solve, c = clear")

while True:
    show_board()

    if is_complete():
        print("Congratulations! You solved Sudoku!")
        break

    command = input(
        "\nEnter your move: "
    ).strip().lower()

    if command == "q":
        print("Game ended.")
        break

    elif command == "s":
        if solve():
            show_board()
            print("Sudoku solved successfully!")
        else:
            print("No solution exists.")
        break

    elif command.startswith("c "):
        parts = command.split()

        if len(parts) != 3:
            print("Enter: c row column")
            continue

        try:
            row = int(parts[1]) - 1
            col = int(parts[2]) - 1
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if not (0 <= row < 9 and 0 <= col < 9):
            print("Row and column must be between 1 and 9.")
            continue

        if original[row][col] != 0:
            print("You cannot clear a fixed cell.")
        else:
            board[row][col] = 0

    else:
        parts = command.split()

        if len(parts) != 3:
            print("Enter exactly three values: row column number")
            continue

        try:
            row = int(parts[0]) - 1
            col = int(parts[1]) - 1
            num = int(parts[2])
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if not (0 <= row < 9 and 0 <= col < 9):
            print("Row and column must be between 1 and 9.")
            continue

        if not (1 <= num <= 9):
            print("Number must be between 1 and 9.")
            continue

        if original[row][col] != 0:
            print("This cell is fixed and cannot be changed.")
            continue

        if not is_valid(row, col, num):
            print("Invalid move! Number already exists.")
            continue

        board[row][col] = num
