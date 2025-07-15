class LoserPrinter:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

loserprinter = [LoserPrinter(*input().split()) for _ in range(5)]

for loser in loserprinter:
    loser.score = int(loser.score)

sorted_loser = sorted(loserprinter, key=lambda x: x.score)
loser = sorted_loser[0]

print(loser.codename, end=' ')
print(loser.score, end=' ')





