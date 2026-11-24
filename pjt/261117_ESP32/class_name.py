class Monster:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"나는 {self.name}, {self.age}살입니다.")
        
shark = Monster("상어",7)
shark.introduce()