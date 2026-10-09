"""Groq-backed English-to-Urdu translation helper."""

import os
from groq import Groq


def translate_english_to_urdu(text: str) -> str:
    """
    Translate English text into natural Urdu.

    Set GROQ_API_KEY in your environment or Hugging Face Space Secrets.
    GROQ_MODEL is optional; it can be used to select a model available
    to your Groq account.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Add it in your environment or "
            "Hugging Face Space Settings → Secrets."
        )

    model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert English-to-Urdu translator. "
                    "Translate the user's English text into fluent, natural "
                    "Urdu written in the Urdu script. Preserve the original "
                    "meaning, tone, names, numbers, and formatting where "
                    "practical. Return only the Urdu translation; do not "
                    "add explanations or transliteration."
                ),
            },
            {"role": "user", "content": text},
        ],
        temperature=0.2,
    )

    translation = response.choices[0].message.content
    if not translation:
        raise RuntimeError("The translation service returned an empty response.")
    return translation.strip()
