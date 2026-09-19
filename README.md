🚀 **I Built a PDF Book Information & Summarization Tool using LangChain + Groq AI**

I recently built a small **RAG/LLM-based PDF processing project** that takes a PDF book, extracts its content, and uses an LLM to generate structured information about the book.

### 🔍 What my project does

The workflow is:

**PDF → Text Extraction → LLM → Structured JSON Output**

The system extracts information such as:

📖 **Book Name**
✍️ **Author**
📅 **Published Year**
📝 **Book Summary**
💡 **Important Notes**

For the output structure, I used **Pydantic**, which helps make the LLM response consistent and structured instead of returning random text.

### 🛠️ Technologies I used

• Python
• LangChain
• PyPDFLoader
• Groq API
• `openai/gpt-oss-120b`
• Pydantic
• PydanticOutputParser
• dotenv

### 🧠 One important thing I learned

Instead of simply asking an LLM:

> "Summarize this PDF"

I created a **defined schema** for the expected output.

For example:

```python
class pdf_summary(BaseModel):
    Book_Name: str
    Auther: str
    Published: Optional[int]
    Summary: List[str]
    Important_Notes: List[str]
```

This makes the generated information much easier to save, process, and use inside another application.

The final result is saved as a **JSON file**, which opens the door to building more advanced systems around it.

### 🔥 Next Step

Right now, my prototype sends the first **7 pages** of the PDF to the model.

My next step is to improve the pipeline so it can process **entire books page-by-page**, generate summaries for every page/chapter, and eventually build a system where users can:

📚 Upload a complete book
🔎 Search inside the book
🤖 Ask questions about specific chapters/pages
📝 Get chapter summaries
💡 Extract important notes
🎧 Potentially convert the book summary into audio

This project is helping me understand how **LangChain, document loaders, structured outputs, and LLMs** work together in real-world applications.

Still learning. Still building. 🚀

#Python #LangChain #GenerativeAI #LLM #AI #MachineLearning #DataScience #RAG #Pydantic #Groq #ArtificialIntelligence #BuildInPublic
