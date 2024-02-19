import streamlit as st
from flask import Flask, render_template, request
# from dotenv import load_dotenv
from flask import Flask, send_from_directory

import os
import random
import string

# Load environment variables from .env file
# load_dotenv()
port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
app._static_folder = 'templates/static'
# @app.route('')

@app.route("/", methods=["GET", "POST"])
def index():
    prompt = ""
    split_length = ""
    file_data = ""
    num_parts1=''
    # print(file_data)

    if request.method == "POST":
        prompt = request.form["prompt"]
        print(prompt)
        split_length = int(request.form["split_length"])
        num_parts1 = -(-len(prompt) // split_length) 
        file_data = split_prompt(prompt, split_length)


    # hash_value = generate_random_hash(8)

    return render_template("chatgpt.html", num_parts=num_parts1,prompt=prompt, split_length=split_length, file_data=file_data)

def split_prompt(text, split_length):
    if split_length <= 0:
        raise ValueError("Max length must be greater than 0.")
    print('textvalue',len(text))
    num_parts = -(-len(text) // split_length)  #divide into partss login
    print(num_parts)
    file_data = []
    # print("first -",file_data)

    for i in range(num_parts):
        print('values',i)
        start = i * split_length
        print(start)
        end = min((i + 1) * split_length, len(text))
        print('mini',end)

        if i == num_parts - 1:
            print(num_parts-1)
            content = f'[START PART {i + 1}/{num_parts}]\n' + text[start:end] + f'\n[END PART {i + 1}/{num_parts}]'
            content += '\nALL PARTS SENT. Now you can continue processing the request.'
        else:
            content = f'Do not answer yet. This is just another part of the text I want to send you. Just receive and acknowledge as "Part {i + 1}/{num_parts} received" and wait for the next part.\n[START PART {i + 1}/{num_parts}]\n' + text[start:end] + f'\n[END PART {i + 1}/{num_parts}]'
            content += f'\nRemember not answering yet. Just acknowledge you received this part with the message "Part {i + 1}/{num_parts} received" and wait for the next part.'

        file_data.append({
            'name': f'split_{str(i + 1).zfill(3)}_of_{str(num_parts).zfill(3)}',
            'content': content
        })

    return file_data
   

# def generate_random_hash(length):
#     return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)),debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
