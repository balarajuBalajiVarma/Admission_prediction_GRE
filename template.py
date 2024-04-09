import os
from pathlib import Path
import logging # it will show logs while trmplate python scriprs works

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')


list_of_files=[

    "src/__init__.py", 
    "src/helper.py", # definition scripts
    # "src/prompt.py", # prompt py script
    # ".env",      # credentials
    # "setup.py",  # If we want to use the libraries in local that is from src folder to import a filename.
                    # src is not installed in libraries to work those folders which contains file we use
                    #setup.py and add some code their 
    "research/trails.ipynb", # trails notebook
    "app.py", # flask 
    # "store_index.py", #store vector db data
    "static/.gitkeep",
    "templates/chat.html" 
]

for filepath in list_of_files:

    #to make path as windows 
    filepath=Path(filepath)

    #Split filedir and filepath using split function
    filedir, filename=os.path.split(filepath)
    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the filename {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating an empty file: {filepath}")
    else:
        logging.info(f'File name already exists')


