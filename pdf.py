from pypdf import PdfReader

reader = PdfReader(
    r"C:\Users\VICTUS\Downloads\NIPS-2017-attention-is-all-you-need-Paper.pdf"
)

# Print total pages
print("Total pages:", len(reader.pages))

# Extract PDF metadata
metadata = reader.metadata

if metadata:
    for key, value in metadata.items():
        print(key, ":", value)

# Extract text from every page
documents = []

for page_number, page in enumerate(reader.pages):
    text = page.extract_text() or ""

    documents.append({
        "page": page_number + 1,
        "text": text
    })

print("Extracted documents:", len(documents))
print(documents[0]["text"])