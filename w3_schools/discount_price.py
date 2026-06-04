# Read input
price = float(input())
discount_percent = int(input())
dis=price*discount_percent/100
fp=price-dis
print(f"Discount: {dis:.2f}")
print(f"Final price: {fp:.2f}")