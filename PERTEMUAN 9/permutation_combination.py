# Permutation and Combination
print ("NAMA: Nevillaz Sahrul B")
print ("NIM: 312510352")
print ("KELAS: TI25C5")

# Permutation Example no 1
print ("Permutasi Contoh no 1")
from itertools import permutations
perm = permutations([1,2,3])
for i in perm:
    print(i)

# Permutation Example no 2
print ("Permutasi Contoh no 2")
from itertools import permutations
perm = permutations([1,2,3], 2)
for i in perm:
    print(i)

# Combination Example no 1
print ("Kombinasi Contoh no 1")
from itertools import combinations
comb = combinations([1,2,3], 2)
for i in comb:
    print(i)

# Combination Example no 2
print ("Kombinasi Contoh no 2")
from itertools import combinations
comb = combinations([2,1,3], 2)
for i in comb:
    print(i)

# Combination with Loop
print ("Kombinasi dengan Pengulangan")
from itertools import combinations_with_replacement
comb = combinations_with_replacement([1,2,3], 2)
for i in comb:
    print(i)
    