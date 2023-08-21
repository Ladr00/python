class Turtle:
    def __init__(self, initial_x=0, initial_y=0, initial_s=1):
        self.x = initial_x
        self.y = initial_y
        self.s = initial_s
    
    def go_up(self):
        self.y += self.s
    
    def go_down(self):
        self.y -= self.s
    
    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
    
    def evolve(self):
        self.s += 1
    
    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("s не может стать меньше или равно 1.")
    
    def count_moves(self, x2, y2):
        horizontal_moves = abs(x2 - self.x) // self.s
        vertical_moves = abs(y2 - self.y) // self.s
        total_moves = horizontal_moves + vertical_moves
        return total_moves

turtle = Turtle(0, 0, 2)
turtle.go_right()
turtle.go_up()
turtle.evolve()
print("Текущая позиция черепашки:", turtle.x, turtle.y)
print("Количество клеточек за ход:", turtle.s)
turtle.degrade()
print("Количество клеточек за ход после уменьшения:", turtle.s)
moves_needed = turtle.count_moves(6, 4)
print("Минимальное количество действий до точки (6, 4):", moves_needed)
