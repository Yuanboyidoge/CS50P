from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 48)
        self.cell(0, 30, 'CS50 Shirtificate',align='C')
        self.add_image()
    
    def add_text(self, text, font='Arial', size=24, color=(255, 255, 255)):
        self.set_text_color(*color)
        self.set_font(font, 'I', size)
        # 这参数太奇怪了
        self.cell(-180, 220, f"{text} took CS50", align='C')

    def add_image(self):
        self.image("shirtificate.png",10,70,190)

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=False, margin=0)
pdf.add_text(input("Name:"))
pdf.output('shirtificate.pdf')