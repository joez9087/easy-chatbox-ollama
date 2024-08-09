from flask import Flask, render_template, request, jsonify
import os
import ollama

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    image = request.files.get('image')
    user_message = request.form.get('message')

    if image:
        image_path = os.path.join('static/uploads', image.filename)
        image.save(image_path)

        try:
            res = ollama.chat(
                model="llava",
                messages=[
                    {
                        'role': 'user',
                        'content': user_message,
                        'images': [image_path]
                    }
                ]
            )
            response_text = res['message']['content']
        except Exception as e:
            response_text = f"An error occurred with LLaVA: {str(e)}"
    
    else:
        try:
            res = ollama.chat(
                model="llama3.1",
                messages=[
                    {
                        'role': 'user',
                        'content': user_message
                    }
                ]
            )
            response_text = res['message']['content']
        except Exception as e:
            response_text = f"An error occurred with LLaMA 3.1: {str(e)}"

    return jsonify({'response': response_text})

if __name__ == '__main__':
    if not os.path.exists('static/uploads'):
        os.makedirs('static/uploads')
    app.run(debug=True)
