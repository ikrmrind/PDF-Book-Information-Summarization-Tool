from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser


load_dotenv()
model = ChatGroq(
    model='openai/gpt-oss-120b'
)

print('#'*80)
# Base Schema Of Dataset
class pdf_summary(BaseModel):
    Book_Name:str
    Auther : str
    Published : Optional[int]
    Summary : List[str]
    Important_Notes :List[str] 
#Output will be json Format

# For Output Results
Parser=PydanticOutputParser(pydantic_object=pdf_summary)



# Create Instrction for Chatbot
prompt=ChatPromptTemplate.from_messages([
    ('system',"""Extract the Information Related to That From PDF {pdf_Instruction}"""),
    ('user','{Paragraph}')
])

# Load the PDF
Doc=PyPDFLoader(r'C:\Users\IKRAM RIND\Desktop\RAG\Projects\data.pdf')
pdf=Doc.load()
print("Load Sucssesfully")


# Stores the 7 Pages Content
pdf_send= "\n\n".join(
    page.page_content for page in pdf[:7]
)

#Load Both Power in SIngle Chain
chain= prompt | model


# Send instrcution and data to Template and Invoke the Model
output=chain.invoke({
    'pdf_Instruction':Parser,
    'Paragraph':pdf_send
})

print(output.content)

with open('Summarry.json','w',encoding='utf-8') as file:
    file.writelines(output.content)