class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell(self, count):
        if count <= self.stock:
            self.stock = self.stock - count
            print(f"{self.name} {count}개 판매!")
        else:
            print(f"{self.name} 재고가 부족합니다!")

keyboard = Product("키보드", 10)
mouse = Product("마우스", 4)

keyboard.sell(3)
mouse.sell(5)

print(keyboard.stock)
print(mouse.stock)