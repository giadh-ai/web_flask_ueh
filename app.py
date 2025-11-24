from flask import Flask, render_template
import requests
import os

app = Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True

# --- CẤU HÌNH SUPABASE ---
SUPABASE_URL = "https://ocateixuzulwmrtxseom.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9jYXRlaXh1enVsd21ydHhzZW9tIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTYyMTYyMTQsImV4cCI6MjA3MTc5MjIxNH0.w7PLqjLGj4hNNGDh81NwDodEUCCqVSVm_PL0FpYWif8"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

# --- 1. TRANG CHỦ (HOME) ---
@app.route('/')
def home():
    # Gọi API lấy toàn bộ sản phẩm từ bảng 'product1' (bảng mới giống React)
    # Sắp xếp theo id tăng dần
    url = f"{SUPABASE_URL}/rest/v1/product1?select=*&order=id.asc"
    
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            products = response.json()
            # Nếu API trả về None thì gán là danh sách rỗng
            if products is None:
                products = []
            return render_template('trangchu.html', products=products)
        else:
            print(f"Lỗi API: {response.text}")
            return render_template('trangchu.html', products=[])
    except Exception as e:
        print(f"Lỗi kết nối: {str(e)}")
        return render_template('trangchu.html', products=[])


# --- 2. CHI TIẾT SẢN PHẨM ---
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Gọi API lấy 1 sản phẩm theo id
    url = f"{SUPABASE_URL}/rest/v1/product1?id=eq.{product_id}&select=*"
    
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            if data and len(data) > 0:
                # Truyền object sản phẩm đầu tiên tìm được vào template
                return render_template('product_detail.html', product=data[0])
            else:
                return "Không tìm thấy sản phẩm", 404
        else:
            return f"Lỗi server: {response.status_code}", 500
    except Exception as e:
        return f"Lỗi hệ thống: {str(e)}", 500


# --- 3. GIỎ HÀNG (QUAN TRỌNG: Route này sửa lỗi BuildError) ---
@app.route('/cart')
def cart():
    # Trả về giao diện giỏ hàng
    return render_template('cart.html')


# --- 4. CÁC TRANG TĨNH KHÁC ---
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


# --- KHỞI CHẠY APP ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)