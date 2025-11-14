# 🩺 MediBot: AI Healthcare Assistant

**MediBot** is an intelligent, dual-mode AI chatbot designed to assist with healthcare queries. It utilizes Google's Gemini API to provide general health advice and implements a RAG (Retrieval-Augmented Generation) pipeline to answer specific questions based on uploaded medical documents (PDFs).

## 🌟 Key Features

- **Dual-Mode AI:** Switch seamlessly between General Health advice and Document Analysis.
- **RAG Technology:** Upload medical PDFs (e.g., lab reports, guidelines) to get answers strictly based on the document's content.
- **Interactive UI:** Built with **Streamlit** for a clean and responsive user experience.
- **Session Memory:** Retains conversation history for contextual interactions.

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **AI Model:** Google Gemini API (`gemini-2.0-flash`)
- **Frameworks:** LangChain, Streamlit
- **Vector Database:** FAISS
- **PDF Processing:** PyPDF2

## 🚀 Local Installation

Follow these steps to set up the project locally:

**1. Clone the Repository**
```bash
git clone [https://github.com/anishTechie/HealthBot.git](https://github.com/anishTechie/HealthBot.git)
cd HealthBot