import streamlit as st
import pandas as pd
import io
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from core import TaskManager
from config import MODEL_NAME

st.set_page_config(page_title="AI Task Oracle", page_icon="🤖")

st.title("🤖 AI Task Oracle")
st.markdown("Transform messy meeting notes into structured task lists instantly.")

if 'manager' not in st.session_state:
    st.session_state.manager = TaskManager()

with st.sidebar:
    st.header("Settings")
    st.info(f"Model: {MODEL_NAME}")
    st.write("---")
    st.write("This tool identifies tasks, assignees, and deadlines from unstructured text.")

uploaded_file = st.file_uploader("Upload meeting notes (.txt)", type="txt")

if uploaded_file is not None:
    stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
    content = stringio.read()
    
    st.subheader("Document Preview:")
    st.text_area("", content, height=150, disabled=True)

    if st.button("🚀 Analyze & Extract Tasks"):
        with st.spinner("AI Magic in progress..."):
            try:
                tasks = st.session_state.manager.process_text(content)
                
                if tasks:
                    st.success(f"Success! Found {len(tasks)} tasks.")
                    df = pd.DataFrame(tasks)
                    # Ensuring standard column names
                    df.columns = ["Task", "Assignee", "Deadline"]
                    
                    st.dataframe(df, use_container_width=True)
                    
                    csv = df.to_csv(index=False).encode('utf-8-sig')
                    st.download_button(
                        label="📥 Download CSV Report",
                        data=csv,
                        file_name="tasks_report.csv",
                        mime="text/csv",
                    )
                else:
                    st.warning("No tasks identified. Please check the input text.")
            except Exception as e:
                st.error(f"Error during processing: {e}")

st.write("---")
st.caption("Developed by Viacheslav | AI Engineer Portfolio 2026")