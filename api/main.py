from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from function_retriever import FunctionRetriever

app = FastAPI()
retriever = FunctionRetriever()

class ExecuteRequest(BaseModel):
    prompt: str

def generate_code(function_name: str) -> str:
    """Generate executable Python code for a given function name."""
    code = f"""from automation_registry import AutomationRegistry

def main():
    try:
        AutomationRegistry.{function_name}()
        print("{function_name.replace('_', ' ').title()} executed successfully.")
    except Exception as e:
        print(f"Error executing function: {{e}}")

if __name__ == "__main__":
    main()"""
    return code

@app.post("/execute")
async def execute(request: ExecuteRequest):
    try:
        results = retriever.retrieve_function(request.prompt, top_k=1)
        if not results:
            raise HTTPException(status_code=404, detail="No matching function found")
        
        best_match = results[0]
        return {
            "function": best_match["name"],
            "code": generate_code(best_match["name"])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))