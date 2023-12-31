import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells) == self.count:
            return set(self.cells)
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count == 0:
            return set(self.cells)
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell not in self.cells or self.count <= 0:
            return None
        self.cells.remove(cell)
        self.count -= 1
        return None

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell not in self.cells:
            return None
        self.cells.remove(cell)
        return None


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def mark_knowledge(self):
        curmines = set()
        cursafes = set()
        for sentence in self.knowledge:
            for pre in sentence.known_mines():
                curmines.add(pre)  
            for pre in sentence.known_safes():
                cursafes.add(pre)

        for safecell in self.safes:
            cursafes.add(safecell)
        for safecell in cursafes:
            self.mark_safe(safecell)

        for minecell in curmines:
            self.mark_mine(minecell)
        
        for mine in curmines:
            if type(mine) == int:
                continue
            addset = set(mine)
            self.knowledge.append(Sentence(addset, 1))
        self.knowledge.append(Sentence(cursafes, 0))

    def update_knowledge(self):
        print("updating")
        for sentence0 in self.knowledge:
            for sentence1 in self.knowledge:
                if sentence0 != sentence1:
                    if sentence1.cells.issubset(sentence0.cells):
                        preadd = Sentence(sentence0.cells-sentence1.cells, sentence0.count-sentence1.count)
                        if preadd not in self.knowledge:
                            self.knowledge.append(preadd)
        for sentence0 in self.knowledge:
            if not len(sentence0.cells):
                self.knowledge.remove(sentence0)
        print(f"updated.\nknowledge base size is {len(self.knowledge)}")

    def printf(self):
        path = "output.txt"
        f = open(path, 'a')
        print("-*", "-"*100, "*-", file=f)
        for sentence0 in self.knowledge:
            print(sentence0, file=f)
        print(file=f)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        self.moves_made.add(cell)
        self.mark_safe(cell)

        cells = set()
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                if 0 <= i <self.height and 0 <= j < self.width and (i, j) != cell and (i, j) not in self.mines:
                    cells.add((i, j))
                if (i, j) in self.mines:
                    count -= 1

        newinfo = Sentence(cells, count)
        self.knowledge.append(newinfo)
        self.mark_knowledge()
        self.update_knowledge()
        self.printf()
        

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        movealbe = self.safes-self.moves_made
        if len(movealbe) == 0:
            return None
        ret = random.choice(list(movealbe))
        print(f"Current safes {movealbe}")
        print(f"Current mines {self.mines}")
        print(f"AI moved {ret}")        
        return ret

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        movealbe = []
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) not in self.mines and (i, j) not in self.moves_made:
                    movealbe.append((i, j))

        if len(movealbe) == 0:
            return None
        ret = random.choice(list(movealbe))
        print(f"Current safes {self.safes}")
        print(f"Current mines {self.mines}")
        print(f"AI moved {ret}") 
        return ret
        