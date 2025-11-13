🩺 MediBot Pro: AI Healthcare Assistant

Ek intelligent, dual-mode AI chatbot jo healthcare assistance ke liye design kiya gaya hai. Yeh general health advice de sakta hai aur aapke upload kiye gaye medical documents (jaise lab reports) se specific sawal-jawab bhi kar sakta hai.

(Yahan screenshot link daalein. Aap apne app ka screenshot le kar, use GitHub par upload karke, uska link yahan paste kar sakte hain.)

🌟 Key Features (Mukhya Visheshtayein)

Dual-Mode AI: Do alag-alag mode mein kaam karta hai.

General Health Advice: Symptoms, wellness tips, ya home remedies ke baare mein sawal poochein. AI aapko general jaankari dega.

RAG (Retrieval-Augmented Generation):

Aap ek ya ek se zyada medical PDFs (Jaise Blood Report, WHO guidelines) upload kar sakte hain.

Bot sirf us PDF ke andar di gayi jaankari ke adhaar par hi aapke sawalon ka jawab dega.

Interactive UI: Streamlit ka use karke ek saaf-suthra aur aasaan chat interface banaya gaya hai.

Session History: Aapki poori baat-cheet ko yaad rakhta hai.

🛠️ Tech Stack (Istemal Ki Gayi Technology)

Language: Python 3.11

AI Model: Google Gemini API (gemini-2.0-flash)

Framework: LangChain (RAG pipeline ke liye)

User Interface (UI): Streamlit

Vector Database: FAISS (Text ko search-friendly banane ke liye)

PDF Processing: PyPDF2

🚀 Ise Apne Computer Par Kaise Chalayein (Local Setup)

Is project ko apne local machine par run karne ke liye yeh steps follow karein:

1. Repository Clone Karein (Code Download Karein):

git clone [https://github.com/anishTechie/HealthBot.git](https://github.com/anishTechie/HealthBot.git)


2. Folder Mein Jayein:

cd HealthBot


3. Virtual Environment Banayein (Recommended):

python -m venv myenv


4. Environment Activate Karein:

Windows par:

.\myenv\Scripts\activate


Mac/Linux par:

source myenv/bin/activate


5. Zaroori Libraries Install Karein:
(Humne pehle se requirements.txt file bana li hai.)

pip install -r requirements.txt


6. Apni API Key Daalein:

app.py file ko code editor mein kholein.

Line 19 par jayein aur "YAHAN_APNI_API_KEY_PASTE_KAREIN" ki jagah apni Google Gemini API Key daalein.

7. App Run Karein!

python -m streamlit run app.py


Aapka browser khul jayega aur chatbot taiyar hoga!

🌐 Ise Internet Par Live Kaise Karein (Deployment)

Yeh app Streamlit Community Cloud par deploy karne ke liye taiyar hai.

Apne code ko GitHub par push karein (Yeh aap kar chuke hain).

share.streamlit.io par jayein aur apne GitHub account se login karein.

"Deploy an app" par click karein aur apni HealthBot repository chunein.

Sabse Zaroori: "Advanced settings..." mein, aapko apni API Key daalni hogi.

Secrets section mein jayein.

Neeche di gayi line ko copy karein aur paste karein (Apni key ke saath):

GOOGLE_API_KEY = "AIzaSy..."


Deploy! par click karein.

Kuch hi der mein aapko ek public link mil jayega (jaise healthbot.streamlit.app) jise aap kisi ke bhi saath share kar sakte hain.

⚠️ Disclaimer

Important: Yeh chatbot ek AI-powered educational tool hai aur professional medical advice, diagnosis, ya treatment ka substitute nahi hai. Kisi bhi health samasya ke liye hamesha ek qualified healthcare provider se salaah lein.