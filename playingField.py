class PlayingField:
    column_not_possible_message = "<><><><><><><><><><>\n" \
                                  "COLUMN NOT POSSIBLE!\n" \
                                  "<><><><><><><><><><>"

    def __init__(self):
        self.height = 6
        self.width = 7
        self.playing_field = [[0 for x in range(self.width)] for y in range(self.height)]

    def __str__(self):
        s = "1 2 3 4 5 6 7 \n" \
            "------------- \n"
        for y in range(self.height):
            for x in range(self.width):
                s += str(self.playing_field[y][x])
                s += ' '
            s += '\n'
        return s

    def make_move(self, column, player):
        if column > self.width:
            print(self.column_not_possible_message)
            return -1
        column -= 1
        pin_placeable = False

        for row in range(self.height - 1, -1, -1):
            if self.playing_field[row][column] == 0:
                pin_placeable = True
                break

        if not pin_placeable:
            print(self.column_not_possible_message)
            return -1

        self.playing_field[row][column] = player

        if self.check_for_win(column, row, player):
            return 2

        return 1

    def check_for_win(self, x, y, player):
        # left
        for i in range(4):
            if x - 3 + i < 0 or x + 1 + i > self.width:
                continue
            else:
                if self.playing_field[y][x + i] == player and \
                        self.playing_field[y][x - 1 + i] == player and \
                        self.playing_field[y][x - 2 + i] == player and \
                        self.playing_field[y][x - 3 + i] == player:
                    return True

        # down
        if y + 3 < self.height:
            if self.playing_field[y][x] == player and \
                    self.playing_field[y + 1][x] == player and \
                    self.playing_field[y + 2][x] == player and \
                    self.playing_field[y + 3][x] == player:
                return True

        # up and left
        for i in range(4):
            if x - 3 + i < 0 or y - 3 + i < 0 or x + 1 + i > self.width or y + 1 + i > self.height:
                continue
            else:
                if self.playing_field[y + i][x + i] == player and \
                        self.playing_field[y - 1 + i][x - 1 + i] == player and \
                        self.playing_field[y - 2 + i][x - 2 + i] == player and \
                        self.playing_field[y - 3 + i][x - 3 + i] == player:
                    return True

        # up and right
        for i in range(4):
            if x + 3 - i >= self.width or y - 3 + i < 0 or x - i < 0 or y + 1 + i > self.height:
                continue
            else:
                if self.playing_field[y + i][x - i] == player and \
                        self.playing_field[y - 1 + i][x + 1 - i] == player and \
                        self.playing_field[y - 2 + i][x + 2 - i] == player and \
                        self.playing_field[y - 3 + i][x + 3 - i] == player:
                    return True

        return False
