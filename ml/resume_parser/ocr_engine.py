import re
import fitz # PyMuPDF
import logging

logger = logging.getLogger(__name__)

class OCREngine:
    """Handles scanned resume documents and image-based PDFs."""
    
    @classmethod
    def extract_text_from_scanned_pdf(cls, file_path: str) -> str:
        text = ""
        try:
            doc = fitz.open(file_path)
            for page in doc:
                # First try regular extraction
                page_text = page.get_text()
                if page_text and len(page_text.strip()) > 50:
                    text += page_text + "\n"
                else:
                    # If page contains little/no text, it is likely a scanned image page
                    try:
                        import pytesseract
                        from PIL import Image
                        import io
                        
                        pix = page.get_pixmap(dpi=200)
                        img = Image.open(io.BytesIO(pix.tobytes("png")))
                        ocr_text = pytesseract.image_to_string(img)
                        text += ocr_text + "\n"
                    except Exception as ocr_err:
                        logger.warning(f"Tesseract OCR fallback skipped on page {page.number}: {ocr_err}")
                        text += page_text + "\n"
        except Exception as e:
            logger.error(f"Error executing OCR on PDF {file_path}: {e}")
            raise e
            
        return text.strip()
