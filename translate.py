import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_text(text, target_language="Swedish"):
    prompt = f"Translate the following English text to {target_language}: \n\n{text}\n\n"
    response = openai.completions.create(
        model="gpt-3.5",  # Adjust the model if needed
        prompt=prompt,
        max_tokens=1024,  # Adjust as needed
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def translate_files(directory="docs"):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                translated_content = translate_text(content)
                new_file_path = file_path.replace(".md", f"_{target_language.lower()}.md")
                with open(new_file_path, 'w', encoding='utf-8') as f:
                    f.write(translated_content)

translate_files()
