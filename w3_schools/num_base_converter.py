num_str = input().strip()
src_base = int(input())
src_base = int(input())
decimal = 0
for digit in num:
    decimal=decimal*src_base+int(digit)
if(decimal == 0):
    print(0)
else:
    result = ""
    while decimal > 0:
        result = str(decimal % target_base) + result
        decimal //= target_base
    print(result)