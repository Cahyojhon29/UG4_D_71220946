def aritmatika(a, b, n):
    d = b    
    total = ((2 * a) + ((n - 1) * d)) * n / 2   
    return total

a = int(input("Masukkan nilai awal: "))
b = int(input("Masukkan selisih bilangan: "))
n = int(input("Masukkan banyaknya suku: "))

total = aritmatika(a, b, n)

print("Total dari deret aritmatika adalah", total)
