"""
from fastapi import FastAPI
from gradio.routes import mount_gradio_app
#from environment_setup import*
from agent import demo, agent_with_chat_history  # Importing from other files
import uuid

app = FastAPI()

@app.post("/query")
async def query_handler(message: str, session_id: str|None = None):
    if not session_id:
        session_id = uuid.uuid4().hex

    response = agent_with_chat_history.invoke(
        {"input": message},
        {"configurable": {"session_id": session_id}},
    )
    return {"response": response['output'], "session_id": session_id}

# Mount Gradio app for UI access
mount_gradio_app(app, demo, path="/ui")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)

    """

from fastapi import FastAPI
from pydantic import BaseModel
from agent import  agent_with_chat_history
import uuid

app = FastAPI()

# Define the request body model
class QueryRequest(BaseModel):
    message: str
    session_id: str|None = None  # Optional session_id

@app.post("/query")
async def query_handler(query: QueryRequest):
    try:
        message = query.message
        session_id = query.session_id or uuid.uuid4().hex

        response = agent_with_chat_history.invoke(
            {"input": message},
            {"configurable": {"session_id": session_id}},
        )

        return {"response": response['output'], "session_id": session_id}
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000,timeout_keep_alive=130)
