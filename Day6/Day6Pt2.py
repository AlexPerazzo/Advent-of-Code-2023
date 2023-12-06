time = 60808676
record = 601116315591300
count = 0

for i in range(time):
    if (i * (time - i)) > record:
        count += 1
    

print(count)