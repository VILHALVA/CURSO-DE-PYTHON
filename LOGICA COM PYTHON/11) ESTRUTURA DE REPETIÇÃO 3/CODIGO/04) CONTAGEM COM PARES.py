from time import sleep

n = int(input("😎Digite valor:\n>>>"))
if n % 2 == 1:
    n -= 1
for c in range(n, 0, -2):
    print(f"🔔Regressiva:{c}")
    sleep(1)