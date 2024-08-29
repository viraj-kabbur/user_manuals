import os
from openai import OpenAI

client = OpenAI(
# Set up your OpenAI API key
api_key = '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',
)

def translate_text(text, target_language="Swedish"):

    # Use the Completion.create method for text-based completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # You can change this model if needed
        messages=[
        {
            "role": "user",
            "content": "Translate the following English text to swedish: \n\n{text}\n\n"
        }
    ],
        max_tokens=100000,
        temperature=0.5,
    )
    
    translated_text = response.choices[0].text.strip()
    return translated_text

def translate_file(file_path, target_language="Swedish"):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    translated_content = translate_text(content, target_language)
    
    # Write the translated content to a new file
    output_file_path = file_path.replace('.md', f'_{target_language.lower()}.md')
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(translated_content)

    print(f"Translated {file_path} to {output_file_path}")

# Recursively translate all markdown files in the docs directory
for subdir, dirs, files in os.walk('docs'):
    for file in files:
        if file.endswith('.md'):
            translate_file(os.path.join(subdir, file))
