# Agno Multi-Agent Content Creation

A sophisticated multi-agent system that demonstrates two different approaches to AI-powered content creation using the Agno framework. This project compares **Level 4** (stateless coordinated team) and **Level 5** (stateful workflow) agent architectures for creating high-quality, research-backed content.

## 🎯 Overview

This system uses three specialized AI agents to create comprehensive content:
- **Research Agent**: Conducts thorough web research using DuckDuckGo
- **Writing Agent**: Creates engaging, well-structured content from research
- **Editor Agent**: Reviews and polishes content for quality and accuracy

## 🏗️ Architecture Comparison

### Level 4: Coordinated Team (Stateless)
- Agents work together in a coordinated fashion
- No persistent state between tasks
- Team-based decision making
- Automatic task distribution

### Level 5: Stateful Workflow
- Explicit task sequencing with state management
- Data flows between workflow steps
- Maintains context throughout the process
- Direct control over task execution order

## 🛠️ Prerequisites

- **Python**: 3.8 or higher
- **Package Manager**: Conda
- **API Key**: Mistral AI API key

## 🚀 Setup Instructions

### 1. Clone or Download the Project

If you have the code file, save it as `content_creation.py` in your project directory.

### 2. Create Conda Environment

Open **Anaconda Prompt** or **Windows Terminal** and run:

```bash
# Create a new conda environment
conda create -n agno-content python=3.10

# Activate the environment
conda activate agno-content
```

### 3. Install Required Packages

```bash
# Install core dependencies
pip install agno
pip install python-dotenv
pip install rich
pip install duckduckgo_search
```

### 4. Environment Configuration

Create a `.env` file in your project root directory:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

**To get your Mistral API key:**
1. Visit [Mistral AI Console](https://console.mistral.ai/)
2. Sign up or log in
3. Navigate to API Keys section
4. Generate a new API key
5. Copy and paste it into your `.env` file

## 📁 Project Structure

```
your-project-folder/
│
├── content_creation.py    # Main application file
├── .env                   # Environment variables (API keys)
└── README.md              # This file
```

## 🎮 Usage

### Running the Application

1. **Activate your conda environment:**
   ```bash
   conda activate agno-content
   ```

2. **Run the script:**
   ```bash
   python content_creation.py
   ```

### Customizing Content Generation

You can modify the topic and settings in the `__main__` section:

```python
if __name__ == "__main__":
    topic = "Your Custom Topic Here"
    content_type = "blog post"  # or "technical report", "article", etc.
    target_audience = "general public"  # or "healthcare professionals", etc.
```

### Example Topics to Try

- "The Impact of Climate Change on Agriculture"
- "Cybersecurity Best Practices for Small Businesses"
- "The Rise of Remote Work Technologies"
- "Sustainable Energy Solutions for Urban Areas"

## 🔧 Configuration Options

### Agent Customization

You can modify agent behaviors by updating their `instructions`:

```python
research_agent = Agent(
    # ... other parameters
    instructions=[
        "Focus on recent developments (last 2 years)",
        "Prioritize peer-reviewed sources",
        "Include statistical data where available"
    ]
)
```

### Model Selection

Change the Mistral model by updating the `id` parameter:

```python
model=MistralChat(id="mistral-large-latest", api_key=MISTRAL_API_KEY)
# Options: "open-mistral-nemo", "mistral-large-latest", etc.
```

## 📊 Output Format

The application generates:
- **Side-by-side comparison** of both approaches
- **Rich console formatting** with colors and sections
- **Markdown-formatted content** ready for publication
- **Source citations** in APA format

## 🐛 Troubleshooting

### Common Issues

1. **Import Error for 'agno':**
   ```bash
   pip install --upgrade agno
   ```

2. **API Key Not Found:**
   - Ensure `.env` file is in the project root
   - Check that `MISTRAL_API_KEY` is spelled correctly
   - Verify your API key is valid

3. **Conda Environment Issues:**
   ```bash
   # Reset environment
   conda deactivate
   conda remove -n agno-content --all
   # Then recreate following setup steps
   ```

4. **VS Code Python Path Issues:**
   - Use `Ctrl + Shift + P` → "Python: Select Interpreter"
   - Choose the correct conda environment path

## 📚 Dependencies

- `agno`: Multi-agent framework
- `python-dotenv`: Environment variable management
- `rich`: Enhanced console output

## 🤝 Contributing

To extend this project:

1. **Add new agent types** (e.g., fact-checker, SEO optimizer)
2. **Implement different models** (OpenAI, Anthropic, etc.)
3. **Create custom tools** for specific domains
4. **Add output formats** (PDF, HTML, etc.)

## 📝 License

This project is for educational and demonstration purposes. Check the Agno framework license for commercial usage.

## 🆘 Support

- **Agno Documentation**: [Official Agno Docs](https://docs.agno.com)
- **Mistral AI**: [[Mistral Documentation](https://docs.mistral.ai/)]
- **Issues**: Check your API quotas and internet connection first

## 🎬 Demo Screenshots

### Application in Action

![1](https://github.com/user-attachments/assets/a9a9300b-8354-4022-ae10-5817e255ac6e)
![2](https://github.com/user-attachments/assets/c227719e-4292-409c-9b3e-8490a5edb53a)
![3](https://github.com/user-attachments/assets/c5201a61-ed9b-4bda-825d-30113bec902f)
![4](https://github.com/user-attachments/assets/22e623ec-f13f-4fb5-9a68-471cec4ad548)


## 🎉 Example Output

When you run the script, you'll see:
```
📊 Level 4 vs Level 5 Comparison
════════════════════════════════
## 📝 Level 4 Result
[Coordinated team output with research, writing, and editing]

⬇⬇⬇
════════════════════════════════
## 📝 Level 5 Result  
[Sequential workflow output with maintained state]
```

---

**Happy Content Creating! 🚀**
