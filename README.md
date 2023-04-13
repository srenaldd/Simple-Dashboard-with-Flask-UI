# Google Play Store Analytics
<img src="https://raw.githubusercontent.com/srenaldd/Simple-Dashboard-with-Flask-Ui/main/flask_ui-main/full_capstone.png">

## Introduction
Projek ini dikembangkan sebagai salah satu capstone project dari Algoritma Academy Data Analytics Specialization. Deliverables yang diharapkan adalah dapat membangun sebuah aplikasi web sederhana (dashboard) menggunakan framework Flask. Capstone ini akan fokus pada tampilan user interface Flask. 

## Data Summary
Data yang digunakan pada capstone project ini adalah data hasil scraping dari Google Playstore App. Data Google Playstore App terdiri dari beberapa variabe dengan rincian sebagai berikut:
- `App` : Nama aplikasi                
- `Category` : Kategori aplikasi
- `Rating` : Rating keseluruhan yang diberikan oleh user aplikasi(ketika di scrap)
- `Reviews` : Jumlah review yang diberikan oleh user aplikasi(ketika di scrap)
- `Size` : Ukuran aplikasi(ketika di scrap)           
- `Installs` : Jumlah user yang menginstall/mendownload aplikasi(Ketika di scrap)     
- `Type` : Tipe aplikasi (berbayar/gratis)       
- `Price` : Harga aplikasi (ketika di scrap)        
- `Content Rating` : Kelompok usia aplikasi ini ditargetkan - Children / Mature 21+ / Adult   
- `Genres` : Genre aplikasi.        
- `Last Updated` : Tanggal kapan aplikasi terakhir diperbarui di Play Store (ketika discrap) 
- `Current Ver` : Versi aplikasi saat ini tersedia di Play Store (ketika discrap)   
- `Android Ver` : Minimum versi Android yang diperlukan (ketika discrap) 

## Dependencies
- Flask
- Matplotlib
- Pandas
- Numpy

## Rubrics
Pada capstone ini, diharapkan untuk dapat membangun sebuah aplikasi Flask yang fokus pada tampilan user interface. Langkah pertama yang harus  dilakukan adalah silahkan download atau clone repositori ini. File pada repositori ini merupakan sebuah skeleton untuk membuat sebuah dashboard aplikasi Flask. Pada bagian `app.py` dan `templates/index.html`. Beberapa hal yang harus diperhatikan adalah sebagai berikut:

### Setting Repository Github dan Environment 
- Repository 

a. Membuat repository baru di Github

b. Clone repository tersebut ke local dengan git clone

- Environment 

a. Created virtual environment called "capstone-flask"

Hal pertama yang harus dilakukan adalah melakukan pengaturan environment conda. Untuk menyiapkan conda environment dan kernel, silahkan gunakan command berikut:
```
conda create -n <ENV_NAME> python=3.10
conda activate <ENV_NAME>

conda install ipykernel
python -m ipykernel install --user --name <ENV_NAME>
```

b. Install packages: pandas, flask, matplotlib, dan numpy

Seluruh dependecies telah di-export ke dalam file requirements-final.txt. Oleh karena itu untuk melakukan install packages, Anda dapat menggunakan perintah berikut:
```
pip install -r requirements-final.txt --user
```


```
