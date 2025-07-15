class Forcast:
    def __init__(self, day, weekday, weather):
        self.day = day
        self.weekday = weekday
        self.weather = weather

n = int(input())
forcast = []
for i in range(n):
    day, weekday, weather = input().split()
    if weather == "Rain":
        forcast.append(Forcast(day, weekday, weather))

sorted_forcast = sorted(forcast, key=lambda x: x.day)
#메모리에 저장하지 않고 rain인 경우에만 메모리에 저장하는 게 좋지 않나?

res = sorted_forcast[0]
print(res.day, res.weekday, res.weather)



