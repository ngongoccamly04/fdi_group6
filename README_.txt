#FDI ATTRACTION IN VIETNAM 

Chương trình dùng để thống kê và trực quan hóa dữ liệu về số lượng dự án, vốn đầu tư và các phân bố ngành nghề vốn đầu tư nước ngoài vào Việt Nam giai đoạn 2015 - 2022. 

############################################################################### 
  
Cách chạy chương trình: 
- Trong folder chứa file Python và các file csv, nháy chuột phải vào khoảng trống. Chọn Open in Terminal. 
- Trong cửa sổ Terminal, nhập lệnh: 
	py tên_file.py 
sau đó nhấn enter. Chương trình sẽ được chạy. 
- Chương sẽ chạy và đưa ra các lựa chọn để bạn có thể chọn. Sau khi chọn thì biểu đồ sẽ được hiển thị. 
- Để tiếp tục hiển thị các biểu đồ tiếp theo bạn cần đóng các biểu đồ trước đó lại. 
- Muốn thoát khỏi chương trình, bạn cần chọn giá trị ứng với chức năng thoát. 

############################################################################### 

Các ứng dụng về thư viện: 
- Pandas: 
+ Dùng để đọc các dữ liệu có trong file csv (pd.read_csv),  Trích xuất dữ liệu từ cột 'Column_Name' 
(column_data = df['Column_Name']), Trích xuất dữ liệu từ dòng có chỉ mục index (row_data = df.iloc[index]). 
+ Xử lí các dữ liệu: 
   ·  Xử lý giá trị thiếu: Sử dụng các phương thức như fillna() để điền giá trị cho các ô dữ liệu trống. 
   ·  Sử dụng phương thức replace() để thay thế các giá trị không hợp lệ hoặc không mong muốn. 
   ·  Chuyển đổi kiểu dữ liệu: Sử dụng phương thức pd.to_numeric() để chuyển đổi các cột thành kiểu số nếu cần thiết. 
