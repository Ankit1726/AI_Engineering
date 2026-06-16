import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

# -------- Model --------
model = ChatMistralAI(model="mistral-small-2506")

# -------- Pydantic Schema --------
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: Optional[List[str]]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ('system', """Extract movie information from the paragraph
    {format_instructions}"""),
    ('human', '{paragraph}')
])

# -------- Page Config --------
st.set_page_config(page_title="Movie Info Extractor", page_icon="🎬", layout="centered")

# -------- CSS Styling --------
st.markdown("""
<style>

.main-title{
font-size:38px;
font-weight:bold;
text-align:center;
color:#00FFD1;
margin-bottom:20px;
}

.box{
background:#1E1E1E;
padding:20px;
border-radius:10px;
color:white;
}

.result{
background:#262730;
padding:15px;
border-radius:10px;
margin-top:15px;
}

</style>
""", unsafe_allow_html=True)

# -------- Title --------
st.markdown('<div class="main-title">🎬 Movie Information Extractor</div>', unsafe_allow_html=True)

st.markdown('<div class="box">Enter a movie paragraph below and the AI will extract structured movie data.</div>', unsafe_allow_html=True)

# -------- Input --------
paragraph = st.text_area("Enter Movie Paragraph", height=200)

# -------- Button --------
if st.button("Extract Movie Info"):

    final_prompt = prompt.invoke({
        "paragraph": paragraph,
        "format_instructions": parser.get_format_instructions()
    })

    response = model.invoke(final_prompt)
    movie_data = parser.parse(response.content)

    # -------- Output --------
    st.markdown('<div class="result">', unsafe_allow_html=True)

    st.subheader("Extracted Movie Data")

    st.write("**Title:**", movie_data.title)
    st.write("**Release Year:**", movie_data.release_year)
    st.write("**Genre:**", movie_data.genre)
    st.write("**Director:**", movie_data.director)
    st.write("**Cast:**", movie_data.cast)
    st.write("**Rating:**", movie_data.rating)
    st.write("**Summary:**", movie_data.summary)

    st.markdown('</div>', unsafe_allow_html=True)