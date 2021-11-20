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
elif b > a and a > c and c > d:
    print(f"{b},{a},{c},{d}")
elif b > a and a > d and d > c:
    print(f"{b},{a},{d},{c}")
elif b > c and c > d and d > a:
    print(f"{b},{c},{d},{a}")
elif b > c and c > a and a > d:
    print(f"{b},{c},{a},{d}")
elif b > d and d > a and a > c:
    print(f"{b},{d},{a},{c}")
elif b > d and d > c and c > a:
    print(f"{b},{d},{c},{a}")
elif c > a and a > b and b > d:
    print(f"{c},{a},{b},{d}")
elif c > a and a > d and d > b:
    print(f"{c},{a},{d},{b}")
elif c > b and b > a and a > d:
    print(f"{c},{b},{a},{d}")
elif c > b and b > d and d > a:
    print(f"{c},{b},{d},{a}")
elif c > d and d > a and a > b:
    print(f"{c},{d},{a},{b}")
elif c > d and d > b and b > a:
    print(f"{c},{d},{b},{a}")

