import torch

# --- Device Settings ---
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# --- Model Settings ---
WHISPER_MODEL = "base"
TTS_MODEL = "tts_models/multilingual/multi-dataset/xtts_v2"
OLLAMA_BASE_URL = "http://127.0.0.1:11434/"
OLLAMA_MODEL = "codellama:7b"

# --- Audio Settings ---
SAMPLERATE = 16000
CHANNELS = 1
DTYPE = 'int16'
BLOCKSIZE = 1024

# --- FAQ Context ---
FAQ_TEXT = """
About Us

Our company was established with the mission to provide innovative products and services in the technology sector. Our headquarters are located at 123 Tech Avenue, in the heart of Silicon Valley, California. With a team of experienced and dedicated professionals, we strive to meet our customers’ needs in the best possible way.

Business Hours

Our office is open Monday through Friday, from 9 AM to 5 PM for in-person services. We are closed on weekends and public holidays. However, our customer support team is available 24/7 via email and phone.

Customer Support

We understand the importance of staying connected with our customers. Our support team is always ready to assist you with any questions, issues, or suggestions. You can contact us via email at support@example.com or by calling our toll-free number at 1-800-555-1234.

Order and Shipping Tracking

Once your order is placed, you will receive an email with a tracking number that allows you to monitor your shipment on the courier’s website.

Return Policy

Your satisfaction is our priority. If you are not completely satisfied with your purchase, you can return the product within 30 days of purchase for a full refund. Please ensure the product is in new condition and in its original packaging, accompanied by the original receipt.
"""