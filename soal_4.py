berat_badan = int(input("Masukan Berat Badan : "))
tinggi_badan = float(input("Masukan Tinggi Badan : "))
bmi = berat_badan / tinggi_badan
print(f"Berat Badan :{berat_badan}Kg")
print(f"Tinggi Badan : {tinggi_badan}M")
print(f"Nilai BMI anda : {bmi}")
if bmi < 18.5 :
    print("Berat Badan kurang")
elif 18.5 <= bmi < 24.9:
    print("Berat Badan kurang")
elif 25 <= bmi < 29.9:
    print("Kelebihan Berat Badan")
elif bmi / 30:
    print("Obesitas")
else : 
    print("berat badan anda normal")