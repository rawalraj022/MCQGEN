import os             # importing os
import PyPDF2         # importing PyPDF2 is used to read the pdf file
import json           # importing json is used to convert the structure to dictionary
import traceback      # importing traceback is used to print the error

def read_file(file):    # this function is used to read the file
    if file.name.endswith(".pdf"):     # checking whether the file is pdf or not
        try:                          # if the file is pdf then it will read the file
            pdf_reader=PyPDF2.PdfFileReader(file)   # pdf_reader is used to read the pdf file
            text=""                                # text is used to store the text from the pdf file
            for page in pdf_reader.pages:         # for loop is used to extract the text from the pdf file
                text+=page.extract_text()        # text is used to store the text from the pdf file
            return text                         # returning the text
            
        except Exception as e:                  # if the file is not pdf then it will raise an exception
            raise Exception("error reading the PDF file")    # raising an exception
        
    elif file.name.endswith(".txt"):               # if the file is txt then it will read the file
        return file.read().decode("utf-8")        # returning the text
    
    else:                                          # if the file is not pdf or txt then it will raise an exception
        raise Exception(                           # raising an exception
            "unsupported file format only pdf and text file suppoted"   # error message
            )

def get_table_data(quiz_str):                   # this function is used to get the table data
    try:                                         # try block is used to handle the exception
        
        quiz_dict=json.loads(quiz_str)           # json.loads is used to convert the string to dictionary
        quiz_table_data=[]                        # create an empty list to store the table data
        
        # iterate over the quiz dictionary and extract the required information
        for key,value in quiz_dict.items():        # for loop is used to iterate over the dictionary
            mcq=value["mcq"]                       # mcq is used to store the mcq
            options=" || ".join(                   # options is used to store the options
                [
                    f"{option}-> {option_value}" for option, option_value in value["options"].items()   # for loop is used to iterate over the options
                 
                 ]
            )
             
            correct=value["correct"]             # correct is used to store the correct answer
            quiz_table_data.append({"MCQ": mcq,"Choices": options, "Correct": correct})   # append the data to the list 
        
        return quiz_table_data                  # return the table data
        
    except Exception as e:                       # if the file is not pdf or txt then it will raise an exception
        traceback.print_exception(type(e), e, e.__traceback__)     # print the error
        return False                               
  

