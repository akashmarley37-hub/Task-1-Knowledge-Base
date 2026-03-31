# Task 1: Dynamic Knowledge Base Expansion

## Project Overview
This module implements a **Vector Database** using ChromaDB and Sentence-Transformers. It allows the chatbot to ingest new medical information in real-time without requiring a model retraining phase.

## Technical Implementation
- **Vector Engine:** ChromaDB (Persistent)
- **Embedding Model:** `all-MiniLM-L6-v2` (Sentence-Transformers)
- **Search Logic:** Semantic similarity search rather than keyword matching.

## How It Works
The system converts text data into high-dimensional vectors. When a user asks a question, the system converts the query into a vector and finds the "nearest neighbor" in the database to provide a contextually accurate answer.

## Result Screenshot
![Task 1 Result](PASTE_LINK_TO_YOUR_SCREENSHOT_HERE)
