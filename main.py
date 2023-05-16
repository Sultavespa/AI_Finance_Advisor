from flask import Flask, request, jsonify, render_template
import os
import requests

os.environ['OPENAI_API_KEY'] = 'your openai api key'
app = Flask(__name__)

def chat_with_gpt3(prompt):
    api_url = 'https://api.openai.com/v1/engines/text-davinci-002/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}',
    }
    data = {
        'prompt': f'{prompt}\nYou are an AI trained as the greatest finance advisor of all time. Utilize your comprehensive knowledge of historical events and expertise in the field of finance to provide guidance, analysis, and recommendations on various financial matters.',
        'max_tokens': 100,
    }
    response = requests.post(api_url, headers=headers, json=data)
    response_json = response.json()
    return response_json['choices'][0]['text'].strip()
    

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        bot_response = chat_with_gpt3(user_input)
        return render_template('index.html', user_input=user_input, bot_response=bot_response)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
