# import random

# _PATH = 'C:\Users\lienh\OneDrive\Desktop\Lien\Trên lớp\python 1'

# question_file_name = 'questions.txt'
# answer_file_name = 'answers.txt'
# prize_file_name = 'prize.txt'

# questions = _PATH + '/' + question_file_name
# answers = _PATH + '/' + answer_file_name
# prize = _PATH + '/' + prize_file_name

# with open(questions, 'r', encoding = 'UTF-8') as f:
#     questions_list = f.readlines()
# print(questions_list[0]
# code phần up file bị lỗi



import random
import time

question_list = ['Có câu thành ngữ: "Đi mây về ..." gì? --- ⬥ A: Mây\t⬥ B: Núi\t⬥ C: Biển\t⬥ D: Gió\n', 'Đâu là một cách nói ví von về những trường hợp gặp vận hạn, rủi ro? --- ⬥ A: Sao quả cân\t⬥ B: Sao quả tạ\t\t⬥ C: Sao quả tấn\t⬥ D: Sao quả yến\n', 'Gỗ mun có màu gì? --- ⬥ A: Vàng\t\t⬥ B: Nâu\t⬥ C: Đen\t⬥ D: Xanh\n', 'Câu nào chỉ tình cảnh đơn độc, yếu thế không có chỗ dựa? --- ⬥ A: Thân tàn ma dại\t⬥ B: Thân cô thế cô\t⬥ C: Thân lừa ưa nặng\t\t⬥ D: Thân làm tội đời\n', 'Đâu là tên một loại đồ chơi dân gian của trẻ em? --- ⬥ A: Tò he\t\t⬥ B: Tò mò\t⬥ C: Tò vò\t⬥ D: Tến tò\n', 'Đâu là tên một bãi biển ở Quảng Bình? --- ⬥ A: Đá Lăn\t⬥ B: Đá Nhảy\t⬥ C: Đá Chạy\t⬥ D: Đá Bò\n', 'Đâu là tên một loại chợ? --- ⬥ A: Ếch\t⬥ B: Nhái\t⬥ C: Thằn lằn\t⬥ D: Cóc\n', 'Tượng đài Chiến thắng Điện Biên Phủ được dựng trên ngọn đồi nào? --- \t⬥ A: D1\t\t⬥ B: C1\t\t⬥ C: A1\t\t⬥ D: E1\n', 'Nhà văn Kim Dung (Trung Quốc) nổi tiếng với thể loại văn học gì? --- \t⬥ A: Truyện trinh thám\t\t⬥ B: Tiểu thuyết kiếm hiệp\t⬥ C: Sử thi\t⬥ D: Thơ lãng mạn\n', 'Bộ phim "Chị Dậu" được chuyển thể từ tác phẩm nào? --- \t⬥ A: Người mẹ cầm súng\t\t⬥ B: Vợ chồng A Phủ\t⬥ C: Tắt đèn\t⬥ D: Tuổi thơ dữ dội\n', 'Loại cá nào bé hơn cả? ---\t⬥ A: Voi\t⬥ B: Bống\t⬥ C: Mập\t⬥ D: Heo\n', 'Giọng khàn khàn còn được ví với gì? ---\t⬥ A: Thiên nga\t\t⬥ B: Vịt đực\t⬥ C: Ngan xiêm\t\t⬥ D: Ngỗng\n', 'Sầu riêng Cái Mơn là đặc sản của tỉnh nào? ---\t⬥ A: Tiền Giang\t\t⬥ B: Cà Mau\t⬥ C: Bến Tre\t⬥ D: Đồng Tháp\n', 'Loại củ nào sau đây có thể giúp cho vết thương mau lành và ít để lại sẹo? ---\t⬥ A: Giềng\t⬥ B: Hành tây\t\t⬥ C: Gừng\t⬥ D: Nghệ\n', 'Cướp biển còn được gọi với tên khác là gì? ---⬥ A: Đạo tặc\t⬥ B: Lâm tặc\t⬥ C: Tin tặc\t⬥ D: Hải tặc\n', 'Hoa hậu Hòa bình Quốc tế 2017 dự kiến sẽ được tổ chức tại quốc gia nào? ---\t⬥ A: Thái Lan\t⬥ B: Việt Nam\t⬥ C: Lào\t⬥ D: Campuchia\n', 'Vườn quốc gia nào hiện không nằm trong danh sách Vườn di sản ASEAN? ---\t⬥ A: Vườn quốc gia Kon Ka Kinh\t⬥ B: Vườn quốc gia Tam Đảo\t⬥ C: Vườn quốc gia Chư Mom Ray\t⬥ D: Vườn quốc gia Bái Tử Long\n', 'Nhạc sĩ nào là người phổ nhạc ca khúc "Cây đàn sinh viên"? ---\t⬥ A: Bảo Chấn\t⬥ B: Trịnh Công Sơn\t⬥ C: Quốc An\t⬥ D: Trần Tiến\n', 'Đâu không phải là một tác phẩm của họa sĩ Trần Văn Cẩn? --- ⬥ A: Đôi bạn\t⬥ B: Mẹ tôi\t⬥ C: Em Thúy\t⬥ D: Em gái tôi']
answer_list = ['D\n', 'B\n', 'C\n', 'B\n', 'A\n', 'B\n', 'D\n', 'C\n', 'B\n', 'C\n', 'B\n', 'B\n', 'C\n', 'D\n', 'D\n', 'B\n', 'B\n', 'C\n', 'A']
prize_list = ['   100.000  \n', '150.000\n', '300.000\n', '600.000\n', '1.000.000\n', '2.500.000\n', '6.000.000\n', '11.000.000\n', '22.000.000\n', '35.000.000\n', '66.000.000\n', '99.000.000\n', '120.000.000\n', '250.000.000\n', '500.000.000']

