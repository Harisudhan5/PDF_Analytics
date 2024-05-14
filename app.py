import streamlit as st
import fitz  # PyMuPDF
import io

# Set page title and icon
st.set_page_config(page_title="PDF Viewer", page_icon=":books:")

# Define function to read and display PDF file
def view_pdf(uploaded_file):
    pdf_bytes = uploaded_file.read()
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        image_bytes = page.get_pixmap().tobytes()
        st.image(image_bytes, caption=f"Page {page_number+1}", use_column_width=True)

# Define main function
def main():
    st.title("PDF Viewer")
    
    # Sidebar
    st.sidebar.title("Upload PDF")
    uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])
    
    # Button to process PDF
    if st.sidebar.button("Process PDF"):
        if uploaded_file is not None:
            st.sidebar.success("Processing PDF...")
            # Process PDF here
            print("OK")
        else:
            st.sidebar.warning("Please upload a PDF file before processing.")

    # Main content
    if uploaded_file is not None:
        st.sidebar.success("PDF successfully uploaded!")
        # Display PDF
        view_pdf(uploaded_file)
    else:
        st.sidebar.info("Please upload a PDF file.")

# Run the main function
if __name__ == "__main__":
    main()
