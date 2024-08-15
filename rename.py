print("="*50 + "\n\nMengubah Nama File Otomatis\n\n" + "="*50)
print()


def rename_file(nama_folder, nama_file):
   from os import listdir, path, rename
   from natsort import natsorted
   with open(f"./{nama_file}.txt", "r") as file:
      nama_baru_list = file.read().splitlines()
   files = listdir(f"./{nama_folder}")
   files = natsorted(files)
   for i, filename in enumerate(files):
      ext = path.splitext(filename)[1]
      old_file = path.join(f"./{nama_folder}", filename)
      new_file = path.join(f"./{nama_folder}", nama_baru_list[i] + ext)
      rename(old_file, new_file)
   print(f"\nBerhasil!\nSemua file berhasil diubah namanya.")


try:
   nama_folder = input("Masukkan nama folder : ")
   nama_file = input("Masukkan nama file : ")
   rename_file(nama_folder, nama_file)
except:
   print("\nTerjadi Kesalahan!")