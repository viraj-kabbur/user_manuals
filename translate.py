import os.path
import openai

# Set up your OpenAI API key (this should be stored as a GitHub Secret for security)
openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_text(text, target_language="Swedish"):
    prompt = f"Translate the following English text to {target_language}: \n\n{text}\n\n"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a translator that translates text to {target_language}."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100000,
        temperature=0.5,
    )
    
    translated_text = response['choices'][0]['message']['content'].strip()
    return translated_text

def translate_file(file_path, target_language="Swedish"):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    translated_content = translate_text(content, target_language)
    with open(file_path.replace('.md', f'_{target_language.lower()}.md'), 'w', encoding='utf-8') as file:
        file.write(translated_content)

# Recursively translate all markdown files in the docs directory
for subdir, dirs, files in os.walk('docs'):
    for file in files:
        if file.endswith('.md'):
            translate_file(os.path.join(subdir, file))
