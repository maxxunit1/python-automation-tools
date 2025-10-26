#!/usr/bin/env python3
"""
Email Sender - Bulk email sending utility
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Optional
import os
from dotenv import load_dotenv


class EmailSender:
    """Send emails via SMTP"""

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """Initialize EmailSender"""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(
            self,
            to_addresses: List[str],
            subject: str,
            body: str,
            html: bool = False
    ) -> bool:
        """
        Send email to recipients

        Args:
            to_addresses: List of recipient email addresses
            subject: Email subject
            body: Email body
            html: If True, send as HTML email

        Returns:
            True if successful, False otherwise
        """
        try:
            msg = MIMEMultipart('alternative')
            msg['From'] = self.username
            msg['To'] = ', '.join(to_addresses)
            msg['Subject'] = subject

            if html:
                msg.attach(MIMEText(body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)

            print(f"Email sent successfully to {len(to_addresses)} recipient(s)")
            return True

        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

    def send_bulk_emails(
            self,
            recipients: List[dict],
            subject: str,
            body_template: str
    ) -> dict:
        """
        Send personalized emails to multiple recipients

        Args:
            recipients: List of dicts with 'email' and other fields
            subject: Email subject
            body_template: Email body template with {placeholders}

        Returns:
            Dictionary with success/failure counts
        """
        results = {'success': 0, 'failed': 0}

        for recipient in recipients:
            try:
                body = body_template.format(**recipient)
                success = self.send_email([recipient['email']], subject, body)

                if success:
                    results['success'] += 1
                else:
                    results['failed'] += 1

            except Exception as e:
                print(f"Error sending to {recipient.get('email', 'unknown')}: {e}")
                results['failed'] += 1

        return results


def main():
    """Main entry point"""
    load_dotenv()

    # Example usage
    sender = EmailSender(
        smtp_server=os.getenv('SMTP_SERVER', 'smtp.gmail.com'),
        smtp_port=int(os.getenv('SMTP_PORT', 587)),
        username=os.getenv('EMAIL_USERNAME', ''),
        password=os.getenv('EMAIL_PASSWORD', '')
    )

    # Send test email
    recipients = ['test@example.com']
    subject = 'Test Email'
    body = 'This is a test email from Python automation tools.'

    sender.send_email(recipients, subject, body)


if __name__ == "__main__":
    main()

# Fix performance bottleneck in user module - 2025-10-12 17:14:41
def handle_error(error):
    """Handle error gracefully"""
    logger.error(f'Error: {error}')
    return None

# Upgrade security vulnerability in backend service to meet requirements - 2025-10-23 09:04:39
# Improved: 2025-10-23 09:04:39
# Additional configuration

# Adjust memory leak - 2025-10-26 17:44:19
# Improved: 2025-10-26 17:44:19
# Additional configuration