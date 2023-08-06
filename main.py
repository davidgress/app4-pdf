from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

# w=0 extends to end of line
# border=1 puts border around text
# ln=1 is a break line
# align=L is align to Left
# h=12 is recommend same as font size

pdf.output("output.pdf")