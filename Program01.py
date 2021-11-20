a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b and b > c and c > d:
    print(f"{a},{b},{c},{d}")

elif a > b and b > d and d > c:
    print(f"{a},{b},{d},{c}")

elif a > c and c > d and d > b:
    print(f"{a},{c},{d},{b}")

elif a > c and c > b and b > d:
    print(f"{a},{c},{b},{d}")

elif a > d and d > b and b > c:
    print(f"{a},{d},{b},{c}")

elif a > d and d > c and c > b:
    print(f"{a},{d},{c},{b}")
