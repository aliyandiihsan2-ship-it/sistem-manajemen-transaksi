# 📊 Sistem Manajemen Transaksi

Aplikasi backend berbasis **Python** menggunakan **FastAPI** dan **MongoDB** untuk mencatat, mengelola, dan memantau riwayat transaksi keuangan secara efisien.

## 🚀 Fitur Utama
* **Pencatatan Transaksi:** Input data transaksi berdasarkan tipe (Investasi, Pembelian, Kerugian).
* **Filtering Data:** Mencari riwayat transaksi berdasarkan nominal (`amount`) dan metode pembayaran.
* **Export to Excel (New!):** Fitur untuk mengunduh seluruh riwayat transaksi langsung ke format `.xlsx` (Excel) untuk laporan.
* **Validasi Pydantic:** Menjamin data yang masuk ke database selalu valid dan konsisten.
* **FastAPI Docs:** Dokumentasi API otomatis yang bisa langsung dicoba melalui browser.

## 🛠️ Teknologi yang Digunakan
* **Bahasa:** Python 3.x
* **Framework:** FastAPI
* **Database:** MongoDB
* **Library Tambahan:** `pandas` & `openpyxl` (untuk fitur Export Excel)
* **Editor:** VS Code

## ⚙️ Cara Instalasi

1. **Clone Repositori**
   ```bash
   git clone [https://github.com/aliyandiihsan2-ship-it/sistem-manajemen-transaksi.git](https://github.com/aliyandiihsan2-ship-it/sistem-manajemen-transaksi.git)
   cd sistem-manajemen-transaksi
