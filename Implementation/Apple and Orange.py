s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
ap = 0
ora = 0
for x in apple:
    if x >= s - a and x <= t - a:
        ap = ap + 1
for y in orange:
    if -y >= b - t and -y <= b - s:
        ora = ora + 1
print(ap, ora, sep="\n")
