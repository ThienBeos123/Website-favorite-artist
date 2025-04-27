import streamlit as st

st.set_page_config(
    page_title="Ca sĩ yêu thích",
    page_icon=":notes:",
    layout="wide")

img_path = "C:/Users/Admin/Music/den-vau-chang-rapper-day-tai-nang.jpg"
img_path2 = "C:/Users/Admin/Music/images.jfif"
audio_path = open("C:/Users/Admin/Music/Đen - Lối Nhỏ ft. Phương Anh Đào (MV).mp3", "rb")
vid_path = "https://youtu.be/KKc_RMln5UY?si=CibJGFrA20oZR5Nn"

st.title("**Ca sĩ yêu thích** :violin:")
st.image(img_path, caption="Đen vâu")
st.header("**Bài hát yêu thích** :musical_note:")
st.write("Lối nhỏ")
st.audio(audio_path, format = "audio/mp3")
st.header("**MV yêu thích** :movie_camera:")
st.video(vid_path, format = "video/mp4")

with st.sidebar:
    st.title("**Giới thiệu thêm**")
    st.image(img_path2)
    st.write("**Họ tên** :boy: : Nguyễn Đức Cường")
    st.write("**Ngày sinh**  :calendar: : 13 tháng 5 năm 1989")
    st.write("**Quê quán**  :palm_tree: : Ân Thi, Hưng Yên, Việt Nam")
    st.write("**Tiểu sử**  :film_frames: : Anh đi làm công việc nhân viên ban quản lý :blue[_Vịnh Hạ Long_] ở tỉnh :blue[_Quảng Ninh_] trong 7 năm. "
             "Xen lẫn trong khoảng thời gian này, anh xin nghỉ việc không lương để hỗ trợ em trai mở quán cà phê để kiếm sống. "
             "Quán cà phê này làm ăn thua lỗ, anh đi làm để bù đắp chi phí duy trì và quán chính thức đóng cửa vào năm 2016. "
             "Sau khi trả được nợ, anh viết ca khúc :red['_Ngày lang thang_'] - một dấu mốc về suy nghĩ tích cực của mình. "
             "Nói về nghệ danh Đen Vâu, anh cho biết: _'Hồi bé một chị hàng xóm thấy tôi đen nên gọi là Đen. "
             "Đến khi chơi nhạc, mọi người lại gọi là Đen Vâu nên tôi lấy luôn. "
             "Tên xấu cho dễ nuôi'_")





