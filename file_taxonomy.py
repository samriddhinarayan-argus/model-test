from langchain_core.messages import SystemMessage, HumanMessage
from langchain_ollama import ChatOllama
from datetime import datetime
print(datetime.now())

llm = ChatOllama(
    model="gemma3:4b",
    temperature=0,
)

messages = [
    SystemMessage(
        content=(
            "You are an expert taxonomist and document organizer.\n"
            "Your task is to analyze a list of filenames and propose a logical "
            "folder structure (taxonomy) to categorize them based on their names.\n"
            "You must return the proposed taxonomy as a JSON list of objects, "
            "where each object has a 'name' and a 'description'."
        )
    ),
    HumanMessage(
        content=(
            "Analyze the following document samples and propose a logical, "
            "mutually exclusive set of categories to organize them.\n"
            "Create ONLY as many categories as strictly necessary to cover "
            "the provided files. Do not invent extra categories for documents "
            "that are not present in the samles.\n"
            "Keep the taxonomy concise (create between 1 and 5 categories "
            "based on the variety of documents).\n\n"
            "Format your response exactly as valid JSON:\n"
            '[\n'
            '  {"name": "Category Name", '
            '"description": "What belongs in this category"}\n'
            ']\n\n'
            """Document Samples:\n--- Document 1 ---
--- DOCUMENT: finance.txt ---
--- BEGINNING ---
Monthly Finance Summary
Accounts payable this month totaled $58,200 across 14 vendor invoices. Two invoices remain unpaid and are flagged for follow-up with the vendor. The finance team will reconcile these against the general ledger on Friday.
--- END ---


--- Document 2 ---
--- DOCUMENT: cooking.txt ---
--- BEGINNING ---
Weekend Pasta Recipe
Boil a large pot of salted water and cook the pasta until al dente. While it cooks, saute garlic in olive oil, then toss everything together with fresh basil and a generous amount of parmesan cheese.
--- END ---


--- Document 3 ---
--- DOCUMENT: budget_q2.txt ---
--- BEGINNING ---
Q2 Budget Review
Departmental spending exceeded projections by 6%, largely driven by increased marketing spend. The CFO has requested a revised forecast before the next board meeting to account for the overage.
--- END ---


--- Document 4 ---
--- DOCUMENT: baking.txt ---
--- BEGINNING ---
Sourdough Starter Guide
Feed your starter equal parts flour and water every 24 hours at room temperature. Once it doubles in size within 4-6 hours of feeding, it's active enough to use for baking bread.
--- END ---


--- Document 5 ---
--- DOCUMENT: expense_report.txt ---
--- BEGINNING ---
Travel Expense Report
Employee submitted receipts for airfare, hotel, and meals totaling $1,240 for the client visit last week. Reimbursement is pending manager approval and should be processed within 5 business days.
--- END ---"""
        )
    ),
]

response = llm.invoke(messages)

print(response.content)

print(datetime.now())
