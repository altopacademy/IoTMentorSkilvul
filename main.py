all_items = [
    {"item": "susu", "harga": 50000},
    {"item": "daging", "harga": 20000},
    {"item": "lampu", "harga": 15000},
    {"item": "masker", "harga": 25000},
    {"item": "apel", "harga": 30000}
]

promotional_items = [
    {"item": "susu", "harga": 50000},
    {"item": "masker", "harga": 25000}
]

def tampilkan_item_promosi():
    print("Selamat datang di Altop Supermarket!")
    print("Berikut ini adalah beberapa item promosi:")
    for item in promotional_items:
        print(f"{item['item']}: Rp.{item['harga']}")

def tampilkan_semua_item():
    print("Selamat datang di Altop Supermarket!")
    print("Berikut ini adalah semua item yang tersedia:")
    for item in all_items:
        print(f"{item['item']}: Rp.{item['harga']}")

def hitung_total_harga(items):
    total_harga = 0
    detail = []
    for item in items:
        for item_supermarket in all_items:
            if item['item'] == item_supermarket['item']:
                harga = item['jumlah'] * item_supermarket['harga']
                total_harga += harga
                detail.append(f"{item['jumlah']} {item['item']} -> Rp.{harga}")
                break
    return total_harga, detail

def masukkan_input_user(prompt, opsi):
    while True:
        print(prompt)
        pilihan = input().lower()
        if pilihan in opsi:
            return pilihan
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def masukkan_item_yang_dibeli():
    items = []
    while True:
        item = input("Masukkan nama item (atau 'selesai' untuk mengakhiri): ")
        if item == 'selesai':
            break
        jumlah = int(input("Masukkan jumlah: "))
        items.append({"item": item, "jumlah": jumlah})
    return items

def tampilkan_struk(total_harga, detail):
    print(f"\nTotal harga: Rp.{total_harga}")
    print("Detail:")
    for detail_item in detail:
        print(detail_item)

def simulasi_supermarket():
    tampilkan_item_promosi()
    pilihan_user = masukkan_input_user("Masukkan 'item promosi' atau 'semua item': ", ['item promosi', 'semua item'])

    if pilihan_user == 'item promosi':
        item_yang_dibeli = masukkan_item_yang_dibeli()
        total_harga, detail = hitung_total_harga(item_yang_dibeli)
        tampilkan_struk(total_harga, detail)
    else:
        tampilkan_semua_item()
        item_yang_dibeli = masukkan_item_yang_dibeli()
        total_harga, detail = hitung_total_harga(item_yang_dibeli)
        tampilkan_struk(total_harga, detail)

simulasi_supermarket()
