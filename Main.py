import json
nama=[]
def add_task(macam):
    nama.append({"text": macam, "done": False})
    
def show_tasks():
    nomor = 1
    for i in nama:
        print(nomor, i["text"])
        nomor+=1
    
def complete_task(nomor): 
    nama[nomor-1]["done"] = True

def delete_task(nomor):
    del nama[nomor-1]
    
def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(nama, f)
        
def load_tasks():
    global nama
    with open("tasks.json", "r") as f:
        nama = json.load(f)

load_tasks()
save_tasks()

while True:
    print("1. Tambah")
    print("2. Lihat")
    print("3. Tandai Selesai")
    print("4. Hapus")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        teks = input("Masukkan nama task: ")
        add_task(teks)    
    elif pilihan == "2":
        show_tasks()
    elif pilihan == "3":
        angka_string = input("Nomor task yang mau ditandai selesai: ")
        angka_asli = int(angka_string)
        complete_task(angka_asli)
    elif pilihan == "4":
        angka_string = input("Nomor task yang mau dihapus: ")
        angka_asli = int(angka_string)
        delete_task(angka_asli)
    elif pilihan == "5":
        break
    save_tasks()