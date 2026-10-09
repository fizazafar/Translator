import gradio as gr
from sources import translate_english_to_urdu


def translate_text(text: str) -> str:
    """Translate English text into Urdu."""
    if not text or not text.strip():
        return "Please enter some English text to translate."

    try:
        return translate_english_to_urdu(text.strip())
    except Exception as exc:
        # Keep the interface usable while showing a concise error.
        return f"Translation failed: {exc}"


with gr.Blocks(title="English to Urdu Translator", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # English → Urdu Translator
        Enter English text below and translate it into Urdu using the Groq API.
        """
    )

    with gr.Row():
        english_input = gr.Textbox(
            label="English text",
            placeholder="Type or paste English text here...",
            lines=8,
        )
        urdu_output = gr.Textbox(
            label="Urdu translation",
            placeholder="اردو ترجمہ یہاں ظاہر ہوگا",
            lines=8,
            rtl=True,
            interactive=False,
        )

    with gr.Row():
        translate_button = gr.Button("Translate", variant="primary")
        clear_button = gr.ClearButton([english_input, urdu_output])

    translate_button.click(
        fn=translate_text,
        inputs=english_input,
        outputs=urdu_output,
    )
    english_input.submit(
        fn=translate_text,
        inputs=english_input,
        outputs=urdu_output,
    )

if __name__ == "__main__":
    # Hugging Face Spaces provides its own hosting URL.
    demo.launch()
