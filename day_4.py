from copy import deepcopy


class BingoBoard:
    def __init__(self, board):
        self.rows = board
        self.columns = []

        # Set columns
        columns = list(map(list, zip(*board)))
        # print(columns)
        self.columns = columns
        self.already_has_bingo = False

    def __str__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self.rows)

    def check_bingo(self, number):
        for row in self.rows:
            if number in row:
                row.remove(number)

        for column in self.columns:
            if number in column:
                column.remove(number)

        # if any rows or columns are empty - BINGO
        if [] in self.rows or [] in self.columns:
            self.already_has_bingo = True
            return True
        return False

    def get_sum(self):
        return sum([sum(x) for x in self.rows])


def day_4_part_1(boards: list, numbers: list):
    bingo = False
    for number in numbers:
        for i, board in enumerate(boards):
            if board.check_bingo(number):
                bingo = True
                break
        if bingo:
            break

    print(i, number)
    # print(boards[i])
    # print(boards[i].get_sum())
    return boards[i].get_sum() * number


def day_4_part_2(boards: list, numbers: list):
    bingo_boards = 0
    i = 0
    for number in numbers:
        # print("Bingo boards", number, bingo_boards)
        if bingo_boards < len(boards):
            for i, board in enumerate(boards):
                if not board.already_has_bingo and board.check_bingo(number):
                    bingo_boards += 1
                    if bingo_boards == 100:
                        break
        if bingo_boards == 100:
            break

    # print(i, number)
    # print(boards[i])
    # print(boards[i].get_sum())
    return boards[i].get_sum() * number


def main():
    fileObj = open("day_4_input.txt", "r")
    lines = fileObj.readlines()

    numbers = [int(x) for x in lines[0].split(",")]
    # print(numbers)

    # Create Bingo Boards
    boards = []
    one_board = []
    for line in lines[2:]:
        if line == "\n":
            bingo = BingoBoard(one_board)
            boards.append(bingo)
            one_board = []
        else:
            one_board.append([int(x) for x in line.strip().split()])

    # Part 1
    final_score = day_4_part_1(deepcopy(boards), numbers)
    print("Final score: ", final_score)

    # # Part 2
    final_score_2 = day_4_part_2(deepcopy(boards), numbers)
    print("Final Score 2: ", final_score_2)

    fileObj.close()


if __name__ == "__main__":
    main()
