# HCMS - Halal Consultant Management System

## 📋 Deskripsi

HCMS adalah aplikasi desktop berbasis Python yang dirancang untuk mengelola sistem manajemen consultant halal. Aplikasi ini menyediakan interface yang user-friendly untuk mengelola klien, pengajuan halal, invoice, dan sertifikat.

## ✨ Fitur Utama

- **Dashboard**: Tampilan overview dengan statistik real-time
  - Total Klien
  - Pengajuan Halal
  - Invoice
  - Sertifikat
  - Invoice Pending
  - Klien Aktif

- **Manajemen Klien**: Kelola data klien dengan mudah
  - Tambah Klien Baru
  - Edit Data Klien
  - Hapus Klien
  - Pencarian Klien

- **Manajemen Invoice**: Kelola invoice dan pembayaran
  - Buat Invoice
  - Track Status Pembayaran
  - Generate Laporan Keuangan

- **Manajemen Sertifikat**: Kelola sertifikat halal
  - Catat Sertifikat Baru
  - Track Tanggal Kadaluarsa
  - Perbarui Status Sertifikat

- **Error Handling**: Pesan error yang user-friendly
  - Dialog info untuk informasi
  - Dialog error untuk masalah
  - Validasi form yang komprehensif

## 🛠️ Instalasi

### Requirements

- Python 3.8+
- CustomTkinter 5.0+
- Pillow 9.0+

### Setup

1. Clone atau download project ini:
```bash
git clone <repository-url>
cd LEGAL_SYSTEM
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi:
```bash
python main.py
```

## 📂 Struktur Project

```
LEGAL_SYSTEM/
├── main.py                    # Entry point aplikasi
├── requirements.txt           # Python dependencies
├── assets/                    # Logo dan icons
├── data/
│   ├── database/
│   │   ├── hcms.db           # SQLite database
│   │   └── database.sql      # Database schema
│   ├── exports/              # File export
│   ├── reports/              # Laporan
│   └── backup/               # Backup database
├── app/
│   ├── models/               # Data models
│   │   ├── client_model.py
│   │   ├── user_model.py
│   │   ├── invoice_model.py
│   │   ├── certificate_model.py
│   │   └── halal_submission_model.py
│   ├── views/                # UI components
│   │   ├── base_view.py      # Base frame class
│   │   ├── sidebar_view.py   # Navigation sidebar
│   │   ├── dashboard_view.py # Dashboard page
│   │   ├── client_list_view.py # Client list
│   │   └── client_form_view.py # Client form
│   ├── controllers/          # Business logic
│   │   └── app_controller.py
│   ├── services/             # External services
│   │   ├── word_service.py
│   │   ├── pdf_service.py
│   │   ├── excel_service.py
│   │   └── backup_service.py
│   ├── database/
│   │   └── database.py       # Database connection
│   └── utils/                # Helper utilities
│       ├── validator.py      # Data validation
│       ├── helper.py         # Helper functions
│       └── formatter.py      # Data formatting
└── logs/                      # Application logs
```

## 🎯 Penggunaan

### Dashboard
- Halaman pertama menampilkan overview statistik
- Klik tombol Refresh untuk update data terbaru

### Mengelola Klien
1. Klik menu "Clients" di sidebar
2. Lihat daftar semua klien
3. Gunakan search untuk mencari klien spesifik
4. Klik "Add Client" untuk tambah klien baru
5. Klik "Edit" untuk mengubah data klien
6. Klik "Delete" untuk hapus klien (dengan konfirmasi)

### Validasi Data
- **Nama Klien**: Required
- **Email**: Format email valid (jika diisi)
- **Nomor Telepon**: Minimal 10 digit (jika diisi)
- **Invoice Amount**: Angka positif

## 🔧 Fitur Error Handling

Aplikasi dilengkapi dengan comprehensive error handling:

1. **Form Validation**: Validasi otomatis saat submit form
2. **Error Dialogs**: Pesan error yang jelas dan helpful
3. **Info Dialogs**: Notifikasi sukses untuk aksi
4. **Database Error Handling**: Try-catch untuk database queries
5. **User Feedback**: Toast-like messages untuk user actions

## 📊 Database

### Tables

1. **users**: User system HCMS
   - id, username, email, password, full_name, role, created_at

2. **clients**: Data klien
   - id, name, phone, email, address, company, industry, status, created_at, updated_at

3. **halal_submissions**: Pengajuan halal
   - id, client_id, submission_type, status, submission_date, completion_date

4. **invoices**: Data invoice
   - id, client_id, invoice_number, amount, status, due_date, created_at

5. **certificates**: Sertifikat halal
   - id, client_id, certificate_number, issue_date, expiry_date, status, created_at

## 🔐 Security

- Password di-hash menggunakan SHA256
- Data validation pada setiap form submission
- Database error handling untuk mencegah SQL injection

## 📝 Tips Penggunaan

1. **Backup Data Secara Berkala**: Gunakan fitur backup service
2. **Export Data**: Gunakan Excel/PDF export untuk laporan
3. **Search Function**: Gunakan search untuk mencari klien cepat
4. **Status Management**: Update status klien sesuai kebutuhan

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'customtkinter'"
```bash
pip install customtkinter
```

### Error: "Database connection failed"
- Pastikan folder `data/database/` ada
- Hapus `hcms.db` jika corrupt dan jalankan ulang aplikasi

### Error: "Icon file not found"
- Pastikan file `assets/logo/logo.ico` ada
- Aplikasi akan berjalan normal tanpa icon

## 📞 Support

Untuk masalah atau fitur request, silakan hubungi tim development.

## 📄 Lisensi

© 2026 HCMS - Halal Consultant Management System

---

**Version**: 1.0.0
**Last Updated**: 2026-07-15
