# DarwixAIHackathon
<img src = "https://img.etimg.com/thumb/width-650,height-488,imgsize-14594,resizemode-75,msid-121912486/tech/funding/genai-startup-darwix-ai-raises-1-5-million-in-seed-funding.jpg" width="300">

Virtual Hackathon for Darwix AI

## About Darwix AI
Building the agent led future to level up customer conversations for omni-channel sales teams across the world.

### The Premise
In software development, code reviews are the lifeblood of a healthy team. They catch
bugs, improve quality, and spread knowledge. However, they are often a source of
friction and a truly mundane task. Written feedback can feel blunt, impersonal, and at
worst, discouraging. A junior developer might feel attacked by a comment like "This is
inefficient," while the senior developer who wrote it was simply being direct. This
communication gap slows down learning and can harm team morale. Your mission is
to build an AI that acts as a bridge, translating raw critique into supportive,
educational guidance, thereby freeing developers from the negative cycle of harsh
feedback.

### Your Mission
Create a program that takes a snippet of code and a list of direct, critical review
comments, and then uses Generative AI to rewrite them. The AI should act as an ideal
senior developer or a patient mentor, rephrasing the feedback to be empathetic,
constructive, and educational, ensuring the recipient understands the "why" behind
the suggestion, not just the "what."

**Digital Skeptic AI** is an assistant designed to help readers critically analyze news articles. Instead of telling you what is "true" or "false," it highlights claims, examines language, and provides questions and prompts to guide your independent verification.

---

## Key Features

1. **Core Claim Extraction:** Identifies 3-5 main factual claims in an article.
2. **Language & Tone Analysis:** Classifies articles as Neutral, Persuasive, Opinionated, or Emotionally Charged.
3. **Red Flag Detection:** Detects loaded language, biases, or poor reporting practices.
4. **Verification Questions:** Generates insightful questions to help readers fact-check the article.
5. **Entity Recognition:** Identifies key people, organizations, and locations with investigation prompts.
6. **Counter-Argument Simulation:** Summarizes the article from a hypothetical opposing viewpoint to highlight biases.

---

## Folder Structure
```
DigitalSkepticAI/
├── main.py                     # Core Python script to generate reports
├── app.py                      # Streamlit frontend
├── config.py                   # Configuration settings (API keys, directories)
├── .env                        # Stores sensitive keys (not committed to Git)
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Files/folders to ignore in Git
│
├── reports/                    # Generated analysis reports (Markdown files)
│
├── utils/                      # Helper functions for different tasks
│   ├── fetch_article.py
│   ├── text_processing.py
│   ├── claim_extraction.py
│   ├── tone_analysis.py
│   ├── red_flags.py
│   ├── verification_questions.py
│   ├── entity_analysis.py
│   └── counter_argument.py
│
├── tests/                      # Unit tests for utility functions
│   ├── test_fetch_article.py
│   ├── test_claim_extraction.py
│   ├── test_tone_analysis.py
│   ├── test_red_flags.py
│   ├── test_verification_questions.py
│   ├── test_entity_analysis.py
│   └── test_counter_argument.py
```

---

## Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/adijha2401/DarwixAIHackathon.git
cd DigitalSkepticAI
```

2. Create a virtual environment and activate it:
```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Set up environment variables:
Create a .env file in the root directory and add your Google Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

5. (Optional) Install SpaCy English model:

```
python -m spacy download en_core_web_sm
```

### Running the Project

Option 1: Streamlit Frontend
```
streamlit run app.py
```
- A browser window opens automatically.
- Paste a news article URL, click Generate Report, and view the interactive analysis.

Option 2: Command-Line
```
python main.py
```
- Enter a URL when prompted.
- The report is generated in reports/analysis_report.md and printed in the terminal.

Additional, not necessary: **Testing Utilities**:-
The tests/ folder contains unit tests for utility modules. Run all tests using:
```
python -m unittest discover tests
```

**Tips for Hackathon Presentation**
1. Entity Recognition: Investigate key people, organizations, and locations mentioned in the article.
Example: "Investigate the author's previous work" or "Check funding of 'The XYZ Institute'."
2. Counter-Argument Simulation: Summarize the article from an opposing viewpoint to highlight potential biases.
3. Interactive Demo: Streamlit frontend allows judges to input any URL and see instant analysis.
4. Clear Visuals: Use the assets/ folder to include logos, diagrams, or screenshots in your README.

**Security Note**
- Do not commit your .env file containing your API key to GitHub. Add .env to .gitignore.
- Use environment variables to securely store and access keys.
