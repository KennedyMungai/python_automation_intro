# %% [markdown]
# Importing the required packages

# %%
import spacy
import pdfminer
import re
import os
import pandas as pd

# %% [markdown]
# Imported the code inside the pdf2text file

# %%
import pdf2txt

# %% [markdown]
# Converting PDFs to text

# %%


def convert_pdf(f):
    output_filename = os.path.basename(os.path.splitext(f)[0]) + '.txt'
    output_filepath = os.path.join('output/txt/', output_filename)
    pdf2txt.main(args=[f, "--outfile", output_filepath])
    print(output_filepath + " saved successfully!!!")
    return open(output_filepath).read()

# %% [markdown]
# Loading the NLP language model


# %%
nlp = spacy.load('en_core_web_sm')

# %% [markdown]
# Defined a data structure which has the data fields needed

# %%
result_dict = {
    'name': [],
    'phone': [],
    'email': [],
    'skills': []
}

names = []
phones = []
emails = []
skills = []

# %% [markdown]
# Wrote a function that parses the content of a text file

# %%


def parse_content(text):
    skillset = re.compile("python|java|sql|hadoop|tableau")
    phone_num = re.compile(
        "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")
    doc = nlp(text)
    name = [entity.text for entity in doc.ents if entity.label_ == "PERSON"][0]
    print(name)
    email = [word for word in doc if word.like_email == True][0]
    print(email)
    phone = str(re.findall(phone_num, text.lower()))
    skills_list = re.findall(skillset, text.lower())
    unique_skills_list = str(set(skills_list))
    names.append(name)
    emails.append(email)
    phones.append(phone)
    skills.append(unique_skills_list)
    print("Extraction completed successfully")

# %% [markdown]
# Added a for loop so that the logic can work on multiple files instead of one file


# %%
for file in os.listdir('resumes/'):
    if file.endswith('.pdf'):
        print('Reading ' + file)
        txt = convert_pdf(os.path.join('resumes/', file))
        parse_content(txt)

# %%
names

# %%
phones

# %%
emails

# %%
skills

# %% [markdown]
# Assigning the individual lists to the result_dict dictionary

# %%
result_dict['name'] = names
result_dict['phone'] = phones
result_dict['email'] = emails
result_dict['skills'] = skills

# %% [markdown]
# Showing all the objects in the dictionary

# %%
result_dict

# %% [markdown]
# Rendering out the data in a table

# %%
result_df = pd.DataFrame(result_dict)
result_df

# %% [markdown]
# Extract the tabular data to a CSV output file

# %%
result_df.to_csv('output/csv/parsed_resumes.csv')
