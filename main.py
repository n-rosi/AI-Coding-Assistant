# Copyright 2023 Mistral AI

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dotenv import load_dotenv
import os 
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context 
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent.legacy.react.base import ReActAgent
from llama_index.llms.mistralai import MistralAI 
from pdf import jazz_engine

# load environment variables (opneai key)
load_dotenv()

# provide the data to the csv file
csv_path = os.path.join("data","tcc_ceds_music.csv")
pandas_df = pd.read_csv(csv_path)

# wrap quiry engie around structured data for RAG system
df_query_engine = PandasQueryEngine(df = pandas_df,                     # structured data
                                            verbose = False, 
                                            instruction_str=instruction_str,
                                            new_prompt = new_prompt)
df_query_engine.update_prompts({"pandas_prompt":new_prompt})

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=df_query_engine,
        metadata=ToolMetadata(
            name="music_data",
            description="this gives a list of lyrics from 1950 to 2019 \
                        describing music metadata as sadness, danceability,\
                        loudness, acousticness, etc. Authors also provide \
                        some information as lyrics which can be used to \
                        natural language processing. ",
        ),
    ),
    QueryEngineTool(
        query_engine=jazz_engine,
        metadata=ToolMetadata(
            name="jazz_data",
            description="this gives detailed information about Jazz music style.",
        ),
    ),
]

api_key = os.getenv("MISTRALAI_API_KEY")
llm = MistralAI(model="open-mixtral-8x22b", api_key=api_key) 
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

import time
while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
    time.sleep(5)

