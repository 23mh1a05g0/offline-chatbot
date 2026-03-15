import requests
import json
import os

# Ollama configuration
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"


# Function to query Ollama
def query_ollama(prompt):

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)

        response.raise_for_status()

        data = response.json()

        return data.get("response", "").strip()

    except requests.exceptions.RequestException as e:
        print("Error contacting Ollama:", e)
        return "Error: Could not get response"


# Load prompt template
def load_template(path):

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


# Default 20 evaluation queries
def get_default_queries():

    return [
        "How do I track my order?",
        "My discount code is not working at checkout.",
        "How can I change my delivery address?",
        "I received the wrong item in my order.",
        "My order has not arrived yet. What should I do?",
        "How do I cancel my order?",
        "Can I return a product after delivery?",
        "How long does shipping usually take?",
        "I forgot my account password.",
        "How do I update my payment method?",
        "My payment was deducted but my order was not confirmed.",
        "How do I apply a coupon code?",
        "Can I exchange a product for another size?",
        "Where can I download my invoice?",
        "How do I contact customer support?",
        "Why is my order still processing?",
        "Can I change the product color after ordering?",
        "Do you offer international shipping?",
        "How can I check my previous orders?",
        "Is there a warranty for electronics?"
    ]


def main():

    print("\nOffline Customer Support Chatbot")

    zero_template = load_template("prompts/zero_shot_template.txt")
    one_template = load_template("prompts/one_shot_template.txt")

    # Ensure results file exists
    if not os.path.exists("eval/results.md"):
        with open("eval/results.md", "w", encoding="utf-8") as file:
            file.write("# Chatbot Evaluation Results\n\n")
            file.write("| Query # | Customer Query | Prompting Method | Response |\n")
            file.write("|--------|---------------|------------------|----------|\n")

    query_count = 1

    # -----------------------------
    # Run default 20 evaluation queries
    # -----------------------------

    print("\nRunning default evaluation queries...\n")

    default_queries = get_default_queries()

    for query in default_queries:

        print(f"Processing Query {query_count}: {query}")

        zero_prompt = zero_template.replace("{query}", query)
        zero_response = query_ollama(zero_prompt)

        one_prompt = one_template.replace("{query}", query)
        one_response = query_ollama(one_prompt)

        with open("eval/results.md", "a", encoding="utf-8") as file:

            file.write(f"| {query_count} | {query} | Zero-Shot | {zero_response} |\n")
            file.write(f"| {query_count} | {query} | One-Shot | {one_response} |\n")

        query_count += 1

    print("\nDefault evaluation completed!\n")

    # -----------------------------
    # Start interactive chatbot
    # -----------------------------

    print("Interactive Chatbot Started")
    print("Type 'exit' to stop\n")

    while True:

        user_query = input("Customer Question: ")

        if user_query.lower() == "exit":
            print("\nChatbot stopped.")
            break

        print("\nProcessing...\n")

        zero_prompt = zero_template.replace("{query}", user_query)
        zero_response = query_ollama(zero_prompt)

        one_prompt = one_template.replace("{query}", user_query)
        one_response = query_ollama(one_prompt)

        print("Zero-Shot Response:")
        print(zero_response)

        print("\nOne-Shot Response:")
        print(one_response)

        with open("eval/results.md", "a", encoding="utf-8") as file:

            file.write(f"| {query_count} | {user_query} | Zero-Shot | {zero_response} |\n")
            file.write(f"| {query_count} | {user_query} | One-Shot | {one_response} |\n")

        query_count += 1


if __name__ == "__main__":
    main()