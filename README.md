# Task Manager API

## 1. Nama Aplikasi dan Fungsi
Task Manager API adalah REST API sederhana untuk menambah, melihat,
menandai selesai, dan menghapus tugas.

## 2. Bahasa dan Framework
Python 3 dan Flask. Unit test menggunakan pytest.

## 3. Cara Menjalankan
    pip install -r requirements.txt
    python run.py

Akses di http://127.0.0.1:5000/tasks

## 4. Overview Pipeline CI/CD
Pipeline (`.github/workflows/devsecops.yml`) terpicu saat push dan
pull_request ke branch main. Terdiri dari 2 job:
- **build**: install dependencies dan menjalankan unit test (pytest)
- **sast-scan**: menjalankan Bandit (SAST), bergantung pada job build,
  dengan Quality Gate yang gagal jika ditemukan isu severity MEDIUM ke atas.