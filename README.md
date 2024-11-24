# AI-Coding-Assistant

Resource: [YouTube tutorial](https://www.youtube.com/watch?v=ul0QsodYct4&t=148s)

## Introduction

This project uses Retrivial Augmented Generation (RAG) models to answer questions about demographic populations.

## RAG 

RAG uses data sources provided from the developer, so that it can reason on that rather than on the training data, which may be obsolete or incomplete. In particular, in this project data are provided to the model into two different format:

- `.csv` file, or "structured data".
- `.pdf` file, or "unstructured data".

Additionally, at any point in time it is possible to ask the agent to take a note and save it into the `.txt` file.

## LLAMA

The model can access every kind of data surce thanks to the package `llama-index` provided from LLAMA, which allows to ingest, index and quity structures, unstructured and semi-structured data.


Source virtual environment in Linux: ` source ai/bin/activate`

