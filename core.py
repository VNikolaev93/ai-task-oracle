import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from config import GROQ_API_KEY, MODEL_NAME

class TaskManager:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=GROQ_API_KEY, 
            model_name=MODEL_NAME, 
            temperature=0
        )

    def process_text(self, text):
        print(f"--- [AI] Step 1 ---")

        # Draft Agent
        draft_prompt = ChatPromptTemplate.from_template("""
        SYSTEM: You are a Project Management AI.
        TASK: Extract ALL tasks, including informal ones, from the meeting notes.
        FORMAT: Return ONLY a JSON list of objects (task, assignee, deadline).
        TEXT: {context}
        """)
        
        print("--- [AI] Step 2: Draft extraction complete. Starting reflection... ---") 

        # Critic Agent
        review_prompt = ChatPromptTemplate.from_template("""
        SYSTEM: You are a Senior Quality Controller.
        TASK: Review the task list extracted by another AI.
        CONTEXT: {context}
        DRAFT: {draft}
        INSTRUCTIONS:
        1. Fix assignees based on logic.
        2. Ensure no tasks are missing.
        3. Output ONLY the final JSON list.
        """)

        print("--- [AI] Step 3: Final validation complete. ---")
        
        draft_result = (draft_prompt | self.llm).invoke({"context": text}).content
       
        final_result = (review_prompt | self.llm).invoke({
            "context": text,
            "draft": draft_result
        }).content
        
        print("--- [AI] Final validation complete. ---")
        
        start = final_result.find("[")
        end = final_result.rfind("]") + 1
        return json.loads(final_result[start:end])