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
            "Analyze the following list of filenames and propose a logical, "
            "mutually exclusive set of categories to organize them.\n"
            "Create ONLY as many categories as strictly necessary to cover "
            "the provided files. Do not invent extra categories for files "
            "that are not present.\n"
            "Keep the taxonomy concise (create between 1 and 10 categories "
            "based on the variety of files).\n\n"
            "Format your response exactly as valid JSON:\n"
            '[\n'
            '  {"name": "Category Name", '
            '"description": "What belongs in this category"}\n'
            ']\n\n'
            "Files to classify based on filenames: invoice_march_2024.pdf, invoice_april_2024.pdf, photo_beach_trip.jpg, photo_birthday_party.jpg,resume_john_doe.docx,cover_letter_john_doe.docx,receipt_grocery_store.png,photo_family_dinner.jpg,invoice_may_2024.pdf,resume_updated_2024.docx"
        )
    ),
]

response = llm.invoke(messages)

print(response.content)
print(datetime.now())
