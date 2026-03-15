# Offline Customer Support Chatbot using Ollama and Llama 3.2

## Project Overview

This project implements an **offline AI-powered customer support chatbot** for a fictional e-commerce store named **Chic Boutique**. The chatbot runs entirely on a local machine using **Ollama** to serve the **Llama 3.2 (3B)** language model.

The system demonstrates how organizations can build AI assistants **without sending sensitive customer data to external APIs**. It also compares two prompt engineering techniques: **Zero-Shot Prompting** and **One-Shot Prompting**.

---

## Objective

The main objectives of this project are:

* Deploy a local Large Language Model (LLM) using Ollama.
* Build a Python backend that communicates with the model via API.
* Compare **Zero-Shot vs One-Shot prompting techniques**.
* Evaluate chatbot performance using manual scoring.
* Demonstrate how AI can be used for **customer support automation** while maintaining **data privacy**.

---

## Key Features

* Runs completely **offline**
* Uses **Llama 3.2 local language model**
* Supports **Zero-Shot and One-Shot prompting**
* Automatically evaluates **20 predefined queries**
* Allows **interactive user questions via terminal**
* Logs all responses to `eval/results.md`
* Demonstrates **prompt engineering and evaluation methodology**

---

## Project Structure

```
offline-chatbot/
│
├── chatbot.py
├── README.md
├── setup.md
├── report.md
│
├── prompts/
│   ├── zero_shot_template.txt
│   └── one_shot_template.txt
│
└── eval/
    └── results.md
```

---

## How the Chatbot Works

The chatbot follows this workflow:

1. Python script loads prompt templates.
2. A customer query is inserted into the template.
3. The prompt is sent to the Ollama API.
4. Ollama forwards the prompt to the Llama model.
5. The model generates a response.
6. The response is logged and displayed to the user.

---

## Example Interaction

```
Customer Question: How do I track my order?

Zero-Shot Response:
You can track your order by logging into your account and visiting the Orders section.

One-Shot Response:
Log into your account and open Order History to track your shipment.
```

---

## Technologies Used

* Python
* Ollama
* Llama 3.2 (3B)
* HuggingFace datasets
* Requests library
* Markdown for evaluation logs

---

## Future Improvements

Possible improvements include:

* Integrating a web interface (Flask / FastAPI)
* Adding product policy documents using RAG
* Supporting multi-turn conversation memory
* Implementing automated response scoring

---

