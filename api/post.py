from http.server import BaseHTTPRequestHandler
import google.generativeai as genai
import requests
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # إعداد الذكاء الاصطناعي
        genai.configure(api_key=os.environ.get("GEMINI_KEY"))
        model = genai.GenerativeModel('gemini-pro')
        
        # توليد المحتوى
        prompt = "اكتب نصيحة تقنية لليوم باللغة العربية مع إيموجي"
        response = model.generate_content(prompt)
        content = response.text
        
        # إرسال لتليجرام
        token = os.environ.get("TELEGRAM_TOKEN")
        chat_id = os.environ.get("CHAT_ID")
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", 
                      data={"chat_id": chat_id, "text": content})

        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Done! Posted: {content}".encode())
      
