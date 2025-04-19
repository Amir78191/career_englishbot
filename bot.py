import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import random

API_TOKEN = '7623017087:AAH4hLpQgMev1UjRiEC6-7S7KqQCmcfVLdo'  # Replace with your actual token
ADMIN_ID = 6304947099  # Replace with your Telegram ID to receive forwarded messages

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Define keyboard buttons
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("📖 Business Vocabulary"))
keyboard.add(KeyboardButton("📝 Writing Zone"))
keyboard.add(KeyboardButton("🎙 Speaking Practice"))
keyboard.add(KeyboardButton("🎯 Daily Quizzes"))
keyboard.add(KeyboardButton("💼 Interview Trainer"))

# Sample responses for different sections
responses = {
    "📖 Business Vocabulary": [
        "Marketing, Finance, HR vocab 💼",
        "Business-related words to know 📊",
        "Workplace terms 🏢",
        "Economy and investment terms 💰",
        "Corporate jargon and phrases 🧑‍💼",
        "Tech industry terms 💻",
        "Business meetings vocabulary 🗣",
        "Financial terms and ratios 📉",
        "Negotiation words 🤝",
        "Global economy language 🌍",
        "Startup terminology 🚀",
        "Management language 👩‍💼",
        "Leadership and strategy vocabulary 💡",
        "Business culture terms 🌐"
    ],
    "📝 Writing Zone": [
        "How to write a professional email ✉️",
        "Resume templates 📄",
        "Cover letter tips ✍️",
        "Business letter format 📝",
        "How to write an impactful CV 🖊",
        "Improving your business writing ✍️",
        "Writing formal letters in English 📨",
        "Crafting a perfect LinkedIn profile 🧑‍💼",
        "Tips for writing reports 📈",
        "Writing effective business proposals 📑",
        "How to write a thank-you email 🙏",
        "Requesting meetings in emails 📅",
        "Email etiquette for professionals 🖋",
        "Composing a business presentation 🖥",
        "Writing professional social media posts 📱"
    ],
    "🎙 Speaking Practice": [
        "Let's practice some phrases 🗣",
        "Answer the question: What's your favorite hobby? 🎤",
        "Let's talk about business trends! 📈",
        "How do you introduce yourself in a meeting? 💼",
        "Explain your company's vision in 30 seconds 📊",
        "Talk about a time when you had to solve a problem at work 🤔",
        "Describe the last business event you attended 🗣",
        "What skills are essential for a successful career? 💪",
        "Discuss your favorite business book 📚",
        "Tell me about a challenging project you worked on 📈",
        "Describe your ideal job 💼",
        "What motivates you in your career? 🎯",
        "How do you manage stress at work? 🧘‍♂️",
        "Talk about your strengths and weaknesses 👨‍💼",
        "Give a 30-second elevator pitch about yourself 🚀"
    ],
    "🎯 Daily Quizzes": [
        {"question": "What does 'ROI' stand for? 🤔", "answer": "Return on Investment 💰"},
        {"question": "What is 'B2B'? 📊", "answer": "Business to Business 🤝"},
        {"question": "What does 'KPI' mean? 📈", "answer": "Key Performance Indicator 📊"},
        {"question": "What does 'CRM' stand for? 🧑‍💼", "answer": "Customer Relationship Management 💬"},
        {"question": "What is 'SEO'? 🔍", "answer": "Search Engine Optimization 🌐"},
        {"question": "What is 'GDP'? 📊", "answer": "Gross Domestic Product 💵"},
        {"question": "What does 'SaaS' stand for? 💻", "answer": "Software as a Service 🖥"},
        {"question": "What is 'P&L'? 📑", "answer": "Profit and Loss 📉"},
        {"question": "What is 'PR' in business? 📢", "answer": "Public Relations 📰"},
        {"question": "What is 'IPO'? 📈", "answer": "Initial Public Offering 💵"},
        {"question": "What does 'B2C' mean? 🏬", "answer": "Business to Consumer 🛍"},
        {"question": "What is 'A/B testing'? ⚙️", "answer": "Comparing two versions of something to see which one performs better 📊"},
        {"question": "What is 'VC'? 💼", "answer": "Venture Capital 💵"},
        {"question": "What is 'SWOT'? 📉", "answer": "Strengths, Weaknesses, Opportunities, and Threats 📊"},
        {"question": "What is 'CSR'? 🌱", "answer": "Corporate Social Responsibility 🌍"}
    ],
    "💼 Interview Trainer": [
        "Tell me about yourself 🙋‍♂️",
        "Why should we hire you? 💼",
        "What are your strengths and weaknesses? 💪",
        "Why did you leave your last job? 💼",
        "Describe a difficult situation you’ve overcome 🏅",
        "Where do you see yourself in 5 years? 📅",
        "How do you handle stress at work? 🧘‍♂️",
        "What is your leadership style? 👩‍💼",
        "Why do you want to work here? 🌟",
        "What motivates you to work hard? 🔥",
        "What do you consider your greatest achievement? 🏆",
        "Describe a time when you worked as part of a team 🤝",
        "What are your salary expectations? 💵",
        "Why do you want to change your career path? 🔄"
    ]
}

# Track the user's current section
user_section = {}

# Function to forward messages to admin for Speaking and Interview sections
async def forward_message_to_admin(message: types.Message):
    await bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    original_message = f"User responded in {user_section[message.chat.id]}: {message.text}"
    await bot.send_message(ADMIN_ID, original_message)

# Start command
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Welcome! How can I assist you today? 🤖 Choose a section below 👇", reply_markup=keyboard)

# User chooses a section
@dp.message_handler(lambda message: message.text in responses.keys())
async def choose_section(message: types.Message):
    section = message.text
    user_section[message.chat.id] = section

    # Send the appropriate response based on the section chosen
    if section == "📖 Business Vocabulary":
        await message.answer("Here are some business terms for you to explore 📚: " + ", ".join(responses[section]), reply_markup=keyboard)
    elif section == "📝 Writing Zone":
        await message.answer("Let's dive into writing tips 🖊: " + ", ".join(responses[section]), reply_markup=keyboard)
    elif section == "🎙 Speaking Practice":
        question = random.choice(responses[section])
        await message.answer(question, reply_markup=keyboard)
    elif section == "🎯 Daily Quizzes":
        quiz = random.choice(responses[section])
        await message.answer(quiz['question'], reply_markup=keyboard)
    elif section == "💼 Interview Trainer":
        await message.answer("Let's practice interview questions! 🤝 Here's one for you: " + random.choice(responses[section]), reply_markup=keyboard)

# Handle user answers for speaking practice and quizzes
@dp.message_handler(lambda message: message.text not in responses.keys())
async def handle_answer(message: types.Message):
    section = user_section.get(message.chat.id)

    if section == "🎙 Speaking Practice" or section == "💼 Interview Trainer":
        # Forward the message to admin for manual review
        await forward_message_to_admin(message)
        await message.answer("Thanks for your response! 💬 Your answer has been forwarded to the admin. 👨‍💻", reply_markup=keyboard)

    elif section == "🎯 Daily Quizzes":
        # Check if the answer is correct
        for quiz in responses[section]:
            if quiz['question'] in message.text:
                if message.text.lower() == quiz['answer'].lower():
                    await message.answer("✅ Correct answer! Well done! 🎉", reply_markup=keyboard)
                else:
                    await message.answer(f"❌ Incorrect. The correct answer is: {quiz['answer']}", reply_markup=keyboard)

# Start polling to receive and process messages
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)