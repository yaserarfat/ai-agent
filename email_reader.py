import imaplib
import email
import os

def get_repair_emails():
     # Get email credentials from environment
    email_user = os.getenv("GMAIL_EMAIL")
    email_pass = os.getenv("GMAIL_PASSWORD")
    
    if not email_user or not email_pass:
        print("Missing email credentials in environment variables")
        return None
    
    try:

# Connect to Gmail
        server = imaplib.IMAP4_SSL("imap.gmail.com")
        server.login(email_user, email_pass)
        server.select("inbox")
        
        # Search for unread repair service emails
        result, email_ids = server.search(None, 'UNSEEN SUBJECT "repair service"')
        
        if not email_ids[0]:
            print("No new repair service emails found")
            server.close()
            server.logout()
            return None
        
        # Get the most recent email
        latest_email_id = email_ids[0].split()[-1]
        result, email_data = server.fetch(latest_email_id, "(RFC822)")
        
        # Parse the email
        email_message = email.message_from_bytes(email_data[0][1])
        
        # Extract email content
        email_body = ""
        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    email_body = part.get_payload(decode=True).decode('utf-8')
                    break
        else:
            email_body = email_message.get_payload(decode=True).decode('utf-8')
        
        # Clean up connection
        server.close()
        server.logout()
        
        return email_body.strip()
        
    except Exception as e:
        print(f"Error fetching emails: {e}")
        return None

