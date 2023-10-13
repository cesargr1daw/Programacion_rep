"""
1. Calcula la traza para del siguiente programa para calcular cuánto vale suma:
sumaIt= 0
sumaTotal = 0
for i in range(1,4):
for j in range(3, 0, -1):
sumaIt = i*10+j
suma = suma + sumaIt
print(suma)
"""
|      i      |      j      | sumaIt | suma   |
|-------------|-------------|--------|------- |
|             |             |        | 0      |
| 1           | 3           | 13     | 13     |
| 1           | 2           | 12     | 25     |
| 1           | 1           | 11     | 36     |
| 2           | 3           | 23     | 59     |
| 2           | 2           | 22     | 81     |
| 2           | 1           | 21     | 102    |
| 3           | 3           | 33     | 135    |
| 3           | 2           | 32     | 167    |
| 3           | 1           | 31     | 198    |
