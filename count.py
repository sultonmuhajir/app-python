print("="*50 + "\n\nMenghitung Jumlah Pada Teks\n\n" + "="*50)
print()


teks = input("Masukkan teks :\n")

karakter = len(list(teks))
kata = len([i for i in teks.split(" ") if i != ""])
kalimat = len([i for i in teks.split(".") if i != ""])


print(f"""
Jumlah karakter : {karakter}
Jumlah kata : {kata}
Jumlah kalimat : {kalimat}""")