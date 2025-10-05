from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

template = """
You are an exeprt in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n------------------------------------")
    question = input("Enter your question about pizza restaurants (or 'exit' to quit): ")
    print("\n\n")
    if question.lower() == 'exit':
        break

    result = chain.invoke({"reviews": [], "question": question})
    print(result)