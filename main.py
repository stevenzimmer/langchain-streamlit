import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

st.set_page_config(page_title="Globalize Email App", page_icon=":shark:")

openai_api_key = st.secrets.env.open_ai_api_key

template = """
  Below is an email that may be poorly worded.
  Your goal is to:
   - Properly format the email
   - Convert the input text to a specified tone
   - Convert the input text to a specified dialect

  Here are some examples of different tones:
  - Formal: We went to Barcelona for the weekend. We have a lot of things to tell you.
  - Informal: Went to Barelona for the weekend. Lots to tell.

  Here are some examples of words in different dialects:
  - American English: French fries, cotton candy, apartment, garbage, cookie.
  - British English: chips, candy floss, flat, rubbish, biscuit.

  Below is the email, tone, and dialect:
  TONE: {tone}
  DIALECT: {dialect}
  EMAIL: {email}

  YOUR RESPONSE:
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["tone", "dialect", "email"],
)


def load_llm():
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    return llm  

llm  = load_llm()





def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

st.header("Globalize Email App")



st.subheader("Enter your email to convert it to a global email")

col1, col2 = st.columns(2)

with col1:
    option_tone = st.selectbox(
        'Which tone would you like your emails to have?',
        ('Formal', 'Informal')
    )

with col2:
      
      option_language = st.selectbox(
          'Which English Dialect would you like?',
          ('American English', 'British English')
      )


def get_text():
    input_text = st.text_area(label="Providing a label for accessibility reasons",placeholder="Your email", key="email_input")

    return input_text

email_input = get_text()

st.subheader("Your converted email")

if email_input:
     prompt_with_email = prompt.format(tone=option_tone, dialect=option_language, email=email_input)
    #  formatted_email = llm(prompt_with_email)

    #  st.write(formatted_email)