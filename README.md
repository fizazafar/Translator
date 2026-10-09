---
title: English to Urdu Translator
emoji: 🌐
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.0.0
app_file: app.py
pinned: false
---

# English to Urdu Translator

A Gradio app that translates English text into Urdu using the Groq API.

## Configure the API key

For Hugging Face Spaces, open **Settings → Secrets** and add:

- **Name:** `GROQ_API_KEY`
- **Value:** your Groq API key

Optionally set `GROQ_MODEL` as an environment variable/Space variable to select a model available to your Groq account. The default is `llama-3.3-70b-versatile`.

Do not commit your API key to GitHub or any public repository.

## Files

- `app.py` — Gradio interface
- `sources.py` — Groq translation function
- `requirements.txt` — Python dependencies
