import streamlit as st
from kb_agent import search_knowledge_base
from web_agent import web_search
from guardrails import is_valid_math_question  # Ensure this exists
# The following are not needed unless you use them directly in app.py
# from embedding_service import get_embedding
# from vector_store import search_collection

st.set_page_config(page_title="📚 Math Professor Agent", page_icon="📚")
st.title("📚 Ask the Math Professor")

# --- User Input ---
user_query = st.text_input("🔍 Enter your Math Question:")

if user_query:
    with st.spinner("🔎 Checking your question..."):

        if not is_valid_math_question(user_query):
            st.error("❌ Please enter a valid Math-related question only.")
        else:
            kb_answer = search_knowledge_base(user_query)

            if kb_answer and ("✅" in kb_answer):
                st.success("✅ Found Answer from Knowledge Base:")
                st.markdown(kb_answer)
            else:
                st.warning("⚡ Not found in KB. Searching the Web...")
                web_answer = web_search(user_query)

                if web_answer:
                    st.info("🔎 Answer from Web Search:")
                    st.write(web_answer)
                else:
                    st.error("❌ Sorry, no good answer found from the web either.")

        # --- Feedback Section ---
        st.markdown("---")
        feedback = st.radio("Was this answer helpful?", ("👍 Yes", "👎 No"), horizontal=True)
        if feedback:
            st.success("🎉 Thank you for your feedback!")
