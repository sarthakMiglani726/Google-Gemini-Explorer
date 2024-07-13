# Gemini Explorer

Gemini Explorer is an interactive chatbot application powered by Google Gemini AI. It leverages Vertex AI and Streamlit to provide a user-friendly interface for engaging with the AI model.

## Features

- Interactive chat interface
- Personalized user experience with name input
- Session management to maintain chat history

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.7 or higher
- Vertex AI Python client library
- Streamlit

### Installation

1. Clone the repository:

```bash
git clone https://github.com/sarthakMiglani726/Google-Gemini-Explorer.git
cd Google-Gemini-Explorer
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Configuration

Update the `project` variable in the `vertexai.init` function call with your Google Cloud project ID:

```python
project = "your-google-cloud-project-id"
vertexai.init(project=project)
```

### Running the Application

Start the Streamlit application by running:

```bash
streamlit run app.py
```

### Usage

1. Enter your name when prompted.
2. Interact with the AI by typing queries into the chat input.
3. The chat history is maintained throughout the session.

### Main Components

- vertexai: Initializes Vertex AI with the specified project.
- GenerativeModel: Configures the generative model with specific parameters.
- ChatSession: Manages the chat session and history.
- llm_function: Sends user queries to the AI model and handles responses.
