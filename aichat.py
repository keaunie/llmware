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






from llmware.library import Library
from llmware.retrieval import Query
import gradio as gr
import re

# Load your library
lib = Library().load_library("oneluxstay_docs")
q = Query(lib)

# Clean-up function
def clean_text(text):
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    text = text.replace("•", "-").replace("●", "-").replace("○", "-")
    return text.strip()

# Chat function
def chatbot_response(user_input):
    results = q.text_query(user_input, result_count=2)
    if results:
        return "\n\n".join([clean_text(r["text"]) for r in results])
    else:
        return "Sorry, I couldn't find anything relevant."

# Gradio UI
gr.Interface(fn=chatbot_response, inputs="text", outputs="text", title="OneLuxStay Concierge Assistant").launch()
