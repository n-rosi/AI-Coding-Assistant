from dotenv import load_dotenv
import os 
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str

# load environment variables (opneai key)
load_dotenv()

# load pandas dataframe 
population_path = os.path.join("data","WorldPopulation2023.csv")
population_df = pd.read_csv(population_path)

# wrap quiry engie around structured data for RAG system
population_query_engine = PandasQueryEngine(df = population_df,         # structured data
                                            verbose = True, 
                                            new_prompt = new_prompt)
population_query_engine.update_prompts({"pandas_prompt":new_prompt})
population_query_engine.query("what is the population of canada?")

