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

## Usage

To use the ChatGPT plugin, follow these steps:

1. **Start the Application**: Run `python app.py` to start the application.
2. **Access the Plugin**: The plugin will be accessible at `http://localhost` (or the port you've configured).
3. **Install in ChatGPT**: [Tutorial](https://platform.openai.com/docs/plugins/introduction)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
