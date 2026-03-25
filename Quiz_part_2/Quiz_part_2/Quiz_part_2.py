#1
stock_count = int(input("how many itums are in stock"))

if stock_count == 0:
    print("out of stock")
elif stock_count <= 5:
    print("Low stock: reorder soon")
else:
    print("in stock")


#2
sum = 0
for i in range(2, 51, 2):
    sum = sum + i
print(sum)