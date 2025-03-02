# YouTube Video Summarizer 🎥📝

A FastAPI-powered tool that extracts YouTube video transcripts and summarizes them using OpenAI's
GPT models. Perfect for quickly digesting long videos!

---

## Features ✨

- **YouTube Transcript Extraction**: Fetches transcripts automatically.
- **AI-Powered Summaries**: Summarizes content using OpenAI's GPT models.
- **Customizable Output**: Choose the length and format of your summary.

---

## How It Works 🔧

1. **Extract Transcript**: The tool fetches the transcript of a YouTube video using its URL.
2. **Summarize with OpenAI**: The transcript is sent to OpenAI's GPT model to generate a concise
   summary.
3. **Customize Output**: Users can specify the length (e.g., number of paragraphs) and format of the
   summary.

---

## Contributing 🤝

We welcome contributions to improve this tool! Here’s how you can get started:

### Prerequisites

- Python 3.11+
- OpenAI API Key ([Get it here](https://platform.openai.com/))
- Basic knowledge of FastAPI and Docker

### Steps to Contribute

1. **Fork the Repository**:  
   Click the "Fork" button at the top right of this repository to create your own copy.

2. **Clone Your Fork**:

   ```bash
   git clone https://github.com/your-username/youtube-summarizer.git
   cd youtube-summarizer
   ```

3. **Set Up Environment Variables**:

   - Create a `.env` file in the root directory.

4. **Install Dependencies**:  
   Create a virtual environment and install the required packages:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Run the Application Locally**:  
   Start the FastAPI server:

   ```bash
   uvicorn api.main:app --reload
   ```

6. **Make Your Changes**:

   - Add new features, fix bugs, or improve documentation.
   - Write tests for your changes in the `api/tests/` directory.

7. **Submit a Pull Request**:
   - Push your changes to your forked repository.
   - Open a pull request to the `main` branch of this repository.
   - Provide a clear description of your changes and why they’re valuable.

---

## Code Structure 🗂️

```
youtube-summarizer/
├── api/                       # FastAPI app and related code
│   ├── __init__.py
│   ├── main.py                # FastAPI app entry point
│   ├── models/                # Pydantic models
│   ├── routes/                # API endpoints
│   ├── services/              # Business logic (e.g., summarization)
│   ├── utils/                 # Helper functions (e.g., YouTube API calls)
│   └── tests/                 # Unit and integration tests
├── docker-compose.yml         # Docker Compose configuration
├── Dockerfile                 # Dockerfile for the API
├── requirements.txt           # Python dependencies
├── .env.example               # Example environment variables
├── .gitignore                 # Git ignore rules
├── .dockerignore              # Docker ignore rules
└── README.md                  # Project documentation
```

---

## License 📄

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Support the Project 💖

If you find this tool useful, consider supporting its development by subscribing to the hosted
service. For more details, visit [our website](#) (coming soon).

---

Happy coding! 🚀