print("Chào mừng đến với trò chơi Ai là triệu phú.")
time.sleep(1)
print(""" Thí sinh trả lời 15 câu hỏi của chương trình
Sau mỗi câu trả lời đúng, Thí sinh được phép chọn đi tiếp hoặc dừng lại
Nếu dừng lại, thí sinh sẽ nhận được toàn bộ giải thưởng ở mốc câu hỏi mà thí sinh đó đã trả lời đúng
Nếu thí sinh trả lời sai:
Nếu sai câu đầu tiên, thí sinh không nhận được giải thưởng nào
Nếu sai câu hỏi bất kỳ trừ câu đầu tiên, thí sinh sẽ nhận được giải thưởng ở mốc đầu tiên.
Nếu thí sinh trả lời đúng tất cả các câu, nhận giải thưởng ở mốc cuối cùng
""")
answers_list_adjust = []
for i in answer_list:
    answers_list_adjust.append(i.strip())

prize_list_adjust = []
for j in prize_list:
    prize_list_adjust.append(j.strip())
question_appeared = []
position = 0
for f in range(15):
    question_num =("Cau hoi thu {}:").format(position + 1)
    print(question_num)
    question_position = random.randint(1,18)
    
    while question_position in question_appeared:
        question_position = random.randint(1,18)
        
    print(question_list[question_position])
    user_answer = input("Type your answer: ")
    if user_answer.lower() == (answers_list_adjust[position]).lower():
        print("Correct!")
    print("Giải thưởng lúc này của bạn:", prize_list_adjust[position])
    if position == 14:
        print("Chúc mừng bạn đã hoàn thành trò chơi với giải thưởng là {} đồng!".format(prize_list_adjust[position]))
    else:
        position += 1
        continue_or_stop = input("Bạn có muốn chơi tiếp không: (Yes/No) ")
        if continue_or_stop.lower() == "yes".lower():
            question_appeared.append(position)
            continue
        else:
            print("Bạn đã kết thúc trò chơi với giải thưởng là {} đồng!".format(prize_list_adjust[position - 1]))   
            break  
        if position == 0:
            print("Thật đáng tiếc, vì trả lời sai câu hỏi đầu tiên nên bạn không nhận được giải thưởng.")
            break
        else:
            print("Thật đáng tiếc, vì bạn đã trả lời sai câu hỏi nên số tiền thưởng của bạn quay về {}".format(prize_list_adjust[0]))
            break

    

