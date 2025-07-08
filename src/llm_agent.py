from langchain_ollama import ChatOllama
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# Import configuration settings
import src.config as config

# Define the prompt template for the LLM
template = (
    "You are a polite and knowledgeable assistant designed to answer frequently asked questions.\n"
    "Please use the following information to respond to the user's question.\n"
    "FAQ context:\n{doc}\n"
    "user question:\n{question}\n"
    "Provide a concise and respectful answer based on the provided information."
    "Keep answer short"
)

human_prompt = HumanMessagePromptTemplate.from_template(template)
chat_prompt = ChatPromptTemplate.from_messages([human_prompt])

def ask_llm(text, faq_context=config.FAQ_TEXT):
    """
    Sends the transcribed text to the LLM and returns its response.
    Uses the FAQ_TEXT from config as context.
    """
    llm = ChatOllama(
        base_url=config.OLLAMA_BASE_URL,
        model=config.OLLAMA_MODEL,
        temperature=0.5,
        max_tokens=100, # Increased max_tokens for potentially longer answers
    )

    try:
        # Format the prompt with the user's question and FAQ context
        messages = chat_prompt.format_prompt(question=text, doc=faq_context).to_messages()
        response = llm(messages)
        return response.content
    except Exception as e:
        print(f"Error interacting with LLM: {e}")
        return "I'm sorry, I couldn't process your request at the moment."