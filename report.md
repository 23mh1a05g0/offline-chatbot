# Project Report

## Introduction

This project explores the feasibility of deploying a **local AI chatbot for customer support** using Ollama and the Llama 3.2 language model. The goal is to automate responses to common e-commerce queries while maintaining **data privacy** and eliminating reliance on external APIs.

The experiment focuses on comparing two prompt engineering techniques:

* Zero-Shot Prompting
* One-Shot Prompting

---

## Methodology

### Query Preparation

Twenty customer support queries were created based on scenarios commonly encountered in e-commerce systems. These queries were adapted from patterns observed in the Ubuntu Dialogue Corpus dataset.

Examples include:

* Order tracking
* Payment issues
* Returns and exchanges
* Shipping information
* Account management

---

### Prompt Templates

Two prompt templates were designed.

**Zero-Shot Prompt**

The model receives only instructions and the user query.

**One-Shot Prompt**

The model receives an example question and response before the user query to guide the output style.

---

### System Architecture

```
Customer Query
      ↓
chatbot.py
      ↓
Prompt Template
      ↓
Ollama API
      ↓
Llama 3.2 Model
      ↓
Generated Response
      ↓
Logged to results.md
```

---

## Evaluation Criteria

Each response was manually scored based on three criteria:

### Relevance (1-5)

How accurately the response addresses the user's query.

### Coherence (1-5)

Clarity and grammatical correctness of the response.

### Helpfulness (1-5)

Usefulness and practicality of the response.

---

## Results

Average scores were calculated from the evaluation results.

| Prompt Method | Relevance | Coherence | Helpfulness |
| ------------- | --------- | --------- | ----------- |
| Zero-Shot     | 4.7       | 5.0       | 4.6         |
| One-Shot      | 4.5       | 5.0       | 4.4         |

Both prompting techniques produced **clear and understandable responses**.

Zero-Shot prompting performed slightly better in helpfulness for certain queries.

---

## Observations

* The model handled common e-commerce queries effectively.
* Responses were generally polite and well-structured.
* Some responses asked for additional information instead of providing direct solutions.
* One-Shot prompting helped maintain consistent response style.

---

## Limitations

Several limitations were observed:

* The model does not have access to real order data.
* Responses may occasionally contain **hallucinated information**.
* Performance depends on local hardware capabilities.

---

## Conclusion

The experiment demonstrates that **local LLM deployment is a viable solution for customer support automation**.

Using Ollama with Llama 3.2 enables organizations to build AI tools while maintaining full control over their data.

Future improvements may include integrating real order databases, adding document retrieval systems, and deploying the chatbot through a web interface.

---


