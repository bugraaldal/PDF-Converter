import os
import tkinter as tk
from PyPDF2 import PdfFileReader
from tkinter import filedialog
from pathlib import Path
from fpdf import FPDF
txt2pdf = FPDF()


def PDFToText():
    # Choosing the file
    my_file = filedialog.askopenfilename(initialdir="/", title="Select File",
                                         filetypes=(("PDF Files", "*.pdf"),))
    pdf_reader = PdfFileReader(str(my_file))
    File = os.path.basename(str(my_file))
    # Splitting the name to name it properly in the future
    name = File.split(".")[0]
    # Setting the name of the text file
    output_file_path = Path.home() / "Desktop" / f"{name}.txt"
    # Opening the file and getting the info into it using the module
    with output_file_path.open(mode="w", encoding='utf-8') as output_file:
        title = pdf_reader.documentInfo.title
        num_pages = pdf_reader.getNumPages()
        output_file.write(f"{title}\\nNumber of pages: {num_pages}\\n\\n")
        for page in pdf_reader.pages:
            t = page.extractText()
            output_file.write(t)
    # Showing a file converted message at the end
    top = tk.Toplevel()
    tk_resultsfound_label = tk.Label(
        top, text=f"File Converted {my_file} to {output_file}", font="none 12 bold")
    tk_resultsfound_label.pack()


def All_toPDF():
    # Same things as the upper one
    my_file = filedialog.askopenfilename(initialdir="/", title="Select File",
                                         filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files", "*.*")))
    File = os.path.basename(str(my_file))
    name = File.split(".")[0]
    output_file_path = Path.home() / "Desktop" / f"{name}.pdf"
    # Reading the text file and exporting it into a PDF
    with open(my_file, "r", encoding="utf-8") as f:
        n = f.readlines()
        k = [a.replace("\n", "") for a in n]
        txt2pdf.add_page()
        for x in k:
            txt2pdf.set_font("Arial", size=15)
            txt2pdf.cell(200, 10, txt=x, ln=1, align="C")
    txt2pdf.output(output_file_path)
    # Showing a file converted message at the end
    top = tk.Toplevel()
    tk_resultsfound_label = tk.Label(
        top, text=f"File Converted {name}", font="none 12 bold")
    tk_resultsfound_label.pack()


# Basic configurations of the GUI
root = tk.Tk()
root.title("PDF-Text Conventer")
root.configure(background="red")
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
PDF_Button = tk.Button(root, text="Choose a File to Convert to PDF", padx=310,
                       pady=5, fg="white", bg="red", command=All_toPDF)
PDF_Button.pack(side="bottom")

Txt_Button = tk.Button(root, text="Choose a PDF File to Convert to Text", padx=310,
                       pady=5, fg="white", bg="red", command=PDFToText)
Txt_Button.pack(side="bottom")

root.mainloop()
