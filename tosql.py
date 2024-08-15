print("="*50 + "\n\nKonversi Spreadsheet ke Sql\n\n" + "="*50)
print("""
Format Spreadsheet
1. Excel
2. Csv
""")


def encod(data):
   from chardet import detect
   with open(data, 'rb') as file:
      return detect(file.read())['encoding']
   
   
def to_sql(df, table):
   df = df.replace('"', "'", regex=True)
   arr = []
   for index, row in df.iterrows():
      col = ['_'.join(i.lower().split(' ')) for i in df.columns]
      values = ', '.join([f'"{str(value)}"' for value in row.values])
      query = f"INSERT INTO {table} ({', '.join(col)}) VALUES ({values});"
      arr.append(query)
   with open(f"{table}.sql", "w", errors="replace") as file:
      for value in arr: file.write(value + "\n")
   print(f"\nBerhasil!\nFile sql bisa diakses di ./{table}.sql")


import pandas as pd
format_file = input("Pilih format (angka) : ")
print()

try:
   if format_file == "1":
      nama_file = input("Nama file excel : ")
      nama_sheet = input("Nama sheet (opsional) : ") or 0
      df = pd.read_excel(f"./{nama_file}.xlsx", sheet_name=nama_sheet)
      to_sql(df, nama_file)

   elif format_file == "2":
      nama_file = input("Nama file csv : ")
      encoding = encod(f"./{nama_file}.csv")
      df = pd.read_csv(f"./{nama_file}.csv", encoding=encoding)
      to_sql(df, nama_file)

   else:
      print("Input salah!")

except:
   print("\nFile tidak ditemukan!")