import json
import requests
import streamlit as st

# Tiêu đề
st.title("Nhận Biết Khách Hàng Rời Bỏ Dịch Vụ Viễn Thông")

# Hình ảnh
st.image("img/churn-image.jpeg")
# Giới thiệu
st.write(
    """
    ## Giới thiệu
    Toàn cầu hóa và sự phát triển của ngành công nghiệp viễn thông đã làm gia tăng nhanh chóng số lượng nhà cung cấp dịch vụ trên thị trường, từ đó đẩy mạnh sự cạnh tranh. 
    Trong thời kỳ cạnh tranh khốc liệt này, việc tối đa hóa lợi nhuận theo định kỳ đã trở thành bắt buộc. Nhiều chiến lược đã được đề xuất, bao gồm: thu hút khách hàng mới, 
    tăng doanh số từ khách hàng hiện tại và kéo dài thời gian sử dụng dịch vụ của khách hàng. Trong số các chiến lược này, việc giữ chân khách hàng hiện tại là cách ít tốn kém nhất. 
    Để thực hiện chiến lược thứ ba, các công ty phải giảm thiểu tỷ lệ khách hàng rời bỏ dịch vụ. Nguyên nhân chính của việc rời bỏ dịch vụ là do sự không hài lòng với hệ thống hỗ trợ và dịch vụ khách hàng. 
    Chìa khóa để giải quyết vấn đề này là dự đoán những khách hàng có nguy cơ rời bỏ dịch vụ.

    **Ứng dụng Streamlit này sử dụng mô hình Máy Học (XGBoost) API để phát hiện liệu khách hàng của một công ty viễn thông có rời bỏ dịch vụ hay không.**

    Notebook, mô hình, tài liệu (kịch bản FastAPI, kịch bản Streamlit) và các phân tích khác

    Thực hiện bởi nhóm 4 AI Enginnering

    """
)

######################################## Hàm ###########################################################
# Biến nhị phân
def create_binary(content):
    if content == "Nam":
        content = 1
    elif content == "Nữ":
        content = 0
    elif content == "Có":
        content = 1
    elif content == "Không":
        content = 0
    return content
# Chuyển đổi Dịch vụ Nhiều Đường Truyền, Bảo Mật Trực Tuyến, Sao Lưu Trực Tuyến, Bảo Vệ Thiết Bị, Hỗ Trợ Kỹ Thuật, Truyền Hình Trực Tuyến và Phim Trực Tuyến
def convert_muliples_var(content):
    if content == "Không sử dụng dịch vụ điện thoại":
        content = 1
    elif content == "Không":
        content = 0
    elif content == "Có":
        content = 2
    return content

def convert_internet_ser(content):
    if content == "Cáp quang":
        content = 1
    elif content == "DSL":
        content = 0
    elif content == "Không":
        content = 2
    return content

def convert_contract(content):
    if content == "Một năm":
        content = 1
    elif content == "Theo tháng":
        content = 0
    elif content == "Hai năm":
        content = 2
    return content

def convert_payment_method(content):
    if content == "Thẻ tín dụng (tự động)":
        content = 1
    elif content == "Chuyển khoản ngân hàng (tự động)":
        content = 0
    elif content == "Hóa đơn điện tử":
        content = 2
    elif content == "Hóa đơn gửi qua bưu điện":
        content = 3
    return content


########################################################### Dữ liệu đầu vào ######################################################################
st.sidebar.title("Dữ liệu Khách Hàng")

# Biến phân loại và nhị phân
var_gender = ("Nam", "Nữ")
var_bool = ("Có", "Không")
var_multiple = ("Có", "Không", "Không sử dụng dịch vụ điện thoại")
var_internet = ("DSL", "Cáp quang", "Không")
var_contract = ("Theo tháng", "Một năm", "Hai năm")
var_payment_m = ("Thẻ tín dụng (tự động)", "Chuyển khoản ngân hàng (tự động)", "Hóa đơn điện tử", "Hóa đơn gửi qua bưu điện")

gender = st.sidebar.selectbox("Giới tính của khách hàng", var_gender)
partner = st.sidebar.selectbox("Bạn đời", var_bool)
dependents = st.sidebar.selectbox("Khách hàng có sống cùng người phụ thuộc (trẻ em, cha mẹ, v.v.) không?", var_bool)
mutiple_lines = st.sidebar.selectbox("Khách hàng có sử dụng nhiều đường truyền điện thoại không?", var_multiple)
internet_services = st.sidebar.selectbox("Khách hàng có sử dụng nhiều dịch vụ Internet không?", var_internet)
online_security = st.sidebar.selectbox("Khách hàng có sử dụng dịch vụ bảo mật trực tuyến không?", var_multiple)
online_backup = st.sidebar.selectbox("Khách hàng có sử dụng dịch vụ sao lưu trực tuyến không?", var_multiple)
device_protection = st.sidebar.selectbox("Khách hàng có sử dụng dịch vụ bảo vệ thiết bị không?", var_multiple)
tech_support = st.sidebar.selectbox("Khách hàng có sử dụng dịch vụ hỗ trợ kỹ thuật không?", var_multiple)
streaming_tv = st.sidebar.selectbox("Khách hàng có sử dụng dịch vụ truyền hình trực tuyến không?", var_multiple)
streaming_movies = st.sidebar.selectbox("Khách hàng có sử dụng dịch vụ xem phim trực tuyến không?", var_multiple)
contract = st.sidebar.selectbox("Loại hợp đồng hiện tại của khách hàng là gì?", var_contract)
paperless_billing = st.sidebar.selectbox("Hóa đơn điện tử", var_bool)
payment_method = st.sidebar.selectbox("Phương thức thanh toán", var_payment_m)

# Biến số
tenure_months = st.sidebar.number_input("Số tháng gắn bó", min_value=0, max_value=80)
monthly_charges = st.sidebar.number_input("Phí hàng tháng")
cltv = st.sidebar.number_input("Giá trị vòng đời của khách hàng (CLTV)")

######################################################### Dự đoán #########################################################

prediction = st.button("Phát hiện kết quả")

if prediction:

    data = {
        "Gender" : create_binary(gender),
        "Parther" : create_binary(partner),
        "Dependents" : create_binary(dependents),
        "Tenure_Months" : tenure_months,
        "Mutiple_lines" : convert_muliples_var(mutiple_lines),
        "Internet_services" : convert_internet_ser(internet_services),
        "Online_Security" : convert_muliples_var(online_security),
        "Online_Backup" : convert_muliples_var(online_backup),
        "Device_Protection" : convert_muliples_var(device_protection),
        "Tech_support": convert_muliples_var(tech_support),
        "Streaming_tv": convert_muliples_var(streaming_tv),
        "Streaming_movies" : convert_muliples_var(streaming_movies),
        "Contract" : convert_contract(contract),
        "Paperless_billing" : create_binary(paperless_billing),
        "Payment_method": convert_payment_method(payment_method),
        "Monthly_charges" : monthly_charges,
        "cltv": cltv
    }

    # Query
    rep = requests.post("http://api-ai-churn:80/predict", json= data)
    json_str = json.dumps(rep.json())
    respon = json.loads(json_str)

    st.subheader(f"{respon[0]}")



