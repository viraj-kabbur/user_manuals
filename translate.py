import openai
import os

# Set your OpenAI API key here
openai.api_key = os.environ.get("YOUR_OPENAI_API_KEY")

def translate_text(text, target_language):
    # Construct the prompt for translation
    prompt = f"Translate the following text to {target_language}: \n\n{text}"

    # Use the OpenAI API to generate a translation
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2048,
        temperature=0.3,
    )

    translated_text = response['choices'][0]['message']['content'].strip()
    return translated_text

# Example of how you might read content from a file and translate it
def translate_gitbook_content():
    with open('path/to/your/gitbook/file.md', 'r', encoding='utf-8') as file:
        content = file.read()

    translated_content = translate_text(content, "Swedish")  # Specify the target language

    with open('path/to/your/gitbook/file_sv.md', 'w', encoding='utf-8') as file:
        file.write(translated_content)

if __name__ == "__main__":
    translate_gitbook_content()
