def calculate_tip(bill, tip_percent):
  tip=bill*(tip_percent/100)
  total=bill+tip
  print(f"Bill: ${bill:.2f}")
  print(f"Tip: ${tip:.2f}")
  print(f"Total: ${total:.2f}")

# Read input
bill = float(input())
tip_percent = int(input())

calculate_tip(bill, tip_percent)
