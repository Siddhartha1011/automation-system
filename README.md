# automation-system

# Installation

# Clone the Repository
```bash
git clone https://github.com/Siddhartha1011/automation-system.git
cd automation-system

# Install Dependencies
    fastapi
    uvicorn
    chromadb
    psutil

# Working
  1)Create a registry of common automation functions on automation_registry.py

  The AutomationRegistry class provides system automation functions,including:
	•	Application Control → Opens Chrome, Calculator, Notepad.
	•	System Monitoring → Retrieves CPU, RAM, and disk usage.
	•	Command Execution → Runs shell commands and executes Python scripts.

  2)Store function metadata in ChromaDB and retrieve relevant functions dynamically on function_retriever.py.

  The FunctionRetriever class:
	•	Extracts function metadata using inspect.
	•	Stores function descriptions in ChromaDB.
	•	Retrieves the most relevant function based on a user query.

  3)Generate structured Python code for function execution on function_retriever.py

  After retrieving the best function, the code generator creates an executable script.

  4)Enhance function retrieval with chat history on function_retriever.py

	•	ChromaDB stores indexed functions, so they persist across sessions.
	•	The retriever searches previously stored functions, allowing context-aware queries.

  5)Expose API endpoints using FastAPI on main.py

  A FastAPI /execute endpoint allows users to call functions via API.

# Run the API call
  uvicorn main:app --reload
  curl -X POST "http://127.0.0.1:8000/execute" -H "Content-Type: application/json" -d '{"prompt": "Launch Google Chrome"}'
 
