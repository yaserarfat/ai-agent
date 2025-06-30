Automatically reads unread Gmail emails (filtered by subject)
Extracts:
  - Customer **mobile number**
  - Customer **name**
  - List of **questions**
  - Uses **LLaMA3.2 via Ollama** for parsing & replying
  - Sends WhatsApp replies using **Twilio Sandbox**

---

## 🛠️ Tech Stack

- Python
- LangChain + LLaMA3 via Ollama (if use ollama it should be locall on your machine)
- Twilio WhatsApp API
- IMAP (for reading Gmail)
- `.env` file for credentials


1. Clone or Prepare Your Project Directory
------------------------------------------
git clone <https://github.com/yaserarfat/ai-agent>
cd ai-whatsapp-agent
Or create a folder and copy your code files into it.
2. Install Required Python Packages
-----------------------------------
Create and activate a virtual environment (optional but recommended):
 python -m venv venv
 source venv/bin/activate # On Windows: venv\Scripts\activate
Install the dependencies:
 pip install -r requirements.txt
3. Create a .env File
---------------------
In the project root, create a file named `.env` and add:
 GMAIL_EMAIL=your@gmail.com
 GMAIL_PASSWORD=your_app_password
 TWILIO_ACCOUNT_SID=your_twilio_sid
 TWILIO_AUTH_TOKEN=your_twilio_token
 TWILIO_FROM_NUMBER=+14155238886
 TO_WHATSAPP_NUMBER=+91XXXXXXXXXX


4. Pull the LLaMA3 Model Using Ollama
-------------------------------------
Install Ollama from https://ollama.com
Then run:
 ollama pull llama3.2
To test:
 ollama run llama3.2
5. Connect to Twilio Sandbox
----------------------------
- Go to https://www.twilio.com/console/sms/whatsapp/sandbox
- Follow the instructions to connect your WhatsApp number


6. Run the Agent
----------------
Run the script:
 python main.py
It will read email, generate reply using LLM, and send it to WhatsApp.