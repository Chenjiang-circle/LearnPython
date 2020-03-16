times = input().split()
C1 = int(times[0])
C2 = int(times[1])

time = round((C2 - C1) / 100)
second = 0
minute = 0
hour = 0

second = time % 60
time = time // 60
minute = time % 60
hour = time // 60

print("{:0>2}:{:0>2}:{:0>2}".format(hour, minute, second))
