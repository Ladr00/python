class cassa:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def top_up(self, donate):
        if donate > 0:
            self.balance += donate
            print(f"Пополнено на {donate} денег. Текущий баланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть положительной.")
    
    def count_1000(self):
        tmp = self.balance // 1000
        print(f"Количество целых тысяч в кассе: {tmp}")
    
    def take_away(self, donate):
        if donate <= self.balance:
            self.balance -= donate
            print(f"Взято {donate} денег. Текущий баланс: {self.balance}")
        else:
            raise ValueError("Недостаточно денег в кассе.")

money = cassa(5000)
money.top_up(3000)
money.count_1000()
money.take_away(2000)
try:
    money.take_away(7000)
except ValueError as e:
    print(e)
