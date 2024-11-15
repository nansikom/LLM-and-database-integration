## LLM with Database Integration (Chinook)
This project integrates a large language model (LLM) with the Chinook database to provide insightful interactions with the data.
The application is built using several modern Python libraries to handle both the LLM and the communication with the database.

## Requirements(Technology needed)
The following Python libraries are required to run the application:

makefile
Copy code
aiohappyeyeballs==2.4.3
aiohttp==3.10.10
aiosignal==1.3.1
altair==5.4.1
annotated-types==0.7.0
anyio==4.6.2.post1
async-timeout==4.0.3
attrs==24.2.0
blinker==1.8.2
cachetools==5.5.0
certifi==2024.8.30
charset-normalizer==3.4.0
click==8.1.7
colorama==0.4.6
contourpy==1.3.0
cycler==0.12.1
dataclasses-json==0.6.7
distro==1.9.0
exceptiongroup==1.2.2
faiss-cpu==1.9.0
filelock==3.16.1
fonttools==4.54.1
frozenlist==1.5.0
fsspec==2024.10.0
gitdb==4.0.11
GitPython==3.1.43
google_search_results==2.4.2
greenlet==3.1.1
h11==0.14.0
httpcore==1.0.6
httpx==0.27.2
httpx-sse==0.4.0
huggingface-hub==0.26.2
idna==3.10
importlib_resources==6.4.5
Jinja2==3.1.4
jiter==0.7.0
joblib==1.4.2
jsonpatch==1.33
jsonpointer==3.0.0
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
kiwisolver==1.4.7
langchain==0.3.7
langchain-community==0.3.5
langchain-core==0.3.15
langchain-huggingface==0.1.2
langchain-openai==0.2.6
langchain-text-splitters==0.3.1
langsmith==0.1.139
markdown-it-py==3.0.0
MarkupSafe==3.0.2
marshmallow==3.23.1
matplotlib==3.9.2
mdurl==0.1.2
mpmath==1.3.0
multidict==6.1.0
mypy-extensions==1.0.0
narwhals==1.13.2
networkx==3.2.1
numpy==1.26.4
openai==1.54.3
orjson==3.10.10
packaging==24.1
pandas==2.2.3
pillow==11.0.0
propcache==0.2.0
protobuf==5.28.3
pyarrow==18.0.0
pydantic==2.9.2
pydantic-settings==2.6.1
pydantic_core==2.23.4
pydeck==0.9.1
Pygments==2.18.0
pyparsing==3.2.0
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytz==2024.2
PyYAML==6.0.2
referencing==0.35.1
regex==2024.9.11
requests==2.32.3
requests-toolbelt==1.0.0
rich==13.9.4
rpds-py==0.21.0
safetensors==0.4.5
scikit-learn==1.5.2
scipy==1.13.1
sentence-transformers==3.2.1
six==1.16.0
smmap==5.0.1
sniffio==1.3.1
SQLAlchemy==2.0.35
streamlit==1.40.0
streamlit-chat==0.1.1
sympy==1.13.1
tenacity==9.0.0
threadpoolctl==3.5.0
tiktoken==0.8.0
tokenizers==0.20.1
toml==0.10.2
torch==2.5.1
tornado==6.4.1
tqdm==4.66.6
transformers==4.46.1
typing-inspect==0.9.0
typing_extensions==4.12.2
tzdata==2024.2
urllib3==2.2.3
watchdog==5.0.3
yarl==1.17.1
zipp==3.20.2
## Technology used
Python
Java script
Html
SQL
SQLalchemy
Postgres DB
## Setting Up the Project
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/LLM-and-database-integration.git
Navigate into the project directory:

bash
Copy code
cd LLM-and-database-integration
Set up a virtual environment:

bash
Copy code
python -m venv venv
Set up a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

## On Windows:
bash
Copy code
venv\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Database Setup
The application connects to the Chinook database. The Chinook database is a sample database that models a digital media store.

## Download the Chinook Database:
Download the Chinook database from Chinook Database GitHub.
Set up the database:
Once you’ve downloaded the database file (usually a .sqlite file), place it in the project directory or update the connection settings to point to the correct location.
Usage
Run the application: Depending on how your application is set up, you can run it using:

bash
Copy code
python app.py

## Download the Postgres database
For postgres database, download the database
Save the Northwind.sql file
Run play_with_postgres.py
Connect to database
Run python app.py to test web interface with database
