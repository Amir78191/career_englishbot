import logging
import random
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Кнопки главного меню
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("📖 Business Vocabulary"))
keyboard.add(KeyboardButton("📝 Writing Zone"))
keyboard.add(KeyboardButton("🎙 Speaking Practice"))
keyboard.add(KeyboardButton("🎯 Daily Quizzes"))
keyboard.add(KeyboardButton("💼 Interview Trainer"))

# Секции и ответы
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
        "Business culture terms 🌐",
        "Work ethics and values 🧭"
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
        "🎤 Please send a voice message answering: What's your favorite hobby?",
        "🎤 Voice reply: How do you introduce yourself in a meeting?",
        "🎤 Talk about a time you solved a problem at work.",
        "🎤 Describe your ideal job.",
        "🎤 What motivates you in your career?",
        "🎤 How do you manage stress at work?",
        "🎤 Talk about your strengths and weaknesses.",
        "🎤 What’s a recent business trend you noticed?",
        "🎤 Give your 30-second elevator pitch.",
        "🎤 Share your favorite business book.",
        "🎤 Describe your work style.",
        "🎤 What’s your dream company?",
        "🎤 What role do you usually play in a team?",
        "🎤 How do you handle deadlines?",
        "🎤 Talk about a challenging business task."
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
        "Describe a time you worked in a team 🤝",
        "What are your salary expectations? 💵",
        "Why do you want to change careers? 🔄",
        "What are your short-term goals? 🥅"
    ],
    "🎯 Daily Quizzes": [
        {"question": "What does 'ROI' stand for? 🤔", "answer": "Return on Investment"},
        {"question": "What is 'B2B'? 📊", "answer": "Business to Business"},
        {"question": "What does 'KPI' mean? 📈", "answer": "Key Performance Indicator"},
        {"question": "What does 'CRM' stand for? 🧑‍💼", "answer": "Customer Relationship Management"},
        {"question": "What is 'SEO'? 🔍", "answer": "Search Engine Optimization"},
        {"question": "What is 'GDP'? 📊", "answer": "Gross Domestic Product"},
        {"question": "What does 'SaaS' stand for? 💻", "answer": "Software as a Service"},
        {"question": "What is 'P&L'? 📑", "answer": "Profit and Loss"},
        {"question": "What is 'PR' in business? 📢", "answer": "Public Relations"},
        {"question": "What is 'IPO'? 📈", "answer": "Initial Public Offering"},
        {"question": "What does 'B2C' mean? 🏬", "answer": "Business to Consumer"},
        {"question": "What is 'A/B testing'? ⚙️", "answer": "Comparing two versions to find the better one"},
        {"question": "What is 'VC'? 💼", "answer": "Venture Capital"},
        {"question": "What is 'SWOT'? 📉", "answer": "Strengths, Weaknesses, Opportunities, Threats"},
        {"question": "What is 'CSR'? 🌱", "answer": "Corporate Social Responsibility"},
        {"question": "Define 'benchmarking' 📊", "answer": "Comparing performance to industry bests"},
        {"question": "Meaning of 'turnover' 💰", "answer": "Revenue or employee rotation"},
        {"question": "Define 'stakeholder' 👥", "answer": "Anyone affected by a company’s actions"},
        {"question": "What is 'net profit'? 💵", "answer": "Revenue minus expenses"},
        {"question": "What is a 'pitch'? 🗣", "answer": "Presentation to persuade"},
        {"question": "What is 'synergy'? 🤝", "answer": "Combined effect greater than parts"},
        {"question": "Define 'scalability' 🚀", "answer": "Ability to grow efficiently"},
        {"question": "What is 'liquidity'? 💧", "answer": "Ease of converting assets to cash"},
        {"question": "Meaning of 'merger' 🧩", "answer": "Two companies joining"},
        {"question": "What is a 'startup'? 🛠", "answer": "New business venture"},
        {"question": "Define 'cash flow' 💸", "answer": "Movement of money in and out"},
        {"question": "What is 'branding'? 🔖", "answer": "Creating a unique business image"},
        {"question": "Meaning of 'freemium'? 🎁", "answer": "Free service with optional upgrades"},
        {"question": "What is 'outsourcing'? 🏢", "answer": "Delegating tasks externally"},
        {"question": "What is 'IPO'? 📈", "answer": "Initial Public Offering"}
    ]
}

user_section = {}

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer("Welcome to Career EnglishBot! 👋 Choose a section below:", reply_markup=keyboard)

@dp.message_handler(lambda m: m.text in responses)
async def handle_section(message: types.Message):
    user_section[message.chat.id] = message.text
    section = message.text

    if section == "🎯 Daily Quizzes":
        quiz = random.choice(responses[section])
        user_section[message.chat.id] = quiz
        await message.answer(quiz['question'])

    elif section == "🎙 Speaking Practice":
        prompt = random.choice(responses[section])
        await message.answer(prompt)

    elif section == "💼 Interview Trainer":
        question = random.choice(responses[section])
        user_section[message.chat.id] = question
        await message.answer(question)

    else:
        await message.answer("\n".join(responses[section]))

@dp.message_handler(content_types=types.ContentType.VOICE)
async def handle_voice(message: types.Message):
    section = user_section.get(message.chat.id)
    if section == "🎙 Speaking Practice":
        await bot.forward_message(chat_id=ADMIN_ID, from_chat_id=message.chat.id, message_id=message.message_id)

        markup = InlineKeyboardMarkup()
        for label in ["✅ Very nice", "🗣 Work on pronunciation", "❌ Wrong grammar", "📘 Improve fluency"]:
            markup.add(InlineKeyboardButton(label, callback_data=f"reply:{message.chat.id}:{label}"))
        await bot.send_message(ADMIN_ID, f"Voice from {message.chat.id} in Speaking Practice:", reply_markup=markup)

@dp.message_handler()
async def handle_response(message: types.Message):
    section = user_section.get(message.chat.id)

    if section == "🎯 Daily Quizzes":
        quiz = user_section.get(message.chat.id)
        if quiz and quiz['answer'].lower() in message.text.lower():
            await message.answer("✅ Correct!")
        else:
            await message.answer(f"❌ Incorrect. Correct answer: {quiz['answer']}")

    elif section == "💼 Interview Trainer":
        await bot.send_message(ADMIN_ID, f"Interview answer from {message.chat.id}:\nQ: {section}\nA: {message.text}")

@dp.callback_query_handler(lambda c: c.data.startswith("reply:"))
async def handle_admin_reply(callback_query: types.CallbackQuery):
    _, user_id, reply = callback_query.data.split(":")
    await bot.send_message(int(user_id), reply)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)at work? 🧘‍♂️",
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