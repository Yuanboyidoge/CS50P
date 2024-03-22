# from fpdf import FPDF
# from datetime import date
# import sys


# # 定义一个PDF类
# class PDF(FPDF):
#     def header(self):
#         self.add_font('fireflysung',"","D:\\python\\python_ws\\final\\fireflysung.ttf",True)
#         self.set_font('fireflysung', '', 16)
#         self.cell(200,10, "出差说明",ln=1,align='C')
               
#     def chapter_body(self, effective_page_width,text):
#         self.add_font('fireflysung',"","D:\\python\\python_ws\\final\\fireflysung.ttf",True)
#         self.set_font('fireflysung', '', 12)
#         # multi_cell() 方法会根据给定的宽度自动换行。但是，它默认不会解释文本中的 \n 换行符。
#         paragraphs = text.split('\n')
#         for paragraph in paragraphs:
#             self.set_y(self.get_y() + self.font_size)
#             self.multi_cell(effective_page_width, 10, paragraph)

#     def signature(self):
#         self.add_font('fireflysung',"","D:\\python\\python_ws\\final\\fireflysung.ttf",True)
#         self.set_font('fireflysung', '', 12)
#         self.set_xy(self.get_x(), self.get_y()+10)
#         self.cell(0, 10, "本人签字:            ", ln=1, align="R")
#         self.cell(0, 10, "日期:            ", ln=1, align="R")

# def getdate(start_date,end_date):
#     try:
#         return (date.fromisoformat(end_date)-date.fromisoformat(start_date)).days
#     except ValueError:
#         sys.exit("Invalid date")

# def road_fares(rf):
#     try:
#         return sum(list(map(float,rf.split())))
#     except ValueError:
#         sys.exit("Invalid input")

# def main():
#     # 输入
#     name = input("姓名: ")
#     student_id = input("学号: ")
#     start_date = input("出差起始日期（yyyy-mm-dd格式）: ")
#     end_date = input("出差结束日期: ")

#     # 计算出差时间
#     days = getdate(start_date,end_date)

#     place=input("出差地点：")
#     route = input("请输入往返路线: ")
#     hotel_name = input("请输入酒店名称: ")
#     hotel_price = float(input("请输入酒店单价: "))
#     accommodation_expenses = hotel_price * days

#     # 路费
#     total=road_fares(input("路费(以空格分隔)："))

#     # 创建pdf实例
#     pdf = PDF()
#     pdf.add_page()
#     effective_page_width = pdf.w - 2*pdf.l_margin

#     # 添加内容
#     pdf.chapter_body(effective_page_width,f"        本人{name}，学号: {student_id}，因项目需求，在{start_date}至{end_date}于{place}出差,共计{days+1}天。")
#     pdf.chapter_body(effective_page_width,f"出差路线往返说明：\n        {route}。")
#     pdf.chapter_body(effective_page_width,f"住宿安排：\n        本次出差入住{hotel_name}，共计{days}晚，住宿费用共计{accommodation_expenses}元。")
#     pdf.chapter_body(effective_page_width,f"总金额：\n        路费：{total}元\n        住宿：{hotel_price}*{days}={accommodation_expenses}元\n        补助：180.0*{days+1}={180*(days+1):.1f}元\n        总计：{total+accommodation_expenses+180*days}元")
#     pdf.signature()

#     # Save PDF
#     pdf.output("OUTPUT.pdf")

from fpdf import FPDF
from datetime import date
import sys

# Define a PDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', '', 16)
        self.cell(200, 10, "Business Travel Statement", ln=1, align='C')

    def chapter_body(self, effective_page_width, text):
        self.set_font('Arial', '', 12)
        # The multi_cell() method automatically wraps text based on the given width. However, it does not interpret '\n' newline characters by default.
        paragraphs = text.split('\n')
        for paragraph in paragraphs:
            self.set_y(self.get_y() + self.font_size)
            self.multi_cell(effective_page_width, 10, paragraph)

    def signature(self):
        self.set_font('Arial', '', 12)
        self.set_xy(self.get_x(), self.get_y() + 10)
        self.cell(0, 10, "Signature:            ", ln=1, align="R")
        self.cell(0, 10, "Date:            ", ln=1, align="R")

def getdate(start_date, end_date):
    try:
        return (date.fromisoformat(end_date) - date.fromisoformat(start_date)).days
    except ValueError:
        sys.exit("Invalid date")

def road_fares(rf):
    try:
        return sum(list(map(float, rf.split())))
    except ValueError:
        sys.exit("Invalid input")

def main():
    # Input
    name = input("Name: ")
    student_id = input("Student ID: ")
    start_date = input("Start date of business travel (in yyyy-mm-dd format): ")
    end_date = input("End date of business travel: ")

    # Calculate duration of business travel
    days = getdate(start_date, end_date)

    place = input("Location of business travel: ")
    route = input("Please enter the round trip route: ")
    hotel_name = input("Please enter the hotel name: ")
    hotel_price = float(input("Please enter the hotel unit price: "))
    accommodation_expenses = hotel_price * days

    # Road expenses
    total = road_fares(input("Road fares (separated by spaces): "))

    # Create PDF instance
    pdf = PDF()
    pdf.add_page()
    effective_page_width = pdf.w - 2 * pdf.l_margin

    # Add content
    pdf.chapter_body(effective_page_width, f"        I, {name}, Student ID: {student_id}, traveled to {place} from {start_date} to {end_date} for project requirements, totaling {days+1} days.")
    pdf.chapter_body(effective_page_width, f"Explanation of travel route:\n        {route}.")
    pdf.chapter_body(effective_page_width, f"Accommodation arrangement:\n        Stayed at {hotel_name} for {days} nights, with a total accommodation cost of {accommodation_expenses} yuan.")
    pdf.chapter_body(effective_page_width, f"Total amount:\n        Road expenses: {total} yuan\n        Accommodation: {hotel_price} * {days} = {accommodation_expenses} yuan\n        Allowance: 180.0 * {days+1} = {180*(days+1):.1f} yuan\n        Total: {total + accommodation_expenses + 180 * days} yuan")
    pdf.signature()

    # Save PDF
    pdf.output("OUTPUT.pdf")

main()

