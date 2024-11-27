# AI-Coding-Assistant

The code provided in this repository was written following the tutorial here provided: [YouTube tutorial](https://www.youtube.com/watch?v=ul0QsodYct4&t=148s)

Differently from the tutrial, it makes use of Mistal AI free model `open-mixtral-8x22b`, available under Apache2.0 license (see LICENSE).

The utilized dataset can be downloaded at: [Music Dataset: 1950 to 2019](https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019) 

## Introduction

This project uses Retrivial Augmented Generation (RAG) models to answer questions about demographic populations.

## RAG 

RAG uses data sources provided from the developer, so that it can reason on that rather than on the training data, which may be obsolete or incomplete. In particular, in this project data are provided to the model into two different format:

- `.csv` file, or "structured data".
- `.pdf` file, or "unstructured data".

Additionally, at any point in time it is possible to ask the agent to take a note and save it into the `.txt` file.

## LLAMA

The model can access every kind of data surce thanks to the package `llama-index` provided from LLAMA, which allows to ingest, index and query structured, unstructured and semi-structured data.

`llama-index` also provide with wrappers to allow the LLM model to execute user-custom python functions.

## simple use example

Run the code from your python or conda environment with:

`python main.py`

You will able to interact with the agent via the following prompt:

`Enter a prompt (q to quit):`

You can ask a general question or give instruction about writing a particular note in the file `data/note.txt`. 


