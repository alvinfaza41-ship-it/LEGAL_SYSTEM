# PANDUAN PENGGUNA HCMS - Tema Islami

## ☪️ Selamat Datang di HCMS

**HCMS** (Halal Consultant Management System) adalah aplikasi profesional berbasis desktop yang dirancang khusus dengan sentuhan **tema Islami** untuk mengelola sistem manajemen consultant halal dengan mudah dan efisien.

---

## 🎨 Desain & Tema Islami

Aplikasi ini menampilkan:
- **Warna Hijau & Biru Islami** untuk menciptakan suasana profesional
- **Aksent Emas** untuk detail penting
- **Salam Islami** di halaman dashboard
- **Simbol-simbol Islami** (☪️, 🕌) di seluruh interface
- **Typography profesional** dengan spacing sempurna
- **Responsive design** yang elegan

---

## 📂 Struktur Aplikasi

```
SIDEBAR MENU
├── 🏠 Dashboard          → Overview statistik real-time
├── 👥 Manajemen Klien    → Kelola data klien
├── 📋 Pengajuan Halal    → Track pengajuan halal (Soon)
├── 💰 Invoice            → Kelola invoice (Soon)
├── 📜 Sertifikat         → Track sertifikat (Soon)
├── 📊 Laporan            → Generate laporan (Soon)
└── ⚙️ Pengaturan         → Konfigurasi aplikasi (Soon)
```

---

## 🚀 Cara Memulai

### 1. Jalankan Aplikasi
```bash
cd C:\LEGAL_SYSTEM
python main.py
```

### 2. Halaman Pertama - Dashboard
Anda akan melihat:
- **Salam Islami**: "Assalamu Alaikum Wa Rahmatullahi Wa Barakatuh"
- **Statistik Real-time**:
  - 👥 Total Klien
  - 📋 Pengajuan Halal
  - 💰 Invoice
  - 📜 Sertifikat
  - ⏳ Invoice Pending
  - ✅ Klien Aktif
- **Tombol Refresh** untuk update data terbaru

---

## 👥 Mengelola Klien

### Tambah Klien Baru
1. Klik **"Manajemen Klien"** di sidebar
2. Klik tombol **"➕ Tambah Klien"**
3. Isi formulir:
   - 👤 **Nama Klien** (Wajib diisi)
   - 📱 **Nomor Telepon** (Opsional, min 10 digit)
   - ✉️ **Email** (Opsional, format valid)
   - 🏠 **Alamat** (Opsional)
   - 🏢 **Nama Perusahaan** (Opsional)
   - 🏭 **Industri** (Opsional)
   - 📊 **Status**: active / inactive / pending
4. Klik **"💾 Simpan"**

### Cari Klien
1. Di halaman "Manajemen Klien"
2. Gunakan kotak pencarian: **"🔍 Pencarian Klien"**
3. Cari berdasarkan: nama, telepon, atau email
4. Klik **"🔍 Cari"**

### Edit Klien
1. Lihat daftar klien
2. Klik tombol **"✏️"** pada baris klien
3. Edit data yang diperlukan
4. Klik **"💾 Simpan"**

### Hapus Klien
1. Klik tombol **"🗑️"** pada baris klien
2. Konfirmasi penghapusan di dialog popup
3. Klik **"Ya, Hapus"** untuk confirm

---

## 🎯 Fitur-Fitur Profesional

### 1. Validasi Data Otomatis
- ✅ Nama klien wajib diisi
- ✅ Email format harus valid
- ✅ Telepon minimal 10 digit
- ✅ Pesan error yang jelas

### 2. User Interface Responsif
- ✅ Sidebar expandable dan collapsible
- ✅ Konten yang dapat di-scroll
- ✅ Layout yang responsive pada berbagai ukuran layar
- ✅ Performa cepat dan smooth

### 3. Manajemen Status
Status klien dapat berupa:
- **active** (Aktif) - Klien sedang aktif
- **inactive** (Tidak Aktif) - Klien tidak aktif
- **pending** (Pending) - Menunggu konfirmasi

### 4. Database Terpadu
- SQLite 3 database
- Schema terstruktur dengan 5 tabel utama
- Relationship antar tabel
- Automatic backup pada setiap startup

---

