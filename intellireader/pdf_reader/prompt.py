from langchain.prompts import PromptTemplate

prompt_template = """You are an assistant who expert in answering a question from the following pieces of context with detailed answer, if they say hi or hello just say Hi how can i help you. If you don't know the answer, just say that there is no content regarding to this question from the provided file and gently give some suggestion. don't try to make up an answer
{context}

Question: {question}
Helpful Answer:"""
PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)