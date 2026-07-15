CREATE TABLE IF NOT EXISTS clients (

id INTEGER PRIMARY KEY AUTOINCREMENT,

kode_client TEXT,

nama TEXT,

perusahaan TEXT,

alamat TEXT,

telepon TEXT,

email TEXT,

status TEXT,

created_at TEXT

);
CREATE TABLE IF NOT EXISTS clients (

id INTEGER PRIMARY KEY AUTOINCREMENT,

kode_client TEXT UNIQUE,

nama_pic TEXT,

nama_perusahaan TEXT,

jenis_usaha TEXT,

alamat TEXT,

kecamatan TEXT,

kabupaten TEXT,

provinsi TEXT,

kode_pos TEXT,

nik TEXT,

npwp TEXT,

nib TEXT,

email TEXT,

whatsapp TEXT,

status TEXT,

tanggal_daftar TEXT,

catatan TEXT

);