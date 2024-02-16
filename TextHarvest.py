import PyPDF2

def extract_text_from_pdf(pdf_path):
    """Extract text content from a PDF file."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

def main():
    pdf_path = input("Enter the path to the PDF file: ")
    try:
        extracted_text = extract_text_from_pdf(pdf_path)
        print("\nExtracted Text: ")
        print(extracted_text)

        # Optionally save the extracted text to a text file with utf-8 encoding
        with open('extracted_text.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_text)
        print("\nExtracted text saved to 'extracted_text.txt'.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()

