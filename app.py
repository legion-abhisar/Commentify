import ollama
import streamlit as st
import time

from prompt import instruction, context, constraints, example

def main():
    st.set_page_config(
        page_title="Commentify",
        page_icon=":computer:"
    )

    st.header("Commentify python script. :snake:")

    response_container = st.empty()

    with st.sidebar:
        st.subheader("Your python script")
        uploaded_py_file = st.file_uploader(
            "Upload your Python script here and click on Process",
            accept_multiple_files=False
        )
        
        if st.button("Process"):
            with st.spinner("Processing"):
                # get python script
                py_content = uploaded_py_file.read()

                # Parse and run against llm
                response = ollama.chat(
                    model='codellama:7b',
                    messages=[{'role': 'user', 
                        'content': f'{instruction} {py_content} {context + constraints + example}'}],
                    stream=True
                )

                full_response = ""
                for message in response:
                    full_response += message["message"]["content"]
                    response_container.write(full_response)
                    time.sleep(0.1)

    
if __name__ == "__main__":
    main()
