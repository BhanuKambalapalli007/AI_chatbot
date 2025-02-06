from langgraph.graph import Graph
from transformers import pipeline
from sqlalchemy.orm import Session
from .models import Product, Supplier


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def fetch_products(query: str, db):
    products = db.query(Product).filter(Product.name.ilike(f"%{query}%")).all()
    return products

def summarize_supplier(supplier_id: int, db):
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    summary = summarizer(supplier.contact_info, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

workflow = Graph()

@workflow.node
def retrieve_data(query: str, db):
    return fetch_products(query, db)

@workflow.node
def summarize_data(supplier_id: int, db):
    return summarize_supplier(supplier_id, db)

@workflow.edge
def process_query(query: str, db):
    products = retrieve_data(query, db)
    for product in products:
        summary = summarize_data(product.supplier_id, db)
        product.supplier_summary = summary
    return products