- Numpy: 
+ Tính tổng các giá trị trong các nhóm dữ liệu (sum()). 
- Matplotlib: 
+ Sử dụng để vẽ biểu đồ cột (plt.bar()). 
+ Sử dụng để vẽ biểu đồ cột ngang (plt.barh()). 
+ Sử dụng để vẽ biểu đồ cột nhóm. 
+ Sử dụng để vẽ biểu đồ thanh ngang (plt.annotate(). 
Ví dụ về ứng dụng các thư viện: 
- Chuyển đổi dữ liệu sang dạng số: 
+ Sử dụng phương thức pd.to_numeric() của thư viện Pandas để chuyển đổi các cột "Number of new projects" và "Adjusted project number" sang dạng số. Điều này giúp đảm bảo tính chính xác của dữ liệu và thuận tiện cho việc thực hiện các phép tính sau này. 
- Tính tổng số dự án mới và điều chỉnh theo ngành: 
+Sử dụng phương thức groupby() của Pandas để nhóm dữ liệu theo cột "Industry" và tính tổng số dự án mới và điều chỉnh trong mỗi nhóm ngành. 
- Vẽ biểu đồ: 
+ Sử dụng thư viện Matplotlib để vẽ biểu đồ cột ngang. 
+ Thiết lập kích thước của biểu đồ bằng plt.figure(figsize=(length,width)). 
+ Sử dụng plt.barh() để vẽ các cột ngang. 
+ Thiết lập nhãn trục x và trục y bằng plt.xlabel() và plt.ylabel(). 
+ Đặt tiêu đề cho biểu đồ bằng plt.title(). 
+ Hiển thị chú thích về các loại dữ liệu bằng plt.legend(). 
+ Lưu biểu đồ vào file "name.png" bằng plt.savefig(). 
+ Hiển thị biểu đồ bằng plt.show(). 
  
############################################################################### 
  
Phân tích dữ liệu: 
Về tác động của FDI đến sự chuyển dịch cơ cấu kinh tế ở Việt Nam, sự tham gia của khu vực FDI trong nhiều ngành, lĩnh vực, đặc biệt là sự tập trung vốn FDI trong ngành công nghiệp chế biến, chế tạo và một số ngành công nghiệp khác, là nhân tố quan trọng thúc đẩy chuyển dịch cơ cấu kinh tế theo hướng hiện đại, góp phần xây dựng môi trường kinh tế năng động và gia tăng năng lực sản xuất các sản phẩm chứa hàm lượng chất xám cao trong nền kinh tế. FDI góp phần chuyển dịch cơ cấu nông nghiệp, đa dạng hóa sản phẩm, nâng cao giá trị hàng nông sản xuất khẩu. 
- Theo giai đoạn 2015 - 2022 
+ Tổng số dự án đầu tư mới và dự án điều chỉnh: 
   ·  Từ năm 2015, số lượng dự án tăng dần từ mức 2013 dự án đến năm 2019, số lượng dự án đăng kí mới đạt mức đỉnh điểm với mức 3883 dự án, sau đó giảm dần về mức trung bình đến năm 2022. Số lượng dự án được điều chỉnh có sự thay đổi qua các năm nhưng không đáng kể.  
+ Tổng số vốn đầu tư mới và số vốn điều chỉnh: 
   · Năm 2021, tổng vốn đăng ký cấp mới, điều chỉnh và góp vốn mua cổ phần, mua phần vốn góp của nhà đầu tư nước ngoài đạt 31,15 tỷ USD, tăng 9,2% so với cùng kỳ năm 2020, vốn thực hiện ước đạt 19,74 tỷ USD. Tính lũy kế đến ngày 20/12/2021, Việt Nam có khoảng 34.527 dự án còn hiệu lực với tổng vốn đăng ký gần 408,1 tỷ USD, vốn thực hiện lũy kế ước đạt 251,6 tỷ USD, bằng 61,7% tổng vốn đầu tư đăng ký còn hiệu lực. 
   ·  Qua phân tích thực trạng về FDI và chuyển dịch cơ cấu ngành kinh tế ở Việt Nam giai đoạn 2016 - 2022, nghiên cứu nhận thấy Việt Nam đã đạt được những kết quả tích cực trong thu hút vốn FDI, mức bình quân vốn đầu tư khoảng 30 tỷ USD/năm, tốc độ tăng bình quân khoảng 14%/năm, tốc độ tăng bình quân giải ngân vốn khoảng 11%, góp phần giải quyết việc làm, nâng cao chất lượng nguồn nhân lực và đem lại nguồn thu nhập khả quan cho người lao động, thúc đẩy và hỗ trợ các doanh nghiệp trong nước phát triển.. 
+ Xếp hạng các quốc gia có số vốn đầu tư vào Việt Nam lớn nhất: Từ những năm 2015 - 2022, Hàn Quốc là nước dẫn đầu về tổng lượng vốn đầu tư nước ngoài vào Việt Nam với con số hơn 40000 triệu USD, sau đó là Nhật Bản với khoảng 33000 triệu USD, rồi đến Singapore với khoảng 32000 triệu USD. Đây là 3 quốc gia bỏ xa các nước còn lại về tổng lượng vốn đầu tư. 
+ Xếp hạng các ngành được đầu tư nhiều nhất của Việt Nam. 
   ·   Tổng số dự án của các ngành trong giai đoạn này: Phần lớn các dự án đổ dồn về các ngành công nghiệp chế biến và hàng tiêu dùng, kế đến là buôn bán sỉ và lẻ, đứng thứ ba là đầu tư về các vấn đề nghiên cứu khoa học và công nghệ. 
   ·   Tổng số vốn đầu tư của các ngành trong giai đoạn này: Với số lượng dự án lớn, vốn đầu tư vào khu vực công nghiệp đa số tập trung vào các ngành có thời gian hoàn vốn ngắn như công nghiệp sản xuất hàng tiêu dùng và chế biến thực phẩm; số dự án đầu tư vào công nghệ cao, dây chuyền sản xuất hiện đại chưa nhiều. Theo báo cáo khảo sát của Tổng cục Thống kê năm 2021, về trình độ công nghệ, khoảng trên 30% doanh nghiệp cho biết hiện vẫn đang sử dụng hoàn toàn thiết bị điều khiển thủ công, trên 50% có sử dụng thiết bị bán tự động, chỉ hơn 10% doanh nghiệp có sử dụng thiết bị tự động hóa và chưa đến 10% doanh nghiệp có sử dụng robot trong dây chuyền sản xuất. 

Giải pháp thu hút FDI trong thời gian tới: 
- Xu hướng đầu tư ra nước ngoài của các quốc gia đang có dấu hiệu chậm lại. Điều này đòi hỏi Việt Nam cần thực thi nhiều giải pháp hiệu quả để thu hút dòng vốn FDI có chất lượng trong thời gian tới. Mặc dù cơ hội của Việt Nam trong thu hút vốn đầu tư nước ngoài dịch chuyển là rất lớn, nhưng để cơ hội đó trở thành hiện thực và thu hút được những dự án từ các nhà đầu tư chất lượng, uy tín, mang lại hiệu quả cao, Việt Nam đã và đang tập trung vào những giải pháp sau: 
+ Thứ nhất, tiếp tục quảng bá, xúc tiến đầu tư.  
+ Thứ hai, thu hút đầu tư có chọn lọc.  Liên kết khu vực FDI với khu vực kinh tế trong nước nhằm tạo dựng và phát triển công nghiệp phụ trợ trong nước.  
+ Thứ ba, cải thiện môi trường đầu tư kinh doanh. 
+ Thứ tư, ưu đãi hỗ trợ đầu tư. Ngoài việc xây dựng môi trường kinh doanh tạo thuận lợi cho các nhà đầu tư, Việt Nam cần tiếp tục ban hành các gói hỗ trợ hấp dẫn. 
  
############################################################################### 

Người đóng góp: 
22130157 - Lê Bá Sơn 
22130160 - Lê Duy Thắng 
22130097 - Ngô Ngọc Cẩm Ly 
22130158 - Trần Thanh Sơn 

###############################################################################   

Thông tin liên lạc: 
Trần Thanh Sơn - 22130158@student.hcmus.edu.vn 
Lê Duy Thắng - 22130160@student.hcmus.edu.vn 
Lê Bá Sơn - 22130157@student.hcmus.edu.vn 
Ngô Ngọc Cẩm Ly - 22130097@student.hcmus.edu.vn 

###############################################################################  

Dữ liệu tham khảo: 
- https://tapchinganhang.gov.vn/thu-hut-fdi-cua-viet-nam-nam-2022-va-trien-vong.htm 
- https://tapchinganhang.gov.vn/dong-gop-cua-dau-tu-truc-tiep-nuoc-ngoai-doi-voi-kinh-te-viet-nam-giai-doan-2016-2022-va-khuyen-nghi.htm 
- https://data.opendevelopmentmekong.net/dataset/fdi-investment-in-vietnam-2015-2022 

 

 