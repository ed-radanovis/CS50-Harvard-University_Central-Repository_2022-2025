<DOCUMENT filename="README.md">

<p align="center">
  <img src="../materials/images/openai_logo.png" min-width="100px" width="80" min-height="100px" height="80px" alt="OpenAi logo">
  <img src="../materials/images/icon_ai.png" min-width="100px" width="250" min-height="100px" height="250px" alt="AI image">
  <img src="../../week_6_0_python/materials/images/python_logo.png" min-width="100px" width="80" min-height="100px" height="80px" alt="Python logo">
</p>

<br>

# CS50 - Class 6: AI and Python Integration

## Introduction to Computer Science

### Week 6 – Artificial Intelligence Concepts & Python Implementation

Taught by **Dr. David J. Malan, Ph.D.**

<br>

This section explores **Artificial Intelligence concepts** and their implementation in Python, focusing on practical applications demonstrated in CS50's AI teaching tools.

<br>

> 🎯 Learning Objectives :
>
> > - Understand `fundamental AI concepts` and their practical applications.
> > - Implement `AI-powered assistants` using **_[Python](https://www.python.org/)_** and **_[OpenAI](https://openai.com)_** APIs.
> > - Explore `CS50's AI teaching tools` and their educational impact.
> > - Learn about `prompt engineering` and system command design.
> > - Discover `AI algorithms` like decision trees and minimax.
> > - Understand `machine learning` and `large language models`.

<br>

### 📋 AI Concepts Overview

|                 Concept                  | Description                                         | Real-world Application           |
| :--------------------------------------: | --------------------------------------------------- | -------------------------------- |
|       **Generative AI & ChatGPT**        | AI systems that create content (text, images, code) | CS50.ai, content generation      |
| **Prompt Engineering & System Commands** | Designing effective prompts for AI interaction      | CS50 Duck assistant              |
|            **Decision Trees**            | Algorithmic structures for decision-making          | Game AI, classification systems  |
|          **Minimax Algorithm**           | Game theory algorithm for optimal decision making   | Tic-tac-toe, chess AI            |
|           **Machine Learning**           | Algorithms that learn from data and experience      | Pattern recognition, predictions |
|            **Deep Learning**             | Neural network-based learning                       | Image recognition, NLP           |
|     **Large Language Models (LLMs)**     | Massive AI models trained on vast text corpora      | GPT models, conversational AI    |

---

<table align="center">
  <tr>
    <td align="center">
        <img src="../materials/images/ddb50.gif" width="100px" height="100px" alt="Quack50 gif"/>
      <br>
      <sub><b>Quack</b></sub>
    </td>
  </tr>  
</table>

---

### 📚 Key AI Concepts from Lecture

- **Rubber Duck Debugging**: Traditional programming practice of explaining problems to inanimate objects.
- **CS50.ai**: Harvard's AI-powered teaching assistant used by 201,000+ students worldwide.
- **Generative AI**: Systems like ChatGPT that can create text, code, and images.
- **Prompt Engineering**: The art of designing effective prompts for AI systems.
- **Decision Trees**: Algorithmic structures used for classification and decision-making.
- **Minimax Algorithm**: Game theory algorithm for optimal decision making in competitive scenarios.
- **Machine Learning**: Algorithms that improve through experience and data.
- **Deep Learning**: Advanced neural network approaches for complex pattern recognition.
- **Large Language Models**: Massive AI models like GPT trained on extensive text corpora.

---

### 🛠️ Technologies Used

[![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python&logoColor=3776AB)](https://www.python.org/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![OpenAI](https://img.shields.io/badge/-OpenAI_API-333333?style=flat&logo=openai&logoColor=412991)](https://openai.com/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Azure AI](https://img.shields.io/badge/-Azure_AI-333333?style=flat&logo=microsoftazure&logoColor=0078D4)](https://azure.microsoft.com/)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![CS50.ai](https://img.shields.io/badge/-CS50.ai-333333?style=flat&logo=harvard&logoColor=A51C30)](https://cs50.ai/)

---

### 📂 Activity Structure

```bash
week_6_ai_exploration/
└── materials/
    ├── images/
    ├── src/
    │   ├── .env.example         # Environment configuration template
    │   └── cs50_duck.py         # AI teaching assistant implementation
    ├── CS50_class_6_IA.pdf
    └── README.md                # This file
```

---

### 🔍 Key Implementations

<br>

📍 &nbsp;**CS50 Duck Assistant - AI Teaching Tool**

- Objective: Create an AI-powered teaching assistant that helps CS50 students with programming concepts.

```python
# cs50_duck_assistant.py - AI-powered CS50 teaching assistant
# Based on lecture demonstration code

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.environ["API_KEY"])

# System prompt defines the assistant's personality and role
system_prompt = "You are a friendly and supportive teaching assistant for CS50. You are also a duck."

# Get user question
user_prompt = input("What's your question? ")

# Create chat completion with OpenAI API
chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
    model="gpt-4o",
)

# Extract and display response
response_text = chat_completion.choices[0].message.content
print(response_text)
```

---

### ⚙️ Setup and Execution

- [ ] &nbsp;&nbsp;&nbsp;Prerequisites :

✔️ - CS50 VS Code environment at `cs50.dev`.

✔️ - Python 3.x installed and accessible from command line.

✔️ - Active OpenAI account with API access (free credits available for new users).

✔️ - Basic Python Knowledge, understanding of variables, functions, imports, and basic I/O operations.

✔️ - Command Line Proficiency, comfort with terminal navigation and running Python scripts.

<br>

- [x] &nbsp;&nbsp;&nbsp;Workflow for activity :

```bash
# 1. Install required packages
pip install openai python-dotenv

# 2. Set up environment variables
cp .env.example .env
# Edit .env with your OpenAI API key: API_KEY=your_key_here

# 3. Run the CS50 Duck assistant
python cs50_duck_assistant.py

# 4. Example interaction:
# What's your question? How does memory allocation work in C?
# [AI provides detailed explanation with duck analogies]
```

- [x] &nbsp;&nbsp;&nbsp;Configuration Details :

✔️ - Environment File (.env):

```env
# Required: Your OpenAI API key from https://platform.openai.com/api-keys
API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Optional: Customize AI behavior
ASSISTANT_NAME="CS50 Duck"
DEFAULT_MODEL="gpt-4o"
TEMPERATURE=0.7
MAX_TOKENS=1000
```

---

### 🔬 Validation Tests

✔️ **CS50 Duck Assistant** :

- [x] &nbsp;&nbsp;&nbsp;Successfully loads environment variables from `.env` file
- [x] &nbsp;&nbsp;&nbsp;Establishes connection with OpenAI API using valid credentials
- [x] &nbsp;&nbsp;&nbsp;Correctly implements system prompt for "friendly CS50 teaching assistant" personality
- [x] &nbsp;&nbsp;&nbsp;Handles user input and passes it to the AI model appropriately
- [x] &nbsp;&nbsp;&nbsp;Properly extracts and displays AI-generated responses
- [x] &nbsp;&nbsp;&nbsp;Manages API errors gracefully with user-friendly error messages
- [x] &nbsp;&nbsp;&nbsp;Provides relevant, educational responses to programming questions

<br>

✔️ **Environment Configuration** :

- [x] &nbsp;&nbsp;&nbsp;`.env.example` template created with clear documentation
- [x] &nbsp;&nbsp;&nbsp;Environment variables properly isolated from source code
- [x] &nbsp;&nbsp;&nbsp;API keys and sensitive information excluded from version control
- [x] &nbsp;&nbsp;&nbsp;Setup instructions work correctly for new users
- [x] &nbsp;&nbsp;&nbsp;Dependencies correctly specified in requirements.txt

---

### 🧠 Skills Developed

> By completing these class, you will have acquired the following skills and sub-skills:

🧩 **Prompt Engineering** :

- System command design for AI personality
- User interaction patterns
- Context management in conversations
- Response formatting and tone control

<br>

🧩 **AI Algorithms** :

- Decision tree implementation
- Minimax algorithm for game theory
- Machine learning concepts
- Neural network fundamentals

<br>

🧩 **Practical AI Applications** :

- Educational assistance systems
- Code generation and review
- Conceptual explanation tools
- Interactive learning environments

<br>

🧩 **Ethical AI Use** :

- CS50's academic integrity policies
- Responsible AI implementation
- Educational vs. production use cases
- Transparency in AI assistance

---

### 📜 Academic Context & CS50 AI Policy

These implementations demonstrate Harvard CS50's approach to **responsible AI integration in education**:

1. **CS50 AI Policy**: Clear guidelines on acceptable vs. unacceptable AI use
2. **Learning Enhancement**: AI as a supplement to, not replacement for, learning
3. **Skill Development**: Using AI tools to build programming competence

> [!IMPORTANT]
> The CS50 Duck assistant example shows how AI can be **ethically integrated** into programming education, providing 24/7 support while maintaining academic integrity.
> These AI implementations follow CS50's academic integrity policies and demonstrate **educational use cases** of artificial intelligence. They are intended to enhance learning, not replace it. Always follow your institution's guidelines for AI tool usage.

---

<h4 align="center">
  👤 Developed by 
<h4/>
<br>

<table align="center">
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/edmar-radanovis/">
        <img src="/github/foto_perfil.png" width="100px" height="120px" alt="profile picture"/><br>
        <sub><b>Edmar Radanovis</b></sub><br>
        <sub>Full Stack Developer &nbsp;&</sub><br>
        <sub>Bachelor's degree candidate in</sub><br>
        <sub>Software Engineering</sub>
      </a>
    </td>
    <td align="center">
      <a href="https://edwebdev.vercel.app/">
        <img src="/github/Logo_EWD.png" width="200px" height="200px" alt="EWD Apex logo"/><br>
        <sub><b>Ed Web Dev</b></sub><br>
      </a>
    </td>
  </tr>
</table>

<br>
<br>

[⬆ Back to top](#cs50---class-6-ai-and-python-integration)
</DOCUMENT>
