from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Lấy dữ liệu từ Form nhập liệu
        data = {
            'ngay': request.form.get('ngay', ''),
            'thang': request.form.get('thang', ''),
            'nam': request.form.get('nam', '2026'),
            'can_bo_hotro': request.form.get('can_bo_hotro', 'Nguyễn Thanh Nhã'),
            'sdt_hotro': request.form.get('sdt_hotro', '0919435650'),
            'email_hotro': request.form.get('email_hotro', 'ntnha17@gdt.gov.vn'),
            'loai_yeu_cau': request.form.getlist('loai_yeu_cau'),
            'yeu_cau_khac': request.form.get('yeu_cau_khac', ''),
            'ten_nguoi_dung': request.form.get('ten_nguoi_dung', ''),
            'chuc_vu_nguoi_dung': request.form.get('chuc_vu_nguoi_dung', 'Công chức'),
            'phong_ban': request.form.get('phong_ban', ''),
            'sdt_nguoi_dung': request.form.get('sdt_nguoi_dung', ''),
            'email_nguoi_dung': request.form.get('email_nguoi_dung', ''),
            'hinh_thuc': request.form.get('hinh_thuc', ''),
            'y_kien': request.form.get('y_kien', '')
        }
        return render_template('index.html', data=data, is_submitted=True)
    
    return render_template('index.html', is_submitted=False)

if __name__ == '__main__':
    app.run(debug=True)