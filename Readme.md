# PDF Prompter

PDF Prompter is a powerful tool that lets you upload PDFs and ask questions about their content. This tool employs OpenAI's natural language processing capabilities, providing intelligent and context-aware responses to your inquiries. The application is inspired by [Benny's Mind Hack's article](https://bennycheung.github.io/ask-a-book-questions-with-langchain-openai).

## Requirements

* Docker
* Python 3.11.3+
* OpenAI API key

## Dependencies

* langchain
* pypdf2
* python-dotenv
* streamlit
* OpenAI
* tiktoken
* faiss-cpu

These dependencies are listed in the `requirements.txt` file and will be automatically installed within the Docker container

## Project Structure

.
├── Dockerfile
├── requirements.txt
├── .env
├── .gitignore
└── main.py

## Installation

**1. Clone the repository:**

```bash
git clone https://github.com/yourusername/pdf-prompter.git
cd pdf-prompter
```

**2. Create a .env file using .env.example as a template:**

```bash
cp .env.example .env
```

Then, open the .env file and replace 'your_api_key_goes_here' with your actual OpenAI API key:

```bash
OPENAI_API_KEY='your_api_key_goes_here'
```

The .gitignore file is already configured to ignore .env to protect your sensitive information.

**3.Build and run the Docker container:**

```bash
docker build -t pdf-prompter .
docker run -p 8501:8501 pdf-prompter
```

The Dockerfile in this repository is set up to create a Docker container with Python 3.11.3, copy the local directory (which includes your newly created .env file) into the container, install the necessary dependencies, and start the Streamlit app. After running the `docker run` command, the Streamlit app will be available on your local machine at <http://localhost:8501>.

## Usage

Navigate to <http://localhost:8501> on your web browser.
Use the file uploader to upload your PDF.
Type your question in the text input field and hit enter.

## License

This project is licensed under the MIT License.

## Contact

For any queries or further clarification, please feel free to reach out at: <jeff@goodinglabs.com>
