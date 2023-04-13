from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

playstore = pd.read_csv("data/googleplaystore.csv")

playstore.drop_duplicates(subset = "App", keep="first", inplace=True) 

# bagian ini untuk menghapus row 10472 karena nilai data tersebut tidak tersimpan pada kolom yang benar
playstore.drop([10472], inplace=True)

playstore.Category = playstore["Category"].astype("category")

playstore.Installs = playstore["Installs"].apply(lambda x: x.replace(",", ""))
playstore.Installs = playstore["Installs"].apply(lambda x: x.replace("+", ""))

# Bagian ini untuk merapikan kolom Size, Anda tidak perlu mengubah apapun di bagian ini
playstore['Size'].replace('Varies with device', np.nan, inplace = True ) 
playstore.Size = (playstore.Size.replace(r'[kM]+$', '', regex=True).astype(float) * \
             playstore.Size.str.extract(r'[\d\.]+([kM]+)', expand=False)
            .fillna(1)
            .replace(['k','M'], [10**3, 10**6]).astype(int))
playstore['Size'].fillna(playstore.groupby('Category')['Size'].transform('mean'),inplace = True)

playstore.Price = playstore["Price"].apply(lambda x: x.replace("$", ""))
playstore.Price = playstore["Price"].astype("float64")

# Ubah tipe data Reviews, Size, Installs ke dalam tipe data integer
playstore[["Reviews", "Size", "Installs"]] = playstore[["Reviews", "Size", "Installs"]].astype("int64")

@app.route("/")
# This fuction for rendering the table
def index():
    df2 = playstore.copy()

    # Statistik
    top_category = pd.crosstab(index = df2["Category"], columns = "Jumlah").sort_values(by = "Jumlah", ascending=False).reset_index()
    # Dictionary stats digunakan untuk menyimpan beberapa data yang digunakan untuk menampilkan nilai di value box dan tabel
    stats = {
        'most_categories' : top_category.Category.iloc[0],
        'total': top_category.Jumlah.iloc[0],
        'rev_table' : df2.groupby(["Category", "App"]).agg({"Reviews" : "sum", "Rating" : "mean"}).sort_values(by = "Reviews", ascending=False).reset_index().head(10).to_html(classes=['table thead-light table-striped table-bordered table-hover table-sm']),
    }


    ## Bar Plot
    cat_order = cat_order = df2.groupby("Category").agg({
    "Category" : "count"
    }).rename({'Category':'Total'}, axis=1).sort_values(by = "Total", ascending = False).head()    
    X = cat_order.index
    Y = cat_order.Total
    my_colors = [(0.291, 0.609, 0.934)]
    # bagian ini digunakan untuk membuat kanvas/figure
    fig = plt.figure(figsize=(9,4.5),dpi=300)
    fig.add_subplot()
    # bagian ini digunakan untuk membuat bar plot
    plt.barh(X, Y, color=my_colors)
    plt.tight_layout() #menyesuaikan layout
    # bagian ini digunakan untuk menyimpan plot dalam format image.png
    plt.savefig('cat_order.png',bbox_inches="tight") 

    # bagian ini digunakan untuk mengconvert matplotlib png ke base64 agar dapat ditampilkan ke template html
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    # variabel result akan dimasukkan ke dalam parameter di fungsi render_template() agar dapat ditampilkan di 
    # halaman html
    result = str(figdata_png)[2:-1]
    
    ## Scatter Plot
    X = df2["Reviews"].values # axis x
    Y = df2["Rating"].values # axis y
    area = playstore["Installs"].values/10000000 # ukuran besar/kecilnya lingkaran scatter plot
    fig = plt.figure(figsize=(5,5))
    fig.add_subplot()
    # isi nama method untuk scatter plot, variabel x, dan variabel y
    plt.scatter(x=X,y=Y, s=area, alpha=0.3)
    plt.xlabel('Reviews')
    plt.ylabel('Rating')
    plt.tight_layout() #menyesuaikan layout
    plt.savefig('rev_rat.png',bbox_inches="tight")

    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result2 = str(figdata_png)[2:-1]

    ## Histogram Size Distribution
    X=(playstore["Size"]/1000000).values
    fig = plt.figure(figsize=(5,5))
    fig.add_subplot()
    plt.hist(X,bins=100, density=True,  alpha=0.75)
    plt.xlabel('Size (Mb)')
    plt.ylabel('Frequency')
    plt.tight_layout() #menyesuaikan layout
    plt.savefig('hist_size.png',bbox_inches="tight")

    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result3 = str(figdata_png)[2:-1]

    ## Buatlah sebuah plot yang menampilkan insight di dalam data 
    fig = plt.figure(figsize=(7.3,7))
    fig.add_subplot()
    labels= ["Free", "Paid"]
    colors= [(0.291, 0.609, 0.934), (0.391, 0.909, 0.834)]
    sizes= df2["Type"].value_counts()
    plt.pie(sizes,labels=labels, colors=colors, startangle=90, shadow=True,explode=(0.1, 0.1), autopct='%1.2f%%')
    plt.tight_layout() #menyesuaikan layout
    plt.savefig("type_app.png", bbox_inches="tight")
    #plt.show()

    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result4 = str(figdata_png)[2:-1]





    # Tambahkan hasil result plot pada fungsi render_template()
    return render_template('index.html', stats=stats, result=result, result2=result2, result3=result3, result4=result4)

@app.route('/convert-to-png')
def convert_to_png():
    file_path = 'D:\\New\\Pelatihan\\Algoritma\\Project DA\\flask_ui-main'  
    img = Image.open(file_path)
    img.save('capstone_full.png')
    return send_file('capstone_full.png', mimetype='image/png')

if __name__ == "__main__": 
    app.run(debug=True)
