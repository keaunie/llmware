
# 🧠 OneLuxStay Concierge Chatbot (Powered by LLMWare + Ollama)

This project is a fully local, open-source RAG (Retrieval-Augmented Generation) chatbot built for OneLuxStay. It uses [LLMWare](https://github.com/llmware-ai/llmware) to parse and retrieve content from PDFs, and [Ollama](https://ollama.com) to run a local LLM (Mistral) for natural, conversational answers.

---

## 🚀 Features

- 📄 Parses PDFs like property guides, FAQs, and brand manuals  
- 🔍 Retrieves relevant chunks using LLMWare  
- 🧠 Generates elegant answers using Mistral via Ollama  
- 💬 Chat interface built with Gradio  
- 💻 100% local — no API keys or cloud services required  

---

## 🧰 Requirements

- Windows 10/11 or macOS/Linux  
- Python 3.10+  
- Git (optional)  
- [Ollama](https://ollama.com/download) (for running Mistral locally)  

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/keaunie/llmware.git
cd llmware
```

### 2. Set Up Python Environment

```bash
pip install llmware gradio requests
```

### 3. Install and Run Ollama

- Download and install from [ollama.com/download](https://ollama.com/download)  
- Open a terminal and run:

```bash
ollama pull mistral
ollama run mistral
```

> ⚠️ Keep this terminal open — it runs the local LLM server on port `11434`.

---

## 📂 Add Your PDFs

Place your documents (e.g. `OneLuxStaySummary.pdf`) inside a folder named `docs/` in the project root.

---

## 🧠 Index Your Documents

Run this script once to parse and index your PDFs:

```python
from llmware.library import Library

lib = Library().create_new_library("oneluxstay_docs")
lib.add_files(input_folder_path="./docs", strip_unicode=True)
```

---

## 💬 Launch the Chatbot

Run the chatbot interface:

```bash
python aichat.py
```

Ask questions like:
- “What are the brand pillars of OneLuxStay?”
- “What promotions are currently available?”

---

## 🖤 Custom Styling (Coming Soon)

We'll be adding a black-and-gold luxury UI theme to match the OneLuxStay brand.

---

## 🧩 Credits

- [LLMWare](https://github.com/llmware-ai/llmware) for document parsing and retrieval  
- [Ollama](https://ollama.com) for running local LLMs  
- [Gradio](https://gradio.app) for the chat interface  

---

## 📌 Notes

- Performance may be slow on CPU-only machines. For faster results, use a GPU or try smaller models like `llama2` or `gemma`.  
- Ollama must be running in the background for the chatbot to work.  

---

## 🛠️ Maintained by

**Keaunie**  
Luxury branding & AI automation enthusiast  
[github.com/keaunie](https://github.com/keaunie)
```

You can now paste this directly into the GitHub editor at [this link](https://github.com/keaunie/llmware/new/main?filename=README.md) and click **“Commit new file”** to publish it.

Want me to help you add a screenshot or badge section next?
