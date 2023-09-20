# ChatGPT Plugin for Systematic Literature Review

## Overview

This repository contains a ChatGPT plugin designed to assist in systematic literature reviews. The codebase is primarily written in Python and is designed to integrate seamlessly with the ChatGPT plugin API.

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
git clone https://github.com/theUpsider/systematic-literature-review-chatgptplugin.git
cd systematic-literature-review-chatgptplugin
```

### Docker Setup

If you'd like to run the application in a Docker container, a `Dockerfile` is provided. Build and run the Docker image as follows:

```bash
docker build -t chatgpt-plugin .
docker run -p 80:5000 chatgpt-plugin
```

## Usage

To use the ChatGPT plugin for your systematic literature review, follow these steps:

1. **Start the Application**: Run `python app.py` to start the application.
2. **Access the Plugin**: The plugin will be accessible at `http://localhost:4000` (or the port you've configured).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
