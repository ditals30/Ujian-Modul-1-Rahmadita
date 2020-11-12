
def move_zeros(list_angka, n): 
    count = 0
    for i in range(n): 
        if list_angka[i] != 0: 
            list_angka[count] = list_angka[i] 
            count+=1
    while count < n: 
        list_angka[count] = 0
        count += 1

list_angka = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9] 
n = len(list_angka)

print (f'MoveZeros from: {list_angka} ')

move_zeros(list_angka,n)

print(f'Result: {list_angka}') 
