from langchain_community.document_loaders import TextLoader

loader = TextLoader(data/about_me.txt)
documents = loader.load()


