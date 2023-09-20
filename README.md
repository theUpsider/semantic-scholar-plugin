# ChatGPT Plugin for Semantic Scholar

## Overview

This repository contains a ChatGPT plugin to communicate with the [Semantic Scholar API](https://www.semanticscholar.org/product/api/tutorial). The codebase is primarily written in Python and is designed to integrate seamlessly with the ChatGPT plugin API.

[![Python](https://img.shields.io/badge/python-v3.9-blue)]()

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Docker Setup](#docker-setup)
- [Usage](#usage)
- [License](#license)

## Installation

### Prerequisites

- Python 3.9 or higher
- Docker (Optional)

### Clone the Repository

```bash
git clone https://github.com/theUpsider/semantic-scholar-plugin.git
cd semantic-scholar-plugin
```

### Docker Setup

If you'd like to run the application in a Docker container, a `Dockerfile` is provided. Build and run the Docker image as follows:

```bash
docker build -t chatgpt-plugin .
docker run -p 80:5000 chatgpt-plugin
```

#### Docker compose

Alternatively, you can use `docker-compose` to build and run the Docker image:

```bash
docker-compose up -d
```

But be careful, it uses traefik and letsencrypt to generate a certificate for the domain. Make sure to change the compose file to your needs!

## Usage

To use the ChatGPT plugin, follow these steps:

1. **Start the Application**: Run `python app.py` to start the application.
2. **Access the Plugin**: The plugin will be accessible at `http://localhost` (or the port you've configured).
3. **Install in ChatGPT**: [Tutorial](https://platform.openai.com/docs/plugins/introduction)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
