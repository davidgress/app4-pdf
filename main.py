from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    # Set the header
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # pdf.line(10, 21, 200, 21)
    # add lines to the page
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
        # add lines to the page
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

# w=0 extends to end of line
# border=1 puts border around text
# ln=1 is a break line
# align=L is align to Left
# h=12 is recommend same as font size

pdf.output("output.pdf")