## Web App xem dự báo thời tiết của 34 tỉnh thành ở Việt Nam
(Code ở nhánh develop)

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


### Dùng docker đã export image:
Tải file .tar https://github.com/huyhq01/weather-app/releases/tag/v0.1

Vào cmd ở thư mục chứa file, dòng này sẽ load image trong file tar vào docker:
```bash
docker load -i weather-app.tar
```

Tạo và chạy container từ image khi load khi nãy:
```bash
docker run -d -p 5000:8000 weather-app
```
-d
Detached mode: Chạy container ở chế độ nền (background), không chiếm terminal của bạn.
Nếu không dùng -d, container sẽ chạy ở chế độ foreground và bạn sẽ thấy log trực tiếp trong terminal.
*Thay đổi số 5000 tùy ý vì nó là cổng của máy thực, trong app thì chạy port 8000 

Nếu muốn tạo container trước:
```bash 
docker create --name my-container -p 8000:8000 weather-app:latest
```
Chạy container:
```bash
docker start my-container
```

