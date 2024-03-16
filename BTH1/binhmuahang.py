import re

def check1(text):
    pattern1 = r"\d+\.?\d*% higher than in-store"
    match1 = re.search(pattern1, text)
    if match1:
        discount = float(match1.group().strip("% higher than in-store"))
        return discount
    return 0

def check2(text):
    pattern2 = r"\d+\.?\d*% lower than in-store"  
    match2 = re.search(pattern2, text)

    if match2:
        discount = float(match2.group().strip("% lower than in-store"))
        return discount
    return 0

price = list(map(int, input().split()))

comments = []
for _ in range(len(price)):
    comments.append(input())

money = int(input())

online_cost = 0
store_cost = 0
for i in range(len(comments)):

    discount1 = check1(comments[i])
    discount2 = check2(comments[i])

    if "lower than in-store" in comments[i] and "higher than in-store"  in comments[i]:
        online_cost += price[i] * (1 - discount1/100)
        store_cost += price[i] * (1 - discount2/100)
    elif "lower than in-store" in comments[i] and "higher than in-store" not in comments[i]:
        online_cost += price[i] * (1 - discount1/100)
        store_cost += price[i]
    elif "higher than in-store" in comments[i] and  "lower than in-store" not in comments[i]:
        online_cost += price[i]
        store_cost += price[i] * (1 - discount2/100)
    else:
        online_cost += price[i]
        store_cost += price[i]

if online_cost <= money or store_cost <= money:
    print("true")
else:
    print("false")