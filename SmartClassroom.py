readings = list(map(int, input().split()))

if len(readings) != 20:
    print("INVALID INPUT")
    exit()

if not all(10 <= value <= 200 for value in readings):
    print("INVALID INPUT")
    exit()

sensors = [[] for _ in range(5)]
for i in range(20):
    sensors[i % 5].append(readings[i])

averages = [round(sum(sensor) / 4) for sensor in sensors]

max_avg = max(averages)

if max_avg < 50:
    print("Energy consumption is optimal.")
else:
    for i in range(5):
        if averages[i] == max_avg:
            print(f"Sensor Number : {i + 1}")  
