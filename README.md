# LangChain Practice Project

This project is dedicated to practicing and exploring the **LangChain** framework for building applications with Large Language Models (LLMs).

## Overview

LangChain is a powerful framework that simplifies the development of LLM-based applications by providing modular components and abstractions for common patterns and workflows.

## Project Structure

```
GenAIWithLangchain/
├── ChatModels/          # Chat model integrations and implementations
├── EmbeddingModels/     # Embedding model implementations
├── LLMs/                # LLM demonstrations and examples
├── requirements.txt     # Project dependencies
└── test.py              # Test file
```

## Topics We Will Practice

### 1. **Models**
- Chat Models (OpenAI, Gemini, Hugging Face, Anthropic)
- Embedding Models (OpenAI embeddings)
- Local vs API-based models

### 2. **Prompts**
- Prompt templates
- Prompt engineering and optimization
- Dynamic prompt creation

### 3. **Indexes**
- Vector stores and retrieval
- Document indexing and storage
- Semantic search capabilities

### 4. **Memory**
- Conversation memory
- Long-term memory management
- Context retention across interactions

### 5. **Chains**
- Sequential chains
- Custom chains
- Complex workflow orchestration

### 6. **Agents**
- Agent creation and tools
- Autonomous decision-making
- Multi-step reasoning and planning

## Getting Started

### Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your environment variables:
```bash
# Create a .env file with your API keys
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
# Add other API keys as needed
```

### Running Examples

Execute any of the example files in the respective directories:
```bash
python ChatModels/chatmodel_openai.py
python EmbeddingModels/embedding_openai_query.py
python LLMs/LLM_demo.py
```

## Key Features

- **Multi-Model Support**: Integration with various LLM providers
- **Modular Design**: Clean separation of concerns for different LangChain components
- **Practical Examples**: Real-world use cases and demonstrations
- **Extensible Architecture**: Easy to add new models and features

## Dependencies

See `requirements.txt` for all project dependencies. Key packages include:
- `langchain` - Core LangChain framework
- `langchain-openai` - OpenAI integrations
- `langchain-anthropic` - Anthropic integrations
- `python-dotenv` - Environment variable management

## License

This is a personal learning project.
