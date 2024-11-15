class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = {i:set() for i in range(9)}
        columns = {i:set() for i in range(9)}
        boxes = {
            "00": set(),
            "01": set(),
            "02": set(),
            "10": set(),
            "11": set(),
            "12": set(),
            "20": set(),
            "21": set(),
            "22": set(),
        }

        for row in range(9):
            for column in range(9):
                value = board[row][column]
                if value.isdigit():
                    box = str(row//3) + str(column//3)
                    if value in rows[row] or \
                        value in columns[column] or \
                        value in boxes[box]:
                        return False
                    rows[row].add(value)
                    columns[column].add(value)
                    boxes[box].add(value)

        return True