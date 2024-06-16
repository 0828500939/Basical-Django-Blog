# Django

## Cài đặt Django

```bash
pip install django
```

## Tạo một Dự án Django mới

```bash
django-admin startproject myproject
cd myproject
```

## Tạo một Ứng dụng mới

```bash
python manage.py startapp myapp
```

## Chạy Dự án

```bash
# Chạy lệnh dưới để khởi động server phát triển
python manage.py runserver

# Mặc định, server sẽ chạy ở http://127.0.0.1:8000/
```

## Di chuyển Cơ sở Dữ liệu

```bash
# Tạo và áp dụng migration cho cơ sở dữ liệu
python manage.py makemigrations
python manage.py migrate
```

## Tạo Siêu Người Dùng (Superuser)

```bash
# Tạo một tài khoản admin để truy cập trang quản trị Django
python manage.py createsuperuser
```

## Kiểm tra Dự án

```bash
# Chạy các bài kiểm tra có trong dự án
python manage.py test
```

## Lệnh Quản lý Khác

```bash
# Thu thập các file tĩnh cho production
python manage.py collectstatic

# Kiểm tra lỗi trong dự án
python manage.py check

# Xóa tất cả dữ liệu trong cơ sở dữ liệu và tải lại từ các migration
python manage.py flush

# Hiển thị URL patterns của dự án
python manage.py show_urls
```

## Cấu trúc Thư mục Dự án

```plaintext
myproject/
│
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── myapp/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── static/
│
├── templates/
│
├── db.sqlite3
│
└── manage.py
```

## Tham khảo thêm

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django Tutorials](https://docs.djangoproject.com/en/stable/intro/tutorial01/)

```

README này cung cấp các lệnh cơ bản và một cái nhìn tổng quan về cau trúc thư mục của dự án Django. Bạn có thể điều chỉnh và mở rộng thêm tùy theo yêu cầu cụ thể của dự án.
```