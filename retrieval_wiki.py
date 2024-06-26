import llm_check
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

llm_check.check_and_pull_nomic_embed_text()
llm_check.check_and_pull_llama2()
    
# Embedding documents with Ollama using Nomic-embed-text
embedding=OllamaEmbeddings(model='nomic-embed-text')
db3 = Chroma(persist_directory="./VectorStore_Wiki", embedding_function=embedding)

#### RAG testing code ####
# qa_chain = RetrievalQA.from_chain_type(llm,retriever=db3.as_retriever())
# question = "What is capital city of Scotland?"
# result = qa_chain.invoke({"query": question})  # Updated to use 'invoke' as suggested by the deprecation warning
# print(result.get("result", "No result found."))  # Ensure there's a default value in case 'result' key doesn't exist