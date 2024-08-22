import os
import streamlit as st
from pypdf import PdfWriter
from tempfile import NamedTemporaryFile

st.write("""
         ## PDF Image :rainbow[Compressor]
         """)

def compress_pdf(to_compress, compression_factor):
    for idx, pdf in enumerate(to_compress, 1):
        writer = PdfWriter(clone_from = pdf)
        for page in writer.pages:
            for img in page.images:
                img.replace(img.image, quality = compression_factor)
        with NamedTemporaryFile(delete = False, delete_on_close = False, suffix = '.pdf') as tmp:
            writer.write(tmp)
            tmp_path = tmp.name
            to_export.append(tmp_path)
        os.unlink(tmp_path)

    return idx

pdfs_to_compress = st.file_uploader(label = "Upload your PDFs",
                                    type = ['pdf'],
                                    accept_multiple_files = True)

compression_factor = st.slider(label = "Compression Factor (%)",
                               min_value = 1,
                               max_value = 99,
                               value = 50)

if st.button(label = "Compress PDFs"):
    
    to_compress = []
    to_export = []

    if pdfs_to_compress:
        for pdf in pdfs_to_compress:
            with NamedTemporaryFile(delete = False, delete_on_close = False, suffix = '.pdf') as tmp:
                tmp.write(pdf.getvalue())
                tmp_path = tmp.name
                to_compress.append(tmp_path)
            os.unlink(tmp_path)
        # counter = compress_pdf(to_compress, compression_factor)
        # st.success(f"A total of {counter} PDFs has been compressed!")

        st.write(str(compression_factor))
        st.write(to_compress)
        st.write(to_export)

    else:
        st.error("No PDF was uploaded.")