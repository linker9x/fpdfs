from fpdf import FPDF
import pandas as pd


class PDF(FPDF):
    def header(self):
        # Logo
        self.image('./resources/logo_pb.jpg', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'THIS IS THE HEADER', 0, 0, 'C')
        # Line break
        self.ln(50)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def chapter_title(self, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(211, 211, 211)
        # Title
        self.cell(0, 6, 'TITLE : {}'.format(label), 0, 1, 'L', 1)
        # Line break
        self.ln(10)

    def chapter_body(self, name, results):
        # Read text file
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # txt = str(results)
        # Times 12
        self.set_font('Arial', '', 12)
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def chapter_table(self, results):
        s = pd.Series(list(results.values()), index=list(results.keys()))
        s = s.sort_values()

        # setup the main table
        self.cell(90, 10, " ", 0, 1, 'C')
        self.cell(50, 10, 'User', 1, 0, 'C')
        self.cell(40, 10, 'Avg. Difference', 1, 1, 'C')
        self.set_font('arial', '', 12)

        # write the data to table
        for i, j in s.items():
            self.cell(50, 10, '%s' % (str(i)), 1, 0, 'C')
            self.cell(40, 10, '%s' % (str(round(j, 2))), 1, 1, 'C')
        self.ln(10)

    def print_chapter(self, title, name, results):
        self.add_page()
        self.chapter_title(title)
        self.chapter_table(results)
        self.chapter_body(name, results)


if __name__ == "__main__":
    results = {'cats': 10,
               'dogs': 11,
               'bats': 12,
               'cows': 13}

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.set_title('REPORT')
    pdf.set_author('Lisa Winkler')
    pdf.print_chapter('AN IMPORTANT TITLE', './resources/20k_c1.txt', results)
    pdf.output('./pdfs/REPORT.pdf', 'F')
