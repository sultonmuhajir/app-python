print("="*50 + "\n\nMenghitung Jumlah Kata\n\n" + "="*50)
print()


teks = input("Masukkan teks :\n")
arr = [i for i in teks.split(" ") if i != ""]

print()
print(f"Jumlah kata : {len(arr)}")