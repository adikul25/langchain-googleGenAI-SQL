from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import GoogleGenerativeAI

class DatabaseQueryExecutor:
    def __init__(self, api_key, db_uri):
        self.api_key = api_key
        self.db_uri = db_uri
        self.llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=self.api_key, temperature=0.2)
        self.db = SQLDatabase.from_uri(self.db_uri)
        self.db_chain = SQLDatabaseChain.from_llm(
            self.llm, 
            self.db, 
            verbose=True, 
            use_query_checker=True, 
            return_intermediate_steps=True
        )
    
    def execute_query(self, query):
        result = self.db_chain(query)
        return result["intermediate_steps"][2]["sql_cmd"]