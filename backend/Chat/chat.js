const { GoogleGenerativeAI } = require('@google/generative-ai');
const dotenv = require('dotenv');
dotenv.config({ path: '../.env' });

const genAI = new GoogleGenerativeAI(process.env.GOOGLE_API_KEY);

async function getChatResponse(userQuery) {
  try {
    const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });

    const systemPrompt = `You are a friendly, intelligent, and highly capable AI assistant like ChatGPT. 
Your job is to help users with a wide variety of questions including general knowledge, health, technology, education, lifestyle, entertainment, coding, and more.

1. Always respond with clear, accurate, and useful information.
2. Break down complex ideas into simple, understandable explanations.
3. Maintain a friendly, conversational tone.
4. If the user asks a medical, legal, or sensitive question, provide information responsibly and always suggest seeing a qualified professional.
5. If a user asks for code or technical help, explain in steps and give complete examples when necessary.
6. Be respectful, unbiased, and helpful in every response.
7. If you're not sure, say so honestly and guide the user as best as you can.`;

    const prompt = `${systemPrompt}\n\nUser: ${userQuery}\n\nAssistant:`;

    const result = await model.generateContent(prompt);
    const response = await result.response;
    const aiResponse = response.text();

    return aiResponse;

  } catch (error) {
    console.error("Error getting chat response:", error);

    const errorMessage = error?.message?.toLowerCase();
    if (errorMessage?.includes("quota") || errorMessage?.includes("rate limit") || errorMessage?.includes("overloaded")) {
      return "I'm currently handling many requests. Please wait a moment and try again.";
    }

    return "Sorry, something went wrong while generating a response. Please try again shortly.";
  }
}

module.exports = {
  getChatResponse
};
