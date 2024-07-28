print("="*50 + "\n\nKonversi File Spreadsheet\n\n" + "="*50)
print("""
Jenis Konversi
1. Excel ke Csv
2. Csv ke Excel
""")


def encod(data):
   from chardet import detect
   with open(data, 'rb') as file:
      return detect(file.read())['encoding']
   

def convert(jenis, hasil):
   nama_file = input(f"Nama file {jenis} : ")
   if jenis == "xlsx":
      nama_sheet = input("Nama sheet (opsional) : ") or 0
      df = pd.read_excel(f"./{nama_file}.xlsx", sheet_name=nama_sheet)
      df.to_csv(f"./{nama_file}.csv", index=False)
   else:
      encoding = encod(f"./{nama_file}.csv")
      df = pd.read_csv(f"./{nama_file}.csv", encoding=encoding)
      df.to_excel(f"./{nama_file}.xlsx", index=False)
   print(f"\nBerhasil!\nFile {hasil} bisa diakses di ./{nama_file}.{hasil}")


import pandas as pd
jenis = input("Pilih jenis konversi (angka) : ")
print()
try:
   if jenis == "1": convert("xlsx", "csv")
   elif jenis == "2": convert("csv", "xlsx")
   else: print("Input salah!")
except:
   print("\nFile tidak ditemukan!")