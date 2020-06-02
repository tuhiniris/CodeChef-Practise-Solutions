t = int(input())
knapsack = 30

piece = []
profit = []
profitperkg = []
profitoriginal = []


def profitratio(a, b):
    c = (a / b)
    profitperkg.append(c)


for i in range(t):
    a, b = map(int, (input().split()))
    piece.append(a)
    profit.append(b)
    profitratio(a, b)

print("Items Quantity : ", (piece))
print("Profit : ", (profit))
print("Profit Per Kg : ", (profitperkg))
print("")

profitoriginal.extend(profitperkg)
print("Profit List to check : ", profitoriginal)
print("")

profitperkg.sort(reverse=True)
print("Sorted Profits : ", profitperkg)
print("")


profitnow = []
weightnow = []

for i in range(len(piece)):

    greedy = (profitperkg[0])

    Ai = (((profitoriginal.index(greedy))))
    print(Ai)
    print(piece[Ai])

    # updated knapsack value

    remweight = (knapsack - (piece[Ai]))
    currprof = (profit[Ai])
    print("The remaining weight of knapsack is : ", remweight, "out of", knapsack, "KG.")
    print("Current Profit is", currprof * (piece[Ai]))
    print("")


    profitperkg.pop(Ai)
    print(profitperkg)


