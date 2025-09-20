## Web App xem dự báo thời tiết của 34 tỉnh thành ở Việt Nam


### Giới thiệu: 
Dự án nhằm tự học, demo. Có thể xem được thông tin (trong 24h, 7 ngày bao gồm hôm nay) như:
- Nhiệt độ, độ ẩm không khí ở độ cao 2m
- Xác xuất mưa
- Tốc độ gió ở độ cao 10m
- Mô tả thời tiết ban ngày, chiều tối, từng giờ

### Yêu cầu:
 - Windows
 - python 3.13
 - pip 25.2
 - virtualenv 20.34.0
 - Nên cài trong env sau khi khởi tạo môi trường ảo tránh xung đột nếu có:
   + Django 5.2.6
   + djangorestframework 3.16.1
   + requests 2.32.5

### Cài đặt:
 ```bash
 # Tạo môi trường ảo
 python -m venv venv

 # Kích hoạt môi trường ảo:
 env\Scripts\activate

 # kiểm tra python và pip trong env
 where python
 where pip
 # nếu đường dẫn python và pip nằm ở thư mục dự án ở đầu tiên là ok
 # ..weather-app\env\Scripts\python.exe
 # ..weather-app\env\Scripts\pip.exe

 # Cài thư viện
 pip install -r requirements.txt

 # Tạo db
 cd weather_app
 python manage.py migrate

 # Chạy chương trình
 python manage.py runserver
 ```
