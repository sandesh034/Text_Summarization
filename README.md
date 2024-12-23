# Text Summarizer Using google/bigbird-pegasus-large-bigpatent Model

This repository contains a text summarization application built using a fine-tuning Pegasus model on the CNN/DailyMail dataset. The model is capable of generating concise and meaningful summaries from long articles or text passages.

## Features

- **Model**:
  - Fine-tuned Pegasus model (`google/bigbird-pegasus-large-bigpatent`)[Link](https://huggingface.co/google/bigbird-pegasus-large-bigpatent) on the CNN/DailyMail [Link](https://huggingface.co/datasets/abisee/cnn_dailymail)
  - Training configuration:
    - Dataset size: ~15,000 rows.
    - Epochs: 2.
    - Optimized for summarization tasks.

- **API**:
  - Flask-based backend to process summarization requests.
  - Device-aware deployment (uses GPU if available).

- **Frontend**:
  - Interactive user interface built using Streamlit.
  - User-configurable parameters:
    - Maximum and minimum length of the summary.
    - Beam search settings for controlling output quality.

## Dataset

The model was fine-tuned on the **CNN/DailyMail dataset**, which is widely used for abstractive summarization tasks. The dataset consists of news articles paired with human-written summaries, making it ideal for training summarization models.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sandesh034/Text_Summarization.git
   cd Text_Summarizer
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```

3. Install required libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Download the fine-tuned model and tokenizer:

   -  Run the notebook at first and create a folder named `models` inside that folder move  fine-tuned model `pegasus_finetuned` and tokenizer and `tokenizer_finetuned`.

## Usage

### Running the Flask Backend

1. Start the Flask API:

   ```bash
   python main.py
   ```

2. The API will be available at `http://127.0.0.1:5000/summarize`.

### Running the Streamlit Frontend

1. Start the Streamlit app:

   ```bash
   streamlit run ./frontend/streamlit.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

### Using the App

1. Input the text you want to summarize in the **Original Article** section.
2. Adjust parameters such as:
   - Maximum Length
   - Minimum Length
   - Number of Beams
3. Click the **Summarize** button to generate the summary.
4. View the output in the **Summary** section.

 
## API Request Format

### Request URL

`POST http://127.0.0.1:5000/summarize`

### Request Headers

- `Content-Type`: `application/json`

### Request Body (JSON)

```json
{
  "text": "The article text that you want to summarize.",
  "max_length": 400,
  "min_length": 50,
  "num_beams": 4
}
```

- **text** (string): The article or text you want to summarize.
- **max_length** (integer): The maximum length of the summary. Default is `400`.
- **min_length** (integer): The minimum length of the summary. Default is `50`.
- **num_beams** (integer): The number of beams for beam search. Default is `4`.

### Example Request

```json
{
  "text": "The Thirsty Crow On a hot summer day, a thirsty crow flew around in search of water. The sun blazed in the sky, and the dry air made the crow feel even thirstier...",
  "max_length": 200,
  "min_length": 30,
  "num_beams": 4
}
```

### Example Response

```json
{
  "summary": "On a hot summer day, a thirsty crow flew around in search of water. The crow found a pot with low water and used pebbles to raise the water level, finally quenching its thirst."
}
```





## Future Improvements
- Deploy the model to cloud platforms for global accessibility.
- Enable summarization for larger text inputs by splitting them into manageable chunks.


Feel free to contribute or raise issues for enhancements! 😊