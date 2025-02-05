import langgraph
from langchain.llms import HuggingFaceHub
from crud import get_product_details, get_suppliers_by_category
from database import SessionLocal

llm = HuggingFaceHub(repo_id="meta-llama/Llama-2-7b-chat")

def fetch_product_info(query):
    db = SessionLocal()
    product = get_product_details(db, query)
    db.close()
    if product:
        return f"Product: {product.name}, Price: {product.price}, Supplier: {product.supplier.name}"
    return "No product found."

def fetch_supplier_info(query):
    db = SessionLocal()
    suppliers = get_suppliers_by_category(db, query)
    db.close()
    if suppliers:
        return f"Suppliers for {query}: {', '.join(s.name for s in suppliers)}"
    return "No suppliers found."

graph = langgraph.Graph()
graph.add_node("fetch_product_info", fetch_product_info)
graph.add_node("fetch_supplier_info", fetch_supplier_info)

graph.add_edge("fetch_product_info", "fetch_supplier_info")

graph.set_entry_point("fetch_product_info")

def query_chatbot(user_query):
    return graph.run(user_query)
