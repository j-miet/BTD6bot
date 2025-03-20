"""Creates a new easyocr reader.

Reader takes a bit to load up. Only a single one is necessary so this loading process happens only once.

No mypy type hints available for easyocr so either 'Reader' or 'Any' is used with Reader objects.
"""

import easyocr # type: ignore

OCR_READER: easyocr.Reader = easyocr.Reader(['en'], verbose=False)
"""Current easyocr reader for english language text."""