print(" ")
print("Code written by Theo Zanello")
print(" ")
import PyPDF2

def split_pdf_for_duplex(input_pdf_path, odd_output_path, even_output_path):
    """Splits a PDF into odd and reversed even pages for manual duplex printing."""

    try:
        with open(input_pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_writer_odd = PyPDF2.PdfWriter()
            pdf_writer_even = PyPDF2.PdfWriter()

            even_pages = [] #store even pages, to reverse later

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                if (page_num + 1) % 2 != 0:  # Odd page
                    pdf_writer_odd.add_page(page)
                else:  # Even page
                    even_pages.append(page)

            #reverse the order of even pages.
            even_pages.reverse()

            for page in even_pages:
                pdf_writer_even.add_page(page)

            with open(odd_output_path, 'wb') as odd_pdf:
                pdf_writer_odd.write(odd_pdf)

            with open(even_output_path, 'wb') as even_pdf:
                pdf_writer_even.write(even_pdf)

        print("Splitted PDF into odd and even pages and reversed the order of even pages.")

    except FileNotFoundError:
        print("Error: Input PDF file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_file = "my_document.pdf"  # Replace with your PDF file's name
odd_file = "odd_pages.pdf"
even_file = "even_pages.pdf"

split_pdf_for_duplex(input_file, odd_file, even_file)