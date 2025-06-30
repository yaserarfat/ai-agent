import os
from dotenv import load_dotenv
from chain import build_chain
from email_reader import get_repair_emails

load_dotenv()

email_body = get_repair_emails()

if not email_body:
    print("❌ No email to process.")
    exit()

chain = build_chain()
result = chain.invoke({"email": email_body})

