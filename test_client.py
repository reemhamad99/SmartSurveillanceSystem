import requests

# 1. اختبار إيقاف الكاميرا (Disable)
print("جاري إرسال أمر إيقاف الكاميرا...")
response = requests.post("http://127.0.0.1:5000/api/camera/control", json={"enabled": False})
print("استجابة السيرفر:", response.json())

# 2. التحقق من الحالة بعد الإيقاف
status_response = requests.get("http://127.0.0.1:5000/api/camera/status")
print("الحالة الحالية من السيرفر:", status_response.json())