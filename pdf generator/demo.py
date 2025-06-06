from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 16)
        width = self.get_string_width(self.title)+8
        self.set_x((210 - width)/2)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1)
        self.cell(width, 9, self.title, new_x="LMARGIN", new_y="NEXT", align="C", fill=True)
        self.ln(10)
    
    def footer(self):
        self.set_y(-16)
        self.set_font("helvetica", "I", 10)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}")

    
    def chapter_title(self, num, label):
        self.set_font("helvetica", "", 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, f"Chapter {num} : {label}", new_x="LMARGIN", new_y="NEXT", align="L", fill=True)
        
    
    def chapter_body(self, filepath):
        with open(filepath, "rb") as fh:
            txt = fh.read().decode()
        self.set_font("Times", size=12)
        self.multi_cell(0, 5, txt)
        self.ln()
        self.set_font(style="I")
        self.cell(0, 5, "(End of excerpt)")
            
        
    
    def print_chapter(self,num, title, filepath):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(filepath)
        
    

pdf = PDF()
pdf.set_title("100 ways of programming")
pdf.set_author("Amirreza Daneshmand")
# one chapter
pdf.print_chapter(1, "Getting start", "para.txt")
pdf.print_chapter(2, "Getting End", "para.txt")
pdf.output("output.pdf")