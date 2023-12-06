times = [60, 80, 86, 76]
records = [601, 1163, 1559, 1300]
total_counts = []

for i in range(len(times)):
    count = 0
    for j in range(times[i]):
        if (j * (times[i] - j)) > records[i]:
            count += 1
    
    total_counts.append(count)

print(total_counts[0] * total_counts[1] * total_counts[2] * total_counts[3])