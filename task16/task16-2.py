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
            raise ValueError("не может стать меньше или равно 1.")
    
    def count_moves(self, x2, y2):
        horizontal_distance = abs(x2 - self.x)
        vertical_distance = abs(y2 - self.y)
        
        if horizontal_distance % self.s == 0 and vertical_distance % self.s == 0:
            total_moves = horizontal_distance // self.s + vertical_distance // self.s
        else:
            total_moves = -1
        
        return total_moves

Turtle = Turtle(0, 0, 1)
Turtle.go_right()
Turtle.go_up()
Turtle.evolve()
print("Текущая позиция Черепашки:", Turtle.x, Turtle.y)
print("Количество клеточек за ход:", Turtle.s)
try:
    Turtle.degrade()
except ValueError as e:
    print(e)
print("Количество клеточек за ход после уменьшения:", Turtle.s)
moves_needed = Turtle.count_moves(5, 5)
if moves_needed == -1:
    print("Точка недостижима с текущим шагом.")
else:
    print("Минимальное количество действий до точки (5, 5):", moves_needed)
