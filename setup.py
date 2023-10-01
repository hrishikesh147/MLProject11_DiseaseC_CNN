from setuptools import setup,find_packages

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

NAME='CNN Disease Classifier'
VERSION='0.0.0.1'
DESC="This is a CNN based classification Project"
AUTHOR="hrishikesh bhagawati"
EMAIL="hrishikeshbhagawati@gmail.com"
AUTHOR_USER_NAME="hrishikesh147"
REPO_NAME="MLProject11_DiseaseC_CNN"

REQUIREMENTS="requirements.txt"

URL=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"

HYPHEN_E_DOT='-e .'

def get_requirements():
    with open(REQUIREMENTS) as req:
        req=req.readlines()
        req=[i.replace("\n","") for i in req]
        if HYPHEN_E_DOT in req:
            req.remove(HYPHEN_E_DOT)

        return req
        

setup(name=NAME,
      version=VERSION,
      description=DESC,
      long_description=long_description,
      long_description_content="text/markdown", 
      author=AUTHOR,
      author_email=EMAIL,
      url=URL,
      packages=find_packages(),
      install_requires=get_requirements()
      
     )