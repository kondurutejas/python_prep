# Read input
item = input().strip()
price = float(input())
quantity = int(input())
total=price*quantity
print(f"Item: {item}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ${total:.2f}")