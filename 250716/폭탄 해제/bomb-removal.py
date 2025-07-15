class BombDefuser:
    def __init__ (self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

bombdefuser = [BombDefuser(*input().split()) for _ in range(1)]
for time in bombdefuser:
    time.second = int(time.second)
bomb = bombdefuser[0]

print("code :", bomb.code)
print("color :", bomb.color)
print("second :", bomb.second)