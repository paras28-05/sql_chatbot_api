

# SQL Chatbot API

![GitHub stars](https://img.shields.io/github/stars/paras28-05/sql_chatbot_api)
![GitHub issues](https://img.shields.io/github/issues/paras28-05/sql_chatbot_api)
![GitHub forks](https://img.shields.io/github/forks/paras28-05/sql_chatbot_api)
![License](https://img.shields.io/github/license/paras28-05/sql_chatbot_api)

## Project Description
The SQL Chatbot API is a Python-based project designed to provide a conversational interface for SQL databases. It allows users to interact with databases using natural language queries, making database management more accessible and user-friendly.

## Table of Contents
- [Installation Guide](#installation-guide)
- [Usage](#usage)
- [Features](#features)
- [Configuration & Environment Variables](#configuration--environment-variables)
- [Contributing](#contributing)
- [Social & Contact](#social--contact)

## Installation Guide
1. Clone the repository:
    ```sh
    git clone https://github.com/paras28-05/sql_chatbot_api.git
    ```
2. Navigate to the project directory:
    ```sh
    cd sql_chatbot_api
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To start the chatbot API:
```sh
python app.py
```
Example query:
```python
import requests

response = requests.post('http://localhost:5000/query', json={'query': 'Show all users'})
print(response.json())
```

## Features
- Natural language processing for SQL queries
- Supports multiple database types
- User-friendly interface
- Secure and efficient query handling

## Configuration & Environment Variables
- `DB_HOST`: Database host address
- `DB_USER`: Database user
- `DB_PASSWORD`: Database password
- `DB_NAME`: Database name

## Contributing
Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to get involved.


## Social & Contact
- [GitHub](https://github.com/paras28-05)
```
