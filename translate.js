import fs from 'fs';
import dotenv from 'dotenv';
import path from 'path';
import OpenAIApi from 'openai';
import Configuration from 'openai';
dotenv.config();

// Set up your OpenAI API key from environment variables
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

// Function to translate text using OpenAI API
const translateText = async (text, targetLanguage = "Swedish") => {
  const prompt = `Translate the following English text to ${targetLanguage}:\n\n${text}`;

  const response = await openai.createCompletion({
    model: "text-davinci-003", // Use a text completion model
    prompt: prompt,
    max_tokens: 1000,
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
