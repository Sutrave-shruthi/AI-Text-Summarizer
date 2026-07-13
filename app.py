# import streamlit as st
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# #Load API key
# load_dotenv()

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel("gemini-2.5-flash")

# st.title("Ai Text Summarizer")

# text = st.text_area("Enter your text here:", height=250)

# if st.button("Summarize"):
#     if text:

#         prompt = f"""
#         Summarize the following text in simple bullet points.

#         Text:
#         {text}
#         """

#         response = model.generate_content(prompt)

#         st.subheader("Summary")
#         st.write(response.text)

#     else:
#         st.warning("please enter some text.")


import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- Page Config ---------------- #
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Custom CSS ---------------- #
st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

.title{
    text-align:center;
    color:#0068C9;
    font-size:40px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
}

.stButton>button{
    width:100%;
    height:50px;
    font-size:18px;
    border-radius:10px;
}

.result{
    padding:20px;
    background:white;
    border-radius:10px;
    box-shadow:0px 0px 10px #ddd;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Header ---------------- #

st.markdown("<div class='title'>🤖 AI Text Summarizer</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Summarize long text using Google Gemini AI</div>", unsafe_allow_html=True)

st.write("")

left,right = st.columns([2,1])

with left:

    user_text = st.text_area(
        "Enter Text",
        height=300,
        placeholder="Paste your article here..."
    )

with right:

    st.metric("Words", len(user_text.split()))

    summarize = st.button("✨ Generate Summary")

    clear = st.button("🗑 Clear")

if clear:
    st.rerun()

if summarize:

    if user_text.strip()=="":

        st.warning("Please enter some text.")

    else:

        with st.spinner("Generating Summary..."):

            prompt=f"""
            Summarize the following text into simple bullet points.

            {user_text}
            """

            response=model.generate_content(prompt)

        st.write("")

        st.subheader("📄 Summary")

        st.success(response.text)

        st.download_button(
            "⬇ Download Summary",
            response.text,
            file_name="summary.txt"
        )