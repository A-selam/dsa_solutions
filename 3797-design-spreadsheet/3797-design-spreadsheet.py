class Spreadsheet:
    def __init__(self, rows: int):
        self.grid = {}

    def setCell(self, cell: str, value: int) -> None:
        self.grid[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.grid:
            del self.grid[cell]

    def getValue(self, formula: str) -> int:
        def parseOperand(string):
            if string.isdigit():
                return int(string)
            return self.grid.get(string, 0)

        formula = formula[1:]
        left, right = formula.split("+")
        return parseOperand(left) + parseOperand(right)
