from langchain_core.messages import SystemMessage, HumanMessage
from langchain_ollama import ChatOllama
from datetime import datetime

print(datetime.now())

llm = ChatOllama(
    model="gemma3:4b",
    temperature=0,
)

documents = [
    "DOCUMENT: budget_q2.txt --- --- BEGINNING --- Q2 Budget Review Departmental spending exceeded projections by 6%, largely driven by increased marketing spend. The CFO has requested a revised forecast before the next board meeting to account for the overage. --- END ---",
    "DOCUMENT: baking.txt --- --- BEGINNING --- Sourdough Starter Guide Feed your starter equal parts flour and water every 24 hours at room temperature. Once it doubles in size within 4-6 hours of feeding, it's active enough to use for baking bread. --- END ---",
    "DOCUMENT: expense_report.txt --- --- BEGINNING --- Travel Expense Report Employee submitted receipts for airfare, hotel, and meals totaling $1,240 for the client visit last week. Reimbursement is pending manager approval and should be processed within 5 business days. --- END ---"
]

for doc in documents:
    messages = [
        SystemMessage(
            content=(
                """You are a highly accurate document classifier.
Your task is to assign the provided document to ONE of the allowed categories based on the provided taxonomy.
Return ONLY the exact name of the category. If the document does not fit any category, return 'Uncategorized'. No explanation.
"""        )
        ),
        HumanMessage(
            content=(
                f"""Allowed Categories:
- Finance and Expenses: Documents related to financial transactions, accounts payable, expense reports, and reconciliation processes
- Budgeting: Documents detailing budget reviews, spending variances, and forecast revisions
- Recipes: Documents containing cooking and baking instructions, including both general recipes and starter guides
- Uncategorized: For documents that do not fit into any of the above categories.

Document excerpt:
{doc}
"""
            )
        ),
    ]

    response = llm.invoke(messages)
    print(response.content)
print(datetime.now())
