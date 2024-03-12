# Chatbot Application with GPT-Neo

This project is a chatbot application that utilizes the GPT-Neo model from the Hugging Face Transformers library to generate human-like text responses. Built with Flask for the backend and a simple HTML/JavaScript frontend, it's designed to demonstrate how to integrate AI models into web applications. This chatbot is also configured to be deployable on AWS Elastic Beanstalk and uses Cloudflare for domain management and additional security features.

## Features

- Text generation using GPT-Neo 125M model.
- Flask backend with RESTful API endpoint.
- Simple and responsive HTML/JavaScript frontend.
- Cross-Origin Resource Sharing (CORS) enabled.
- Deployment configuration for AWS Elastic Beanstalk.
- Custom domain configuration via Cloudflare.

## Prerequisites

- Python 3.6+
- Pip and Virtualenv
- Docker (for containerization)
- AWS Account (for Elastic Beanstalk deployment)
- Cloudflare Account (for domain management)

## Local Setup

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/yourprojectname.git
cd yourprojectname
Create and Activate a Virtual Environment
```

2. **Create and Activate a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
Install Dependencies
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
Run the Flask Application
```

4. **Run the Flask Application**

```bash
python app.py
Access the application at http://localhost:5000
```

## Deployment

This project includes a Dockerfile for containerization and instructions for deploying to AWS Elastic Beanstalk.

## Building the Docker Container

```bash
docker build -t chatbot-app .
```

## Deploying to AWS Elastic Beanstalk

Refer to the Elastic Beanstalk CLI documentation for details on deploying Docker containers.

## Configuration for Custom Domain via Cloudflare

Instructions for configuring a custom domain managed through Cloudflare are provided. This includes setting up DNS records and SSL/TLS for secure connections.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Hugging Face for the Transformers library.
- The team behind the GPT-Neo model.
