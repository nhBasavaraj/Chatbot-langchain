# Chatbot Projects with LangChain and Streamlit

This repository contains two chatbot projects that leverage LangChain, OpenAI, Ollama, Phi-3 and Streamlit for creating interactive chatbots. Each project demonstrates the use of different language models and configurations.

## Files in the Repository

1. **locallama-Phi3.py**: A chatbot implementation using the Phi-3 model with Ollama.
2. **openai-bot.py**: A chatbot implementation using the OpenAI GPT-3.5-turbo model.
3. **requirements.txt**: A file listing the dependencies required to run the projects.

## Project Details

### locallama-Phi3.py

This project sets up a chatbot using the Phi-3 model provided by Ollama. The application uses Streamlit for the frontend interface.

#### Key Features:
- **Language Model**: Phi-3 by Ollama
- **Prompt Template**: Configured to make the chatbot respond as a helpful assistant.
- **Environment Variables**: Utilizes `.env` file to securely load API keys for OpenAI and LangChain.
- **Streamlit Interface**: Provides a text input for user queries and displays the chatbot responses.


### openai-bot.py

This project sets up a chatbot using the GPT-3.5-turbo model provided by OpenAI. The application uses Streamlit for the frontend interface.

#### Key Features:
- **Language Model: GPT-3.5-turbo by OpenAI
- **Prompt Template: Configured to make the chatbot respond as a helpful assistant.
- **Environment Variables: Utilizes .env file to securely load API keys for OpenAI and LangChain.
- **Streamlit Interface: Provides a text input for user queries and displays the chatbot responses.



## Requirements

The `requirements.txt` file contains the necessary dependencies to run the projects. Install them using the following command:

```bash
pip install -r requirements.txt

  ```

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo-name
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the project root directory and add your OpenAI and LangChain API keys:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    LANGCHAIN_API_KEY=your_langchain_api_key
    ```

5. Run the applications:

    ```bash
    streamlit run locallama-Phi3.py
    ```
    or
    ```bash
    streamlit run openai-bot.py
    ```

## Usage

1. Install Ollama on your local machine by following the installation instructions provided in the Ollama documentation.

2. Once Ollama is installed, open a command prompt and run the command:
    ```bash
    ollama run phi3
    ```

3. Run the Streamlit application by executing the following command in a separate command prompt or terminal:
    ```bash
    streamlit run locallama-Phi3.py
    ```

4. Open the provided URL in a web browser.

5. Input your question and interact with the chatbot to get relevant information.
