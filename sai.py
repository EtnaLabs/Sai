#!/usr/bin/env python3
import requests
import sys
import os
import pyperclip
import warnings

# Suppress all UserWarnings
warnings.filterwarnings('ignore', category=UserWarning)

SAI_RESPONSE = "default"
SAI_ERROR = "red"
SAI_RUN = "green"
SAI_QUESTION = "yellow"


def cprint(text, status="default", new_line=True):
    colors = {
        "default": "\033[0m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
    }
    end_char = '\n' if new_line else ''
    print(colors[status] + text + colors["default"], end=end_char)


def chat_with_gpt(prompt):
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-4",  # Specify the GPT-4 model
        "messages": [
            {
                "role": "system",
                "content": "You are SAI a command line tool for OSX. I'm going to ask you questions about my command line. "
                           "Whenever possible reply with just the command wrapped in backticks. "
                           "If you don't know the answer reply with 'SAI_ERROR:' and the description of the error"
            },
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    # Extract the assistant's response from the messages
    r = response_data['choices'][0]['message']['content'].strip()

    if r[0:10] == "SAI_ERROR:":
        return SAI_ERROR, r[10:]

    if r[0] == "`" and r[-1] == "`":
        return SAI_RUN, r[1:-1]

    return SAI_RESPONSE, r


def copy_command(command):
    pyperclip.copy(command)


def main():
    if len(sys.argv) < 2:
        cprint("Provide a prompt: ", SAI_QUESTION, new_line=False)
        prompt = input()
    else:
        prompt = sys.argv[1]

    status, response = chat_with_gpt(prompt)
    cprint(response, status, new_line=False)

    if status == SAI_RUN:
        copy_command(response)
        print("  copied to clipboard")


if __name__ == "__main__":
    main()
