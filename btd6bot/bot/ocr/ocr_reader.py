"""Creates a new easyocr reader.

Reader might take a bit to load up if you have older pc. Only a single one is necessary so this loading process happens 
only once each session.
"""
import warnings

import easyocr

from bot import _maindata

# PyTorch gives the following warning if no CUDA support is detected:
# OSError: [WinError 1114] A dynamic link library (DLL) initialization routine failed.
# This message is just a warning message and it does not affect ocr operations. Following filter will mute this alert
# and prevents it from getting displayed in the console window.
warnings.filterwarnings("ignore", message=".*pin_memory.*")

OCR_READER: easyocr.Reader = easyocr.Reader(lang_list=['en'], 
                                            gpu=_maindata.maindata["bot_vars"]["use_gpu"], 
                                            verbose=False, 
                                            quantize=False)
"""Easyocr reader for english language text with gpu support disabled.

On windows platforms, you can set quantize=True to test if it improves ocr accuracy.
"""