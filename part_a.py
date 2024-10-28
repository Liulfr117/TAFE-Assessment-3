'''
Program Description: This program makes user-specified changes to pdf files. The available actions are merging, rotating, encrypting and decrypting.
The user is asked which action they would like to perform, and then asked to specify arguments such as input pdf file(s) and output location. The program
performs the chosen action on the specified pdf file using functionality from the PyPDF2 library, and then saves the output file to the specified location.
'''

# Name: Dylan Bailey
# Student ID: 20114978

# Date                   Version                    Reason for Change
# 03/10/2024             1                          Creation of program
# 05/10/2024             2                          Removed duplicate code that was used to save the changed pdf in a seperate file and used the code to make a seperate function, save_pdf
# 05/10/2024             3                          Moved functions so that they are alphabetically ordered
# 06/10/2024             4                          Added getpass functionality for additoinal security. This module ensures that the password the user enters doesn't display on screen

import PyPDF2
import getpass

def main():

    # A while loop is used to create a menu in which the user can specify what action they want to perform. If they choose an action number that
    # doesn't exist, the program will reprompt them.
    while True:
        print("\n1. Merge PDFs")
        print("2. Rotate a page in PDF")
        print("3. Encrypt PDF")
        print("4. Decrypt PDF")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        # Conditional statement that handles a user's request to merge pdf files. Asks the user to specify how many files they want to merge, then uses a
        # for loop to create a list containing the paths to the files that are to be merged.
        if choice == '1':
            pdf_list = []
            num_files = int(input("How many PDF files would you like to merge? "))
            for i in range(num_files):
                pdf_file = input(f"Enter the path for PDF file {i + 1}: ")
                pdf_list.append(pdf_file)
            output_pdf = input("Enter the output merged PDF file name (with .pdf extension): ")
            merge_pdfs(pdf_list, output_pdf)

        # Conditional statement that handles a user's request to rotate pdf files
        elif choice == '2':
            input_pdf = input("Enter the input PDF file name: ")
            output_pdf = input("Enter the output PDF file name (with .pdf extension): ")
            page_number = int(input("Enter the page number to rotate (0-indexed): "))
            rotation_angle = int(input("Enter rotation angle (90, 180, or 270 degrees): "))
            rotate_pdf(input_pdf, output_pdf, page_number, rotation_angle)

        # Conditional statement that handles a user's request to encrypt pdf files
        elif choice == '3':
            input_pdf = input("Enter the input PDF file name: ")
            output_pdf = input("Enter the output encrypted PDF file name (with .pdf extension): ")
            password = getpass.getpass("Enter a password to encrypt the PDF: ")
            encrypt_pdf(input_pdf, output_pdf, password)

        # Conditional statement that handles a user's request to decrypt pdf files
        elif choice == '4':
            input_pdf = input("Enter the input encrypted PDF file name: ")
            output_pdf = input("Enter the output decrypted PDF file name (with .pdf extension): ")
            password = getpass.getpass("Enter the password to decrypt the PDF: ")
            decrypt_pdf(input_pdf, output_pdf, password)

        # Conditional statement that handles a user's request to end the session
        elif choice == '5':
            print("Exiting the program.")
            break

        # Conditional statement that handles invalid user input
        else:
            print("Invalid choice, please try again.")


# Function that decypts an encrypted pdf file
def decrypt_pdf(input_pdf, output_pdf, password):

    pdf_reader = PyPDF2.PdfReader(input_pdf)

    if pdf_reader.is_encrypted:
        try:
            pdf_reader.decrypt(password)
        except:
            print("Failed to decrypt pdf. Password incorrect")
            return

        pdf_writer = PyPDF2.PdfWriter()
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)

    save_pdf(pdf_writer, output_pdf, 'decrypted')


# Function that encypts a pdf file
def encrypt_pdf(input_pdf, output_pdf, password):

    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    pdf_writer.encrypt(password)

    save_pdf(pdf_writer, output_pdf, 'encrypted')


# Function that merges two or more pdf files
def merge_pdf(pdfs, output_pdf):

    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdfs:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    save_pdf(pdf_writer, output_pdf, 'merged')


# Function that rotates a pdf file
def rotate_pdf(input_pdf, output_pdf, page_number, rotation_degree):

    pdf_reader = PyPDF2.PdfReader(input_pdf)
    pdf_writer = PyPDF2.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        if page_num == page_number:
            page.rotate(rotation_degree)
        pdf_writer.add_page(page)

    save_pdf(pdf_writer, output_pdf, 'rotated')


# Function that saves the modified pdf under the specified file name
def save_pdf(pdf_writer, output_pdf, action):

    with open(output_pdf, 'wb') as out_file:
        pdf_writer.write(out_file)
    print(f'PDF {action} and saved as {output_pdf}')



if __name__ == "__main__":
    main()

