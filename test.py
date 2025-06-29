from pathlib import Path

base_dir = Path(r"C:\Users\touse\OneDrive\Desktop\RAG\Avis-Jurisprudence")

print("📁 Directory exists:", base_dir.exists())
print("📂 Contents:")
for entry in base_dir.iterdir():
    print("   •", entry.name, "(Folder)" if entry.is_dir() else "(File)")

# Count PDFs (case-insensitive)
pdfs = list(base_dir.rglob("*.pdf"))
print(f"\n📄 PDFs found in directory (including subfolders): {len(pdfs)}")
for pdf in pdfs[:10]:  # show up to 10
    print("   →", pdf)
