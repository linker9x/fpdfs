from fpdf import FPDF

def print_statement():
    """
    Print Hall Account statements for specified hall_ID
    """

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page('P')
    pdf.set_font('Times', 'B', 14)

    pdf.multi_cell(0, 5, ('Hall Account Statement for Hall: {}'.format('LISA')))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Mess Account: %s' % 'MESSID: 4444'))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Salary Account: %s' % 'SAL ACC: 5555'))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Repair Account: %s' % 'REP ACC: 6666'))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Rent Account: %s' % 'RENT ACC: 7777'))
    pdf.ln()
    pdf.multi_cell(0, 5, ('Others Account: %s' % 'OTHER: 4444'))
    pdf.ln()

    # Write generated output file to PDF
    pdf.output('hall_statement.pdf', 'F')

if __name__ == "__main__":
	print_statement()