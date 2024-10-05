Python với AI
1. Xử lý ngôn ngữ tự nhiên(NLP)
2. Học máy(Machine Learning)
3. Học sâu(Deep Learning)
4. Thị giác máy tính(Computer Vision)

Trong ví dụ này:
Xây dựng 1 ứng dụng: Phân loại văn bản(Text Classification) sử dụng mô hình học máy(Machine Learning)
và frameWork Flask: nhẹ, đơn giản.

Mục đích của ví dụ:
1. Sử dụng AI để phân tích văn bản kiểm tra "Spam" hoặc "Không Spam" (Được ứng dụng trong email...)
2. Tạo ứng dụng tin nhắn demo để kiểm thử kết quả

Các bước thực thi để thực hiện ví dụ
1. Chuẩn bị dữ liệu phân loại văn bản sử dụng sklearn cung cấp tập dữ liệu Spam/Non-Spam, là thư viện học máy để xây dựng mô hình phân loại
2. Sử dụng mô hình AI: Sử dụng Naive Bayes để phân lại văn bản thành Spam or Non-Spam. Naive Bayes là một thuật toán dựa trên định lý Bayes với giả định rằng các đặc điểm của dữ liệu là độc lập nhau. Nó thường được sử dụng với bài toán phân loại văn bản

Quy trình xây dựng mô hình AI
1. Thu thập dữ liệu: Tập hợp các dữ liệu báo cáo để đào tạo(training data) có nhãn.
2. Tiền xử lý dữ liệu: Chuyển đổi dữ liệu từ dạng "Thô" thành định dạng mô hình có thể hiểu, ví dụ: vector hoá văn bản.
3. Huấn luyện mô hình: Dùng dữ liệu để huấn luyện mô hình AI
4. Đánh giá mô hình: Sử dụng dữ liệu kiểm thử để đánh giá độ chính xác của mô hình


Cấu trúc chương trình trong ví dụ trên:
1. ai_model.py: Xây dựng mô hình AI
2. app.py: Flask app chính
3. model.pkl: Mô hình AI đã huấn luyện
4. vectorizer.pkl: Công cụ vector hoá dữ liệu