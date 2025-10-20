# Python Automation Tools

Collection of Python scripts for automating everyday tasks including file organization, backups, email sending, and web scraping.

## ✨ Features

- 📁 **File Organizer** - Automatically organize files by type and extension
- 💾 **Backup Manager** - Create and manage incremental backups
- 📧 **Email Sender** - Bulk email sending with personalization
- 🌐 **Web Scraper** - Extract data from websites easily
- 🛠️ **Utility Helpers** - Common helper functions for all tools

## 🚀 Quick Start

### Installation

1. Clone the repository:
```bash
git clone https://github.com/maxxunit1/python-automation-tools.git
cd python-automation-tools
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Requirements

- Python 3.7+
- See `requirements.txt` for package dependencies

## 📋 Tools Overview

### 1. File Organizer

Automatically organize files in a directory by their type and extension.

**Usage:**
```bash
python file_organizer.py --path /path/to/directory
```

**Options:**
- `--path` - Directory to organize (required)
- `--dry-run` - Preview changes without moving files
- `--undo` - Undo previous organization
- `--verbose` - Enable detailed logging

**Supported File Types:**
- Images: jpg, png, gif, svg, webp, ico
- Documents: pdf, doc, docx, txt, xlsx, pptx
- Videos: mp4, avi, mkv, mov, webm
- Audio: mp3, wav, flac, aac, ogg
- Archives: zip, rar, 7z, tar, gz
- Code: py, js, html, css, java, cpp
- And many more...

**Examples:**
```bash
# Preview organization
python file_organizer.py --path ~/Downloads --dry-run

# Organize files
python file_organizer.py --path ~/Downloads

# Undo organization
python file_organizer.py --path ~/Downloads --undo
```

### 2. Backup Manager

Create and manage file and directory backups with incremental support.

**Usage:**
```bash
python backup_manager.py --source /path/to/source --dest /path/to/backups
```

**Options:**
- `--source` - Source path to backup (required)
- `--dest` - Destination for backups (required)
- `--incremental` - Create incremental backup (only changed files)
- `--list` - List all available backups

**Features:**
- Full and incremental backups
- Automatic timestamping
- Easy restore functionality
- Conflict resolution

**Examples:**
```bash
# Create full backup
python backup_manager.py --source ~/Documents --dest ~/Backups

# Create incremental backup
python backup_manager.py --source ~/Documents --dest ~/Backups --incremental

# List all backups
python backup_manager.py --source ~/Documents --dest ~/Backups --list
```

### 3. Email Sender

Send bulk emails with personalization support via SMTP.

**Usage:**
```python
from email_sender import EmailSender

sender = EmailSender(
    smtp_server='smtp.gmail.com',
    smtp_port=587,
    username='your-email@gmail.com',
    password='your-password'
)

# Send single email
sender.send_email(
    to_addresses=['recipient@example.com'],
    subject='Hello',
    body='Email body here'
)

# Send bulk emails with personalization
recipients = [
    {'email': 'user1@example.com', 'name': 'John'},
    {'email': 'user2@example.com', 'name': 'Jane'}
]

template = "Hello {name}, this is a personalized email!"
sender.send_bulk_emails(recipients, 'Subject', template)
```

**Features:**
- SMTP support (Gmail, Outlook, custom servers)
- HTML email support
- Bulk sending with personalization
- Error handling and retry logic

### 4. Web Scraper

Extract data from websites using BeautifulSoup.

**Usage:**
```python
from web_scraper import WebScraper

scraper = WebScraper('https://example.com', delay=1.0)

# Fetch and parse page
soup = scraper.fetch_page('https://example.com/page')

# Extract specific data
data = scraper.extract_data(
    'https://example.com',
    {
        'titles': 'h1, h2',
        'paragraphs': 'p',
        'links': 'a'
    }
)

# Save to JSON
scraper.save_to_json(data, 'output.json')
```

**Features:**
- Automatic rate limiting
- CSS selector support
- JSON export
- Session management
- User-agent rotation

## 🛠️ Utility Functions

The `utils` package provides common helper functions:

```python
from utils import format_bytes, ensure_directory, get_file_hash

# Format file size
size = format_bytes(1024000)  # "1.00 MB"

# Ensure directory exists
path = ensure_directory('data/output')

# Calculate file hash
hash_value = get_file_hash('file.txt', algorithm='sha256')
```

## 📦 Dependencies

```txt
requests>=2.28.0
beautifulsoup4>=4.11.0
python-dotenv>=1.0.0
pytest>=7.2.0
colorama>=0.4.6
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file for sensitive configuration:

```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USERNAME=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
```

### Gmail Setup

For Gmail, you need to:
1. Enable 2-factor authentication
2. Generate an App Password
3. Use the App Password in your configuration

## 📚 Examples

### File Organization Workflow

```bash
# 1. Preview what will happen
python file_organizer.py --path ~/Downloads --dry-run

# 2. Organize files
python file_organizer.py --path ~/Downloads

# 3. If needed, undo
python file_organizer.py --path ~/Downloads --undo
```

### Backup Workflow

```bash
# Daily backup
python backup_manager.py --source ~/Projects --dest ~/Backups --incremental

# Weekly full backup
python backup_manager.py --source ~/Projects --dest ~/Backups
```

## 🧪 Testing

Run tests with pytest:

```bash
pytest
```

Run specific test:

```bash
pytest tests/test_file_organizer.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Thanks to the Python community for excellent libraries
- BeautifulSoup for web scraping
- Colorama for terminal colors

## 📞 Contact

Project Link: https://github.com/maxxunit1/python-automation-tools

---

**Made with ❤️ for automation enthusiasts**


## Update 2025-10-12 02:34:30
# Enhanced: 2025-10-12 02:34:30
"""Documentation updated"""

## Update 2025-10-18 14:22:40
# Enhanced: 2025-10-18 14:22:40
"""Documentation updated"""

## Update 2025-10-20 11:10:21
async def async_operation():
    """Async operation support"""
    result = await fetch_data()
    return process(result)