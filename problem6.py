n = 0
for x in range(1, 101):
    n += x
n = n ** 2

m = 0
for y in range(1, 101):
    m += y ** 2

ans = n - m

if __name__ == "__main__":
    print(ans)
