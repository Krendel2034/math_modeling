import time
import random
M = random.randint(0,100)
N = random.randint(0,100)
start_time = time.time()

for i in range(M):
    for j in range(N):
        print(f"Внешний цикл: {i}, внутренний цикл: {j}")
        time.sleep(1)
end_time = time.time()
total_time = end_time - start_time

print(f"Общее время работы: {total_time:.2f} секунд")