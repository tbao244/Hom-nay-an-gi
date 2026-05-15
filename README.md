# HỆ THỐNG GỢI Ý BỮA ĂN THÔNG MINH
Dự án xây dựng ứng dụng website nguyên mẫu (Prototype) gợi ý bữa ăn thông minh sử dụng Fuzzy Logic. Hệ thống giúp giải quyết sự lưỡng lự trong việc chọn món ăn dựa trên nhiều yếu tố không chắc chắn để đưa ra danh sách địa điểm phù hợp.

## Tính năng nổi bật
* Gợi ý thông minh: Kết hợp 5 biến đầu vào (Mức độ đói, ngân sách, thời gian, mục tiêu sức khỏe, thời tiết) để đưa ra quyết định.
* Hệ luật Fuzzy Rules: Xử lý 68 quy luật để đảm bảo độ chính xác và bao quát nhất có thể.
* Tích hợp bản đồ trực quan: Kết nối trực tiếp với Google Map API để quét vị trí các nhà hàng thực tế dựa trên loại ẩm thực và vị trí người dùng.
* Xác định vị trí & tính toán khoảng cách: Hệ thống tự động lấy tọa độ GPS của người dùng và tính toán hiển thị khoảng cách từ vị trí hiện tại đến quán ăn được gợi ý.
* Machine Learning: Tự động ghi nhớ khẩu vị của người dùng và ưu tiên các loại ẩm thực người dùng thường chọn.
---
## Công nghệ sử dụng
* Ngôn ngữ lập trình: Python
* Giao diện: Streamlit
* Logic mờ: scikit-learn, numpy
* Dữ liệu thời tiết & bản đồ: OpenWeatherMap API, Google Map API
---
Cấu trúc dự án
```bash
├── app.py               Giao diện chính và kết nối hệ thống
├── fuzzy_logic.py       Bộ não xử lý Fuzzy Logic
├── api_services.py      Dịch vụ API thời tiết và bản đồ
├── config.py            Dữ liệu quán ăn và cấu hình API Key
├── requirements.txt     Danh sách thư viện cần cài đặt
└── README.md

---
## Cài đặt
* Cài đặt các thư viện cần thiết
```
* pip install -r requirements.txt
```
* Khởi chạy ứng dụng
```
* streamlit run app.py
```
---
## Cơ chế hoạt động của Fuzzy Logic
Hệ thống sử dụng các hàm liên thuộc trimf và trapmf để bao quát các từ khóa một cách hơp lý nhất.
*	Mờ hóa (Fuzzification): Mỗi đầu vào rõ ràng (ví dụ: hunger = 5,8) được đánh giá dựa trên tất cả các hàm thành viên của biến đó. Kết quả là một tập các mức độ thành viên cho mỗi nhãn mờ.
*	Đánh giá quy tắc (Rule Evaluation): Mỗi quy tắc If-Then kích hoạt với độ mạnh bằng giá trị nhỏ nhất của các mức độ thành viên tiền đề (toán tử AND). Nhiều quy tắc có thể kích hoạt đồng thời với độ mạnh khác nhau.
*	Tổng hợp (Aggregation): Với mỗi biến đầu ra, các tập mờ đầu ra bị cắt từ tất cả các quy tắc đang hoạt động được kết hợp (hợp / tối đa) thành một tập mờ tổng hợp duy nhất.
*	Giải mờ (Defuzzification): Tập tổng hợp được chuyển đổi thành một số rõ ràng duy nhất bằng phương pháp trọng tâm: tọa độ x của "điểm cân bằng" của vùng tổng hợp.

