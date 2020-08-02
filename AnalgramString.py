T = int(input())
for x in range(T):
    cost1, cost2 = map(int, input().split())
    n = int(input())
    green = []
    purple = []
    totalCost1 = 0
    totalCost2 = 0

    for i in range(n):
        v1, v2 = map(int, input().split())
        green.append(v1)
        purple.append(v2)

    totalCost1 = green.count(1) * cost1 + purple.count(1) * cost2
    totalCost2 = green.count(1) * cost2 + purple.count(1) * cost1

    if totalCost1 < totalCost2:
        print(totalCost1)
    else:
        print(totalCost2)