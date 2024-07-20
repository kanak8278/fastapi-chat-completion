# FastAPI Chat Completion Server

This project is a FastAPI server that provides a chat completion endpoint using a pre-trained language model. It accepts user messages and returns generated responses based on the input. This README file provides information on how to set up, run, and test the server.

## Project Overview

- **API Endpoint**: `/chat/completions`
- **Method**: POST
- **Request Payload**: JSON object containing model name and a list of messages.
- **Response**: JSON object with the model's response.

## Requirements

- Python 3.10 or higher
- Poetry for dependency management

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/fastapi-chat-completion.git
cd fastapi-chat-completion
```

### 2. Install Poetry

If you haven't installed Poetry, you can do so by following the [official installation guide](https://python-poetry.org/docs/#installation).

### 3. Install Dependencies

Install the project dependencies using Poetry:

```bash
poetry install
```

### 4. Environment Variables
Set all the environment variables in the `.env` file. You can use the `.env.template` file as a template.

```bash
cp .env.template .env
```
**Note**: Find the HF_TOKEN in your Hugging Face account and set it in the `.env` file.

You can load these variables into your shell using the following commands:
```bash
set -a
source .env
set +a
```

### 4. Install the Required Model

You need to download the pre-trained model used in the project. Ensure you have internet access as it will download the model weights.

```python
# In a Python shell or script
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b")
```

Run `model.py` to download the model weights and save them. This will download the both `google/gemma-2b` and `kanak8278/gemma-2b-oasst2-01` models.


## Running the Server

### 1. Start the FastAPI Server

Use `uvicorn` to run the FastAPI application:

```bash
poetry run uvicorn server:app --host 0.0.0.0 --port 8000
```

### 2. Access the API Documentation

Once the server is running, you can access the interactive API documentation at:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Testing the Server

### 1. Use `curl` to Test the API

Use request.sh to Test the API
You can use the provided request.sh script to send requests to the server and get formatted responses. This script allows you to pass user content as a command-line argument.

1. Make the script executable:

   ```bash
   chmod +x request.sh
   ```

2. Run the script with your desired user content:

   ```bash
   ./request.sh "Hello, how are you?"
   ```

   Output:
   ```json
   [
      {
         "role": "assistant",
         "content": "user: How are you?\nuser: I'm fine.\nuser: How are"
      }
   ]
   ```

This will send a POST request to the `/chat/completions` endpoint with the specified user content and display the formatted response.


### 2. Stress Test with Multithreading

To stress test the server, use the provided `test.py` script:

```bash
poetry run python test.py "Hello, how are you?"
```

Modify the `NUM_THREADS` variable in `test.py` to control the number of concurrent requests.

**Result**
1. Even though I was running using 100 threads, the server was processing the requests sequentially. I believe that could be due to model.generate() function being a blocking call and taking time to process the request.

2. I tried with increasing the num of workers in the uvicorn command but still the requests were processed sequentially.

3. Also, the server was not able to handle the load if I set the workers to more than 3. It was getting stuck and was not starting the server.


### Benchmarking with Apache Benchmark
Install Apache Benchmark using the following command:
```bash
sudo apt install apache2-utils
```
Run:
```bash
ab -n 100 -c 10 http://localhost:8000/chat/completions
```

Output:
```bash
Benchmarking localhost (be patient)...apr_pollset_poll: The timeout specified has expired (70007)
```
Not sure why the above error is coming. But the server is working fine.