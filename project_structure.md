# Project Structure: WealthWise AI

```
wealthwise-ai/
├── src/
│   ├── backend/
│   │   ├── wealthwise/
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   ├── privacy.py
│   │   │   ├── dashboard.py
│   │   │   ├── agent/
│   │   │   │   ├── __init__.py
│   │   │   │   └── graph.py
│   │   │   ├── analysis/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── categorize.py
│   │   │   │   └── embeddings.py
│   │   │   ├── data/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── sample_data.py
│   │   │   │   └── knowledge.py
│   │   │   ├── rag/
│   │   │   │   ├── __init__.py
│   │   │   │   └── knowledge_base.py
│   │   │   └── tools/
│   │   │       ├── __init__.py
│   │   │       ├── calculators.py
│   │   │       ├── knowledge_tool.py
│   │   │       └── transaction_tools.py
│   │   └── server.py
│   ├── frontend/
│   │   └── index.html
│   └── streamlit_ui/
│       └── app.py
├── main.py
├── test_upload.py
├── requirements.txt
├── render.yaml
├── .env.example
├── README.md
├── project_structure.md
├── LICENSE
└── fingenius-notebook-gemini-agent.ipynb
```
