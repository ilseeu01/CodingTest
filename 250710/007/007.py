class Spy:
    def __init__ (self, code, point, time):
        self.code = code
        self.point = point
        self.time = time
    
code, point, time = input().split()
spy1 = Spy(code, point, time)

print(f"secret code : {spy1.code}")
print(f"meeting point : {spy1.point}")
print(f"time : {spy1.time}")