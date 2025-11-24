# Install dependencies
!pip install flask pyngrok  # Thay đổi vì: Cần cài đặt Flask và pyngrok trong môi trường Colab.

# Configure ngrok
!ngrok authtoken 31pKCCoZnuH8jaFvxa9OICzbNKa_3aJbV2ozJrmVT1t4P5Bb4  # Thay đổi vì: Cần cung cấp authtoken để xác thực với ngrok.

# Create directories
!mkdir -p templates static/css static/images static/js  # Thay đổi vì: Tạo cấu trúc thư mục để chứa template và static files trong Colab.

# (Upload files manually or copy from Google Drive as described above)

# Flask app code
from flask import Flask, render_template
from pyngrok import ngrok
import threading

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('trangchu.html')

# Subpage routes
@app.route('/gioi-thieu')
def gioi_thieu():
    return render_template('gioi_thieu.html')

@app.route('/chuong-trinh-hoc')
def chuong_trinh_hoc():
    return render_template('chuong_trinh_hoc.html')

@app.route('/trai-nghiem-sinh-vien')
def trai_nghiem_sinh_vien():
    return render_template('trai_nghiem_sinh_vien.html')

@app.route('/goc-truyen-thong')
def goc_truyen_thong():
    return render_template('goc_truyen_thong.html')

@app.route('/doanh-nghiep')
def doanh_nghiep():
    return render_template('doanh_nghiep.html')

@app.route('/lien-he')
def lien_he():
    return render_template('lien_he.html')

def run_flask():
    app.run(host='0.0.0.0', port=5000)  # Thay đổi vì: Chạy Flask trên host 0.0.0.0 để ngrok có thể truy cập.

# Start ngrok and Flask
public_url = ngrok.connect(5000).public_url  # Thay đổi vì: Tạo tunnel ngrok để expose server Flask.
print(f" * ngrok tunnel available at: {public_url}")
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()  # Thay đổi vì: Chạy Flask trong thread riêng để Colab không bị block.