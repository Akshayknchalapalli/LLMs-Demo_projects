# export HNSWLIB_NO_NATIVE = 1
import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name='my_collection')

collection.add(
    documents=['my name is akshay', 'my name is not akshay'],
    metadatas=[{'source': 'name is true'}, {'source': 'name is false'}],
    ids=['id1', 'id2']
)


results = collection.query(
    query_texts=['what is my name?'],
    n_results=2
)

print(results)
