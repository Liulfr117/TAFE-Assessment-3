import unittest
from unittest.mock import patch, mock_open, MagicMock
from PyPDF2 import PdfWriter, PdfReader

# Import the functions to test
from part_a import merge_pdf, rotate_pdf, encrypt_pdf, decrypt_pdf, save_pdf

class TestPdfOperations(unittest.TestCase):

    @patch('PyPDF2.PdfWriter.write')
    def test_save_pdf(self, mock_write):
        # Mock PdfWriter object
        pdf_writer = PdfWriter()
        output_pdf = "output_test.pdf"

        # Call the save_pdf function
        with patch("builtins.open", mock_open()) as mocked_file:
            save_pdf(pdf_writer, output_pdf, 'test_action')
            mocked_file.assert_called_once_with(output_pdf, 'wb')
            mock_write.assert_called_once()


    @patch('PyPDF2.PdfWriter')
    @patch('PyPDF2.PdfReader')
    def test_merge_pdfs(self, MockPdfReader, MockPdfWriter):
        # Create the mock instances
        mock_writer = MockPdfWriter.return_value  # Mock instance for PdfWriter
        mock_reader1 = MagicMock()  # Mock instance for the first PDF reader
        mock_reader2 = MagicMock()  # Mock instance for the second PDF reader

        # Setting up the mock readers to simulate pages
        mock_reader1.pages = [MagicMock(), MagicMock()]  # 2 pages in first PDF
        mock_reader2.pages = [MagicMock()]  # 1 page in second PDF

        # Setup the side effects for PdfReader to return the correct mock readers
        MockPdfReader.side_effect = [mock_reader1, mock_reader2]

        pdfs = ["file1.pdf", "file2.pdf"]
        output_pdf = "merged_output.pdf"

        # Call the merge_pdf function
        merge_pdf(pdfs, output_pdf)

        # Check that add_page was called for each page
        self.assertEqual(mock_writer.add_page.call_count, 3)  # Total 3 pages
        mock_writer.write.assert_called_once()


    @patch('PyPDF2.PdfReader')
    @patch('PyPDF2.PdfWriter')
    def test_rotate_pdf(self, MockPdfWriter, MockPdfReader):
        pdf_writer = MockPdfWriter.return_value
        pdf_reader = MockPdfReader.return_value

        # Creating mock pages with the rotate method
        mock_page1 = MagicMock()
        mock_page2 = MagicMock()
        mock_page3 = MagicMock()

        pdf_reader.pages = [mock_page1, mock_page2, mock_page3]  # 3 pages

        input_pdf = "input.pdf"
        output_pdf = "rotated_output.pdf"
        page_number = 0
        rotation_degree = 90

        rotate_pdf(input_pdf, output_pdf, page_number, rotation_degree)
        # Check that rotate was called on the correct page
        mock_page1.rotate.assert_called_once_with(rotation_degree)
        # Check that add_page was called for each page
        self.assertEqual(pdf_writer.add_page.call_count, 3)  # Total 3 pages
        pdf_writer.write.assert_called_once()

    @patch('PyPDF2.PdfReader')
    @patch('PyPDF2.PdfWriter')
    def test_encrypt_pdf(self, MockPdfWriter, MockPdfReader):
        pdf_writer = MockPdfWriter.return_value
        pdf_reader = MockPdfReader.return_value
        input_pdf = "input.pdf"
        output_pdf = "encrypted_output.pdf"
        password = "password123"

        encrypt_pdf(input_pdf, output_pdf, password)
        pdf_writer.encrypt.assert_called_once_with(password)
        pdf_writer.write.assert_called_once()

    @patch('PyPDF2.PdfReader')
    @patch('PyPDF2.PdfWriter')
    def test_decrypt_pdf(self, MockPdfWriter, MockPdfReader):
        pdf_writer = MockPdfWriter.return_value
        pdf_reader = MockPdfReader.return_value
        pdf_reader.is_encrypted = True
        input_pdf = "encrypted.pdf"
        output_pdf = "decrypted_output.pdf"
        password = "password123"

        # Simulating the decryption behavior
        pdf_reader.pages = [MagicMock(), MagicMock()]  # Simulating 2 pages

        with patch.object(pdf_reader, 'decrypt', return_value=True) as mock_decrypt:
            decrypt_pdf(input_pdf, output_pdf, password)
            mock_decrypt.assert_called_once_with(password)
            # Check that add_page was called for each page after decryption
            self.assertEqual(pdf_writer.add_page.call_count, 2)  # Total 2 pages
            pdf_writer.write.assert_called_once()

if __name__ == '__main__':
    unittest.main()
