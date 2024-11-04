import os
import json
import traceback
import pandas as pd
#importing necessary packages


from dotenv import load_dotenv
# load_dotenv = to load .env file
from src.mcqgenerator.utils import read_file,get_table_data
# from utils = to import read_file,get_table_data
from src.mcqgenerator.logger import logging
# from logger = to import logging

#importing necessary packages from langchain
from langchain.chat_models import ChatOpenAI
#from chat_models = to import ChatOpenAI
from langchain.prompts import PromptTemplate
#from prompts = to import PromptTemplate
from langchain.chains import LLMChain
#from chains = to import LLMChain
from langchain.chains import SequentialChain
#from SequentialChain = to import SequentialChain


# Load environment variables from the .env file
load_dotenv()


# Access the environment variables just like you would with os.environ
key=os.getenv("OPENAI_API_KEY")
# environment variable = OPENAI_API_KEY

llm = ChatOpenAI(openai_api_key=key,model_name="gpt-3.5-turbo", temperature=0.7)
# 'llm' is the object of the ChatOpenAI 
# 'ChatOpenAI' is the class provided by the LangChain library.
# temperature is for creativity , if temperature near 2 than it is more creative ,if temperature near 0 than it is less creative and will give the straightforward answer
#llm is object and ChatOpenAI is class


template="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz  of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}

"""
# This is the template of prompt [designing the prompt using prompt template]


quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=template)


quiz_chain=LLMChain(llm=llm,prompts=quiz_generation_prompt,output_key="quiz",verbose=True)
# we use llm chain to connecting the several component
# We have two component first is 'llm' and second one is 'prompt'
# Connecting both component two component we use 'llm chain'

# now i am going to create 'quiz_chain' [1st chain]
# 'llm' is the object of the ChatOpenAI 
# 'ChatOpenAI' is the class provided by the LangChain library.
# 'quiz_generation_prompt' is the object of the PromptTemplate
# 'PromptTemplate' is the class provided by the LangChain library.
# 'quiz_chain' is the object of the LLMChain
# 'LLMChain' is the class provided by the LangChain library.

template2="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""
# This is the template of prompt [designing the prompt using prompt template]
# here we use 'template2' [designing the prompt using prompt template]

# You are an expert English Grammarian and Writer.

quiz_evaluation_prompt=PromptTemplate(input_variables=["subject", "quiz"], template=template2)
# Creating a template
# Now for Template2 and quiz_evaluation_prompt , I am going to create second llmchain .
# 'quiz_evaluation_prompt' is the object of the PromptTemplate
# 'PromptTemplate' is the class provided by the LangChain library.

review_chain=LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)
# Now i am going to create 'review_chain' [2nd chain]
# 'llm' is the object of the ChatOpenAI
# 'ChatOpenAI' is the class provided by the LangChain library.
# 'quiz_evaluation_prompt' is the object of the PromptTemplate
# 'PromptTemplate' is the class provided by the LangChain library.
# 'review_chain' is the object of the LLMChain
# 'LLMChain' is the class provided by the LangChain library.


# [sequential chain] Combining both 1st and 2nd chain and creating 3rd chain . Now i am going to connect two chains 'quiz_chain' and 'review_chain', To create sequential chain

# This is an Overall Chain where we run the two chains in Sequence
generate_evaluate_chain=SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],
                                        output_variables=["quiz", "review"], verbose=True,)

# SequentialChain is the class and generate_evaluate_chain is the object.
# 'SequentialChain' is the class provided by the LangChain library.
# what is input_variables ? input_variables is the input variables of the chain.
# what is output_variables ? output_variables is the output variables of the chain.
# what is verbose ? Verbose is used to show the progress of the chain.