## 🌈 Palet Warna Islami

| Element | Warna | Kode Hex | Keterangan |
|---------|-------|----------|-----------|
| Sidebar Background | Biru Islami | #0f4c75 | Warna dasar navigasi |
| Header | Hijau Islami | #1a5a3f | Warna kepala halaman |
| Primary Button | Hijau Cerah | #2d8659 | Tombol utama |
| Accent | Emas | #d4af37 | Highlight & active state |
| Success | Hijau | #10b981 | Status berhasil |
| Warning | Orange | #f97316 | Status warning |
| Error | Merah | #ef4444 | Status error |

---

## ⌨️ Keyboard Shortcut (Coming Soon)

| Shortcut | Fungsi |
|----------|--------|
| Ctrl + N | Tambah data baru |
| Ctrl + S | Simpan |
| Ctrl + F | Cari |
| Ctrl + R | Refresh |
| Ctrl + Q | Keluar |

---

## 🔐 Keamanan

- ✅ Password di-hash dengan SHA256
- ✅ Data validation pada setiap input
- ✅ Error handling untuk database queries
- ✅ Automatic backup on startup
- ✅ Confirmation dialogs untuk aksi penting

---

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'customtkinter'"
```bash
pip install customtkinter pillow
```

### Aplikasi terasa lambat
- Refresh database dari dashboard
- Tutup aplikasi dan buka ulang
- Pastikan tidak ada proses lain yang berat

### Data tidak tersimpan
- Pastikan folder `data/database/` ada dan accessible
- Cek permission folder LEGAL_SYSTEM
- Restart aplikasi

### Icon tidak muncul
- Pastikan file `assets/logo/logo.ico` ada
- Aplikasi tetap berjalan normal tanpa icon

---

## 📊 Database Schema

### Tabel: users
```sql
id, username, email, password, full_name, role, created_at
```

### Tabel: clients
```sql
id, name, phone, email, address, company, industry, 
status, created_at, updated_at
```

### Tabel: halal_submissions
```sql
id, client_id, submission_type, status, 
submission_date, completion_date
```

### Tabel: invoices
```sql
id, client_id, invoice_number, amount, status, 
due_date, created_at
```

### Tabel: certificates
```sql
id, client_id, certificate_number, issue_date, 
expiry_date, status, created_at
```

---

## 📞 Support & Feedback

Untuk pertanyaan, masukan, atau laporan bug:
1. Hubungi tim development
2. Kirim email ke: support@hcms.local
3. Buat issue di repository

---

## 📝 Tips & Tricks

### Untuk Performa Optimal:
1. ✅ Refresh data secara berkala
2. ✅ Backup database weekly
3. ✅ Tutup aplikasi saat tidak digunakan
4. ✅ Jangan edit database secara langsung

### Untuk UX Terbaik:
1. ✅ Gunakan search untuk mencari klien cepat
2. ✅ Update status klien secara rutin
3. ✅ Export laporan untuk dokumentasi
4. ✅ Check prayer time di sidebar

---

## 🎓 Fitur yang Akan Datang

- 📊 **Reports Module**: Generate laporan lengkap
- 💰 **Invoice Management**: Kelola invoice & pembayaran
- 📜 **Certificate Tracking**: Track sertifikat halal
- 📊 **Analytics Dashboard**: Visualisasi data
- 📧 **Email Notification**: Notifikasi otomatis
- 🔐 **User Authentication**: Login system
- 🌙 **Dark Mode**: Tema gelap

---

## ✨ Versi & Update

| Versi | Release Date | Features |
|-------|--------------|----------|
| 1.0.0 | 2026-07-15 | Dashboard, Client CRUD |
| 1.1.0 | Coming Soon | Invoice Management |
| 1.2.0 | Coming Soon | Certificates |
| 2.0.0 | Coming Soon | Full Authentication |

---

**Alhamdulillah! Semoga aplikasi HCMS dapat membantu mengelola bisnis Anda dengan lebih baik.**

**Terima kasih telah menggunakan HCMS - Halal Consultant Management System** 🙏

---

© 2026 HCMS - Halal Consultant Management System
**Version**: 1.0.0
**Last Updated**: 15 Juli 2026
**Made with ❤️ for Halal Industry**
