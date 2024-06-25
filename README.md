# Language Processing API

This project provides a set of API endpoints for natural language processing tasks using Django Rest Framework (DRF) and NLTK library

## Features

- Tokenize text into words or sentences.
- Perform partial language markup with POS tagging.
- Recognize named entities in text.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/YuraYarmola/NLTK_test_task.git
    cd language-processing-api
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the server**:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### 1. Tokenize Text

- **URL**: `/api/tokenize/`
- **Method**: `POST`
- **Description**: Tokenizes the input text into words or sentences based on the specified mode.

#### Request
```json
{
    "text": "This is a sample text.",
    "mode": "word"  // Optional, can be "word" or "sentence". Default is "word".
}
```

#### Response
- **Status**: `200 OK`
- **Body**:
  - If mode is "word":
    ```json
    ["This", "is", "a", "sample", "text", "."]
    ```
  - If mode is "sentence":
    ```json
    ["This is a sample text."]
    ```

- **Status**: `400 Bad Request`
- **Body**:
  ```json
  {"error": "Invalid mode"}
  ```

### 2. Partial Language Markup

- **URL**: `/api/partial-language-markup/`
- **Method**: `POST`
- **Description**: Performs POS tagging on the input text.

#### Request
```json
{
    "text": "This is a sample text.",
    "language": "eng"  // Optional, default is "eng".
}
```

#### Response
- **Status**: `200 OK`
- **Body**:
  ```json
  [["This", "DT"], ["is", "VBZ"], ["a", "DT"], ["sample", "NN"], ["text", "NN"], [".", "."]]
  ```

### 3. Recognize Named Entities

- **URL**: `/api/recognize-named-entities/`
- **Method**: `POST`
- **Description**: Recognizes named entities in the input text.

#### Request
```json
{
    "text": "Barack Obama was born in Hawaii."
}
```

#### Response
- **Status**: `200 OK`
- **Body**:
  ```json
  [["PERSON", "Barack Obama"], ["GPE", "Hawaii"]]
  ```