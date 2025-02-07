# Customer Churn Prediction (Group 4 Artificial Intelligence Systems Engineering Course - 2425I_INT7024)

[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/sklearn-darkorange.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Framework](https://img.shields.io/badge/FastAPI-darkgreen.svg?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Framework](https://img.shields.io/badge/Streamlit-red.svg?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
![hosted](https://img.shields.io/badge/Google%20Cloud-4285F4?&style=flat&logo=Google%20Cloud&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white)

## Machine Learning

### **Data Preparation**

Bộ dữ liệu khách hàng viễn thông của IBM chứa thông tin về một công ty viễn thông giả định cung cấp dịch vụ điện thoại cố định và internet cho 7.043 khách hàng tại California. Bộ dữ liệu này cho biết khách hàng nào đã rời đi, ở lại hoặc đăng ký dịch vụ của công ty. Nhiều thông tin nhân khẩu học quan trọng được bao gồm cho từng khách hàng, cùng với Điểm hài lòng (Satisfaction Score), Điểm rời mạng (Churn Score) và Chỉ số Giá trị Trọn đời Khách hàng (Customer Lifetime Value - CLTV). Tổng cộng, bộ dữ liệu có 32 đặc trưng hoặc biến dự báo.

Các bước tiền xử lý dữ liệu:

Làm sạch dữ liệu: Loại bỏ các giá trị trùng lặp, giá trị thiếu, các biến không cần thiết và các biến có thể gây rò rỉ dữ liệu.
Chuyển đổi biến không phải số thành biến số.
Chia dữ liệu thành tập huấn luyện, tập kiểm định và tập kiểm tra.
Xử lý dữ liệu mất cân bằng bằng kỹ thuật oversampling - SMOTE.
Chọn tập hợp đặc trưng tốt nhất bằng kỹ thuật Loại bỏ Đặc trưng Đệ quy có Kiểm định Chéo (RFECV - Recursive Feature Elimination with Cross Validation).

Source: [IBM](https://community.ibm.com/accelerators/catalog/content/Telco-customer-churn)


### **Modelling**

Các thuật toán Machine Learning đã thử nghiệm:

- Logistic Regression (baseline)  
- K-Nearest Neighbors (KNN)  
- XGBoost  

XGBoost là mô hình có hiệu suất tốt nhất trên tập kiểm định:

- accuracy: 0.93  
- f1-score: 0.90  
- roc-auc: 0.93  

Hiệu suất của mô hình cuối cùng (XGBoost) trên tập kiểm tra:

- accuracy: 0.94
- f1-score: 0.98
- roc-auc: 0.98

### **Deployment**

- API gọi vào mô hình được deploy bằng Dockerfile trên Google Cloud.
- Ứng dụng Streamlit và Model cũng được deploy cùng một máy trên Google Cloud.







