class Address:
    def __init__(self, name, code, region):
        self.name = name
        self.code = code
        self.region = region

n = int(input())
addr = [Address(*input().split()) for _ in range(n)]

sorted_addr = sorted(addr, key=lambda x: x.name, reverse=True)
res = sorted_addr[0]
print(f"name {res.name}")
print(f"addr {res.code}")
print(f"city {res.region}")