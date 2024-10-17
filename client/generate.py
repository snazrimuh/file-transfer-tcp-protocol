# Script to generate .txt files of different sizes
sizes = [10 * 1024, 100 * 1024, 1 * 1024 * 1024, 5 * 1024 * 1024]

for i, size in enumerate(sizes):
    with open(f'file_{i+1}.txt', 'w') as f:
        f.write('A' * size)
