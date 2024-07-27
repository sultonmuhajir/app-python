print("="*50 + "\n\nMengubah Jenis Case\n\n" + "="*50)
print("""
Jenis Case
1. Upper
2. Lower
3. Title
""")

jenis = input("Pilih jenis case (angka) : ")

if jenis in ["1","2","3"]:
   teks = input(f"\nMasukkan teks :\n")
   print()
   if jenis == "1":
      print("Hasil Uppercase :\n"+teks.upper())
   elif jenis == "2":
      print("Hasil Lowercase :\n"+teks.lower())
   elif jenis == "3":
      print("Hasil Titlecase :\n"+teks.title())

else:
   print("\nInput salah!")