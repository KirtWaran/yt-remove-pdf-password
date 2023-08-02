import PyPDF2
import os

password = input('Provide the password for the PDF files: ')

for filename in os.listdir('./input'):
    if filename.endswith('.pdf'):
        file_path = os.path.join('./input', filename)

        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            if pdf_reader.is_encrypted:
                pdf_reader.decrypt(password)
                pdf_writer = PyPDF2.PdfWriter()

                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)

                with open(f"./output/unlocked_{filename}", 'wb') as output_file:
                    pdf_writer.write(output_file)

                print(f"PDF unlocked successfully. Unlocked PDF saved as: unlocked_{filename}")

            else:
                print("The PDF file is not password-protected.")
