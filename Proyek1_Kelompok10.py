# Katalog produk: [kode, nama, harga, stok]
# Indeks: 0 = kode, 1 = jenis, 2 = harga, 3 = stok
# item = [ ["kode", "jenis", harga,stok] , jumlah ]
vending_machine = "on"
import time

while vending_machine == "on":
    katalog = [
        ["A1", "Air Mineral", 4000, 10],
        ["A2", "Teh Botol", 6000, 10],
        ["B1", "Keripik Kentang", 10000, 10],
        ["B2", "Keripik Pedas", 8000, 10],
        ["C1", "Kopi Kaleng", 9000, 10],
        ["C2", "Soda", 8000, 10],
        ["D1", "Snack bar", 12000, 10],
        ["D2", "Biskuit Gandum", 10000, 10],
        ["E1", "Cokelat", 15000, 10],
        ["E2", "Permen", 5000, 10],
    ]
    sisa_stok = 0
    for produk in katalog:
        sisa_stok = sisa_stok + produk[3]

    while sisa_stok > 0:
        total = 0 
        keranjang = [] 
        
        print("==================================================")
        print(" SELAMAT DATANG DI VENDING MACHINE")
        print("==================================================")
        print("Kode | Nama Produk | Harga | Stok")
        print("--------------------------------------------------")
        for produk in katalog:
            stok = produk[3]
            if stok == 0:
                stok = "HABIS"
            print(produk[0], "|", produk[1], "| Rp", produk[2], "|", stok)
        print("--------------------------------------------------")

        tambah = "ya"                                                            # asumsikan di awal "tambah = y"
        while tambah == "ya":                                                    # masih berjalan selagi "ingin menambah produk = y"
            kode = input("Masukkan kode produk: ")
            produk_dipilih = None                                               # inisialisasi produk dipilih belum ada
            for produk in katalog:
                if produk[0] == kode:
                    produk_dipilih = produk
            if produk_dipilih == None:                                          # kalau kode tidak sesuai
                print("Kode tidak valid.")
            else:
                jumlah = int(input("Masukkan jumlah pembelian: "))
                if jumlah > 0 and jumlah <= produk_dipilih[3]:
                    keranjang.append([produk_dipilih, jumlah])                  # input ke array keranjang
                    print("Produk berhasil ditambahkan.")
                    tambah = input("Ingin menambah produk? (ya/tidak): ")
                else:
                    print("Jumlah tidak valid atau stok tidak cukup. Pilih produk lain.")
            

        for item in keranjang:
            total = total + (item[0][2] * item[1])                              # item[0][2] itu harga produk, item [1] jumlah yang mau di beli (kayak di baris 3)

        print("Total belanja: Rp", total)

        # data_member = [Kode member, Nama]
        # data_voucher = [kode voucher, minimal belanja, diskon]
        data_member = [ ["001", "Andi"], ["002", "Budi"], ["003", "Ciko"] ]
        data_voucher = [
            ["HEMAT2", 10000, 2000],
            ["HEMAT5", 20000, 5000],
            ["HEMAT10", 50000, 10000]
        ]

        # deklarasi awal
        status_member = "GUEST"
        member_ditemukan = False
        tawarkan_daftar = False

        kode_input = input("Masukkan kode member Anda (Klik enter jika bukan member): ") #input data member dari pengguna

        if kode_input != "":                                                    # kalau input bukan kosong/enter, maka dicari datanya
            for member in data_member:
                if member[0] == kode_input:                                     # ambil data dari array member
                    member_ditemukan = True
                    print(f"Halo, {member[1]}")                                 # ngikut struktur array 0 kode membernya 1 namanya
                    status_member = "MEMBER"
            if member_ditemukan == False:
                print("Kode member tidak terdaftar")
                tawarkan_daftar = True                                          # karena tidak punya member maka akan diarahkan untuk mendaftar member
        else:
            tawarkan_daftar = True # tidak punya member

        if tawarkan_daftar:
            mendaftar = input("Apakah Anda ingin mendaftar member baru sekarang? (ya/tidak): ")
            if mendaftar == "ya":
                nama_baru = input ("Masukkan nama: ")
                kode_baru = str(len(data_member) + 1).zfill(3)                  # kode baru 004, 005, dst
                data_member = data_member + [[kode_baru, nama_baru]]
                status_member = "MEMBER"
                print(f"Pendaftaran berhasil! Kode Member Anda: {kode_baru}")
                print(f"Halo, {nama_baru}")

        diskon_member = 0

        if status_member == "MEMBER":
            diskon_member = total * 5 / 100

        total_member = total - diskon_member

        diskon_voucher = 0

        kode_voucher = input("Masukkan kode voucher (Enter jika tidak ada): ")

        while kode_voucher != "":                              # hanya dicek kalau pengguna mengetik sesuatu
            voucher_dipilih = None
            for voucher in data_voucher:
                if voucher[0] == kode_voucher:
                    voucher_dipilih = voucher
            if voucher_dipilih == None:
                print("Kode voucher tidak valid.")
                kode_voucher = input("Masukkan kode voucher (Enter jika tidak ada): ")
            else:
                if total_member >= voucher_dipilih[1]:
                    diskon_voucher = voucher_dipilih[2]
                    print("Voucher berhasil dipakai.")
                    kode_voucher = "" 
                else:
                    print("Minimal belanja untuk voucher belum terpenuhi.")
                    kode_voucher = input("Masukkan kode voucher (Enter jika tidak ada): ")

        diskon = int(diskon_member + diskon_voucher)
        total_akhir = total - diskon

        def rupiah(angka):
            return "Rp " + f"{angka:,.0f}".replace(",", ".")
        total = 0
        for item in keranjang:
            nama_produk = item[0][1]
            jumlah_beli = item[1]
            harga_satuan = item[0][2]
            subtotal = harga_satuan * jumlah_beli
            total += subtotal
            print(f"{nama_produk} x {jumlah_beli} : {rupiah(subtotal)}")
        print("Total:", rupiah(total))
        print("-" * 30)
        print(f"Diskon : {rupiah(diskon)}")
        print("Total akhir:", rupiah(total_akhir))
        print("Silahkan lakukan pembayaran")

        from inputimeout import inputimeout, TimeoutOccurred
        import time

        print("Silakan Lakukan Pembayaran")
        Pembayaran_Sukses = False
        total_terbayar = 0
        while not Pembayaran_Sukses:
            try:
                BB_input = inputimeout (prompt="Scan QRIS di sini: ", timeout=60)
                total_terbayar += int(BB_input)
                if (total_terbayar == total_akhir):
                    ST = 1
                    print ("Pembayaran Berhasil!")
                    Pembayaran_Sukses = True
                elif (total_terbayar < total_akhir):
                    ST = 0
                    sisa_bayar = total_akhir - total_terbayar
                    print (f"Uang yang Anda bayarkan tidak sesuai dengan nominal total belanja, Anda harus melakukan pembayaran tambahan sebesar Rp{sisa_bayar}")
            except TimeoutOccurred:
                keranjang.clear()
                ST = 0
                Pembayaran_Sukses = True
                print("Transaksi dibatalkan karena waktu habis. \n Anda akan dialihkan ke tampilan awal")
                time.sleep(5)

        #Menampilkan struk pembelanjaan
        if ST == 1:
            print("\n===== STRUK PEMBELIAN =====")
            total_struk = 0 
            for item in keranjang: 
                nama = item[0][1]
                jumlah = item[1] 
                subtotal = item[0][2] * jumlah
                total_struk += subtotal 
                print(f"{nama} x{jumlah} = {rupiah(subtotal)}")
            print("-" * 30) 
            print("Total: ", rupiah(total_struk))
            print(f"Diskon : {rupiah(diskon)}")
            print("Total akhir:", rupiah(total_akhir)) 

            for item in keranjang:  #Kurangi stok sesuai jumlah yang dibeli
                item[0][3] = item[0][3] - item[1]

            import time
            time.sleep(3)
            print("\n===== STOK TERBARU =====")
            sisa_stok = sisa_stok + stok    #Hitung ulang total stok
            for produk in katalog:
                stok = produk[3]
                sisa_stok = sisa_stok + stok
                if stok == 0:
                    stok = "HABIS"
                print(produk[0], "|", produk[1], "| Stok:", stok)
        else:
            print("SEMUA STOK HABIS. VENDING MACHINE BERHENTI.")
        print("\n--------------------------------------------------\n")

        keranjang.clear()
        print("Terima Kasih Sudah Berbelanja!")
        time.sleep(10)
            