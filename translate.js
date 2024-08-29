import fs from 'fs';
import path from 'path';
import OpenAIApi from 'openai';
import Configuration from 'openai';


// Set up your OpenAI API key from environment variables
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

// Function to translate text using OpenAI API
const translateText = async (text, targetLanguage = "Swedish") => {
  const prompt = `Translate the following English text to ${targetLanguage}:\n\n${text}`;

  const response = await openai.chat.completions.create({
    model: "gpt-3.5-turbo", 
    messages: [
      { role: "system", content: "You are a helpful assistant that translates text." },
      { role: "user", content: ${prompt} }
    ],
    max_tokens: 100000,
    temperature: 0.5,
  });

  return response.data.choices[0].text.trim();
};

// Function to translate a file and save the translated content
const translateFile = async (filePath, targetLanguage = "Swedish") => {
  const content = fs.readFileSync(filePath, 'utf-8');
  const translatedContent = await translateText(content, targetLanguage);

  const outputFilePath = filePath.replace('.md', `_${targetLanguage.toLowerCase()}.md`);
  fs.writeFileSync(outputFilePath, translatedContent, 'utf-8');

  console.log(`Translated ${filePath} to ${outputFilePath}`);
};

// Recursively translate all Markdown files in the docs directory
const docsDir = path.join(process.cwd(), 'docs');
const files = fs.readdirSync(docsDir);

files.forEach(async (file) => {
  const filePath = path.join(docsDir, file);
  if (file.endsWith('.md')) {
    await translateFile(filePath);
  }
});
