if (i, j) in self.available:
            if self.turn == 2:
                # turn_value=False
                self.grid[i][j] = self.marker[1]
                self.status("Computer turn")
                self.available.remove((i, j))
                self.turn = 1
        if self.turn == 1:
            print('yes')
            best_score = -infinity
            for i in range(3):
                for j in range(3):
                    if self.grid[i][j] == "  ":
                        self.grid[i][j] = self.marker[2]
                        score = self.minimax(self.grid, 0, False)
                        self.grid[i][j] = '  '

                        if score > best_score:
                            best_score = score
                            a = (i, j)

            self.grid[a[0]][a[1]] = self.marker[2]
            # self.available.remove(a)
            self.status("Player1 turn")
            self.turn = 2