# from llmware.library import Library
# from llmware.retrieval import Query

# # Load your library

# lib = Library().load_library("oneluxstay_docs")



# # Create a query object
# q = Query(lib)

# # Run a query
# results = q.text_query("What are the featured destinations?", result_count=3)

# # Print the results
# for r in results:
#     print(r["text"])






# from llmware.library import Library
# from llmware.retrieval import Query
# import gradio as gr
# import re

# # Load your library
# lib = Library().load_library("oneluxstay_docs")
# q = Query(lib)

# # Clean-up function
# def clean_text(text):
#     text = re.sub(r'[^\x00-\x7F]+', '', text)
#     text = text.replace("•", "-").replace("●", "-").replace("○", "-")
#     return text.strip()

# # Chat function
# def chatbot_response(user_input):
#     results = q.text_query(user_input, result_count=2)
#     if results:
#         return "\n\n".join([clean_text(r["text"]) for r in results])
#     else:
#         return "Sorry, I couldn't find anything relevant."

# # Gradio UI
# gr.Interface(fn=chatbot_response, inputs="text", outputs="text", title="OneLuxStay Concierge Assistant").launch()



# import gradio as gr
# import requests
# from llmware.library import Library
# from llmware.retrieval import Query

# # Load your parsed PDF library
# lib = Library().load_library("oneluxstay_docs")
# q = Query(lib)

# # Clean up weird characters
# def clean_text(text):
#     return text.replace("•", "-").replace("●", "-").replace("○", "-").encode("ascii", "ignore").decode()

# # Send prompt to Mistral via Ollama
# def ask_mistral(prompt):
#     response = requests.post(
#         "http://localhost:11434/api/generate",
#         json={
#             "model": "mistral",
#             "prompt": prompt,
#             "stream": False
#         }
#     )
#     return response.json()["response"]

# # Full chatbot logic
# def chatbot_response(user_input):
#     results = q.text_query(user_input, result_count=3)
#     context = "\n".join([clean_text(r["text"]) for r in results])
#     prompt = f"Answer the following question using the context below:\n\nContext:\n{context}\n\nQuestion: {user_input}\nAnswer:"
#     return ask_mistral(prompt)

# # Gradio UI
# gr.Interface(fn=chatbot_response, inputs="text", outputs="text", title="OneLuxStay Concierge Assistant").launch()


from llmware.library import Library
from llmware.retrieval import Query
import gradio as gr
import re
import requests

# Load your library
lib = Library().load_library("oneluxstay_docs")
q = Query(lib)

def clean_text(text):
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    text = text.replace("•", "-").replace("●", "-").replace("○", "-")
    return text.strip()

def ask_mistral(prompt):
    print("\n--- Prompt sent to Mistral ---\n", prompt)
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    print("--- Raw response from Mistral ---\n", response.json())
    return response.json().get("response", "[No response from Mistral]")

# Chat function for Gradio ChatInterface
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Type your message here...")
    clear = gr.Button("Clear")

    def respond(message, chat_history):
        results = q.text_query(message, result_count=2)
        context = "\n".join([clean_text(r["text"]) for r in results])
        prompt = (
            "You are OneLuxStay's helpful, friendly concierge assistant. Use the context below to answer the user's question conversationally and naturally. "
            "Do not just repeat the context—give a clear, helpful answer. If you don't know, say so honestly.\n\n"
            f"Context:\n{context}\n\nUser: {message}\nAssistant:"
        )
        answer = ask_mistral(prompt)
        chat_history = chat_history + [[message, answer.strip()]]
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()
