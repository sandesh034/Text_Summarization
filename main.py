import torch
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the fine-tuned model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained('./models/pegasus_finetuned').to(device)
tokenizer = AutoTokenizer.from_pretrained('./models/tokenizer_finetuned')

app = Flask(__name__)

@app.route('/',methods=['GET'])
def start():
    return jsonify({"message":"Welcome to text summarizer"})

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        # Get JSON data from the request
        data = request.get_json()
        text = data.get("text", "")
        max_length = data.get("max_length", 200)
        min_length = data.get("min_length", 30)
        num_beams = data.get("num_beams", 4)

        # Validate input text
        if not text:
            return jsonify({"error": "Please provide the text for summarization"}), 400

        # Tokenize input text
        inputs = tokenizer(
            text,
            max_length=512,
            truncation=True,
            return_tensors='pt'
        ).to(device)

        # Generate the summary
        output = model.generate(
            inputs["input_ids"],
            max_length=max_length,
            min_length=min_length,
            num_beams=num_beams,
            length_penalty=2.0,
            early_stopping=True
        )

        # Decode the generated summary
        summary = tokenizer.decode(output[0], skip_special_tokens=True)
        return jsonify({"summary": summary})

    except Exception as e:
        # Handle exceptions gracefully
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
