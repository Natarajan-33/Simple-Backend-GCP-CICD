from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from typing import Dict
from dotenv import load_dotenv
import os

app = FastAPI(title="Quote API", description="A simple API to get random quotes")

load_dotenv()

# Read comma-separated origins from environment variable
origin_env = os.getenv("ALLOWED_ORIGINS", "")
origins = [origin.strip() for origin in origin_env.split(",") if origin]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Hardcoded quotes list
QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "Be the change you wish to see in the world. - Mahatma Gandhi",
    "In the middle of difficulty lies opportunity. - Albert Einstein",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "It is during our darkest moments that we must focus to see the light. - Aristotle",
    "Whoever is happy will make others happy too. - Anne Frank",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson",
    "You will face many defeats in life, but never let yourself be defeated. - Maya Angelou",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Never let the fear of striking out keep you from playing the game. - Babe Ruth",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "Many of life's failures are people who did not realize how close they were to success when they gave up. - Thomas A. Edison",
    "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. - Dr. Seuss",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "If you want to lift yourself up, lift up someone else. - Booker T. Washington",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "Don't judge each day by the harvest you reap but by the seeds that you plant. - Robert Louis Stevenson",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "In this life we cannot do great things. We can only do small things with great love. - Mother Teresa",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "I can't change the direction of the wind, but I can adjust my sails to always reach my destination. - Jimmy Dean",
    "Nothing is impossible, the word itself says 'I'm possible'! - Audrey Hepburn",
    "The question isn't who is going to let me; it's who is going to stop me. - Ayn Rand",
    "The mind is everything. What you think you become. - Buddha",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "An unexamined life is not worth living. - Socrates",
    "Eighty percent of success is showing up. - Woody Allen",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Winning isn't everything, but wanting to win is. - Vince Lombardi",
    "I am not a product of my circumstances. I am a product of my decisions. - Stephen Covey",
    "Every child is an artist. The problem is how to remain an artist once he grows up. - Pablo Picasso",
    "You can never cross the ocean until you have the courage to lose sight of the shore. - Christopher Columbus",
    "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel. - Maya Angelou",
    "Either you run the day, or the day runs you. - Jim Rohn",
    "Whether you think you can or you think you can't, you're right. - Henry Ford",
    "The two most important days in your life are the day you are born and the day you find out why. - Mark Twain",
    "Too many of us are not living our dreams because we are living our fears. - Les Brown",
    "Limitations live only in our minds. But if we use our imaginations, our possibilities become limitless. - Jamie Paolinetti",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "We become what we think about. - Earl Nightingale",
    "The mind is everything. What you think you become. - Buddha",
    "The best revenge is massive success. - Frank Sinatra",
    "People often say that motivation doesn't last. Well, neither does bathing. That's why we recommend it daily. - Zig Ziglar",
    "Life shrinks or expands in proportion to one's courage. - Anais Nin",
    "If you hear a voice within you say 'you cannot paint,' then by all means paint and that voice will be silenced. - Vincent Van Gogh",
    "There is only one way to avoid criticism: do nothing, say nothing, and be nothing. - Aristotle",
    "Ask and it will be given to you; search, and you will find; knock and the door will be opened for you. - Jesus",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "Go confidently in the direction of your dreams. Live the life you have imagined. - Henry David Thoreau",
    "When I stand before God at the end of my life, I would hope that I would not have a single bit of talent left and could say, I used everything you gave me. - Erma Bombeck",
    "Few things can help an individual more than to place responsibility on him, and to let him know that you trust him. - Booker T. Washington",
    "Certain things catch your eye, but pursue only those that capture the heart. - Ancient Indian Proverb",
    "Believe in yourself! Have faith in your abilities! Without a humble but reasonable confidence in your own powers you cannot be successful or happy. - Norman Vincent Peale",
    "If you can dream it, you can achieve it. - Zig Ziglar",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "People who are crazy enough to think they can change the world, are the ones who do. - Rob Siltanen",
    "Failure will never overtake me if my determination to succeed is strong enough. - Og Mandino",
    "We may encounter many defeats but we must not be defeated. - Maya Angelou",
    "Knowing is not enough; we must apply. Wishing is not enough; we must do. - Johann Wolfgang von Goethe",
    "Imagine your life is perfect in every respect; what would it look like? - Brian Tracy",
    "We generate fears while we sit. We overcome them by action. - Dr. Henry Link",
    "Whether you think you can or think you can't, you're right. - Henry Ford",
    "Security is mostly a superstition. Life is either a daring adventure or nothing. - Helen Keller",
    "The man who has no imagination has no wings. - Muhammad Ali",
    "A person who never made a mistake never tried anything new. - Albert Einstein",
    "The person who says it cannot be done should not interrupt the person who is doing it. - Chinese Proverb",
    "There are no traffic jams along the extra mile. - Roger Staubach",
    "It is never too late to be what you might have been. - George Eliot",
    "You become what you believe. - Oprah Winfrey",
    "I would rather die of passion than of boredom. - Vincent van Gogh",
    "A truly rich man is one whose children run into his arms when his hands are empty. - Unknown",
    "It is not what you do for your children, but what you have taught them to do for themselves, that will make them successful human beings. - Ann Landers",
    "If you want your children to turn out well, spend twice as much time with them, and half as much money. - Abigail Van Buren",
    "Build your own dreams, or someone else will hire you to build theirs. - Farrah Gray",
    "The battles that count aren't the ones for gold medals. The struggles within yourself–the invisible battles inside all of us–that's where it's at. - Jesse Owens",
    "Education costs money. But then so does ignorance. - Sir Claus Moser",
    "I have learned over the years that when one's mind is made up, this diminishes fear. - Rosa Parks",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. - Oprah Winfrey",
    "Remember that not getting what you want is sometimes a wonderful stroke of luck. - Dalai Lama",
    "You can't use up creativity. The more you use, the more you have. - Maya Angelou",
    "Dream big and dare to fail. - Norman Vaughan",
    "Our lives begin to end the day we become silent about things that matter. - Martin Luther King Jr.",
    "Do what you can, where you are, with what you have. - Teddy Roosevelt",
    "If you do what you've always done, you'll get what you've always gotten. - Tony Robbins",
    "Dreaming, after all, is a form of planning. - Gloria Steinem",
    "It's your place in the world; it's your life. Go on and do all you can with it, and make it the life you want to live. - Mae Jemison",
    "You may be disappointed if you fail, but you are doomed if you don't try. - Beverly Sills",
    "Remember no one can make you feel inferior without your consent. - Eleanor Roosevelt",
    "Life is what we make it, always has been, always will be. - Grandma Moses",
    "The question isn't who is going to let me; it's who is going to stop me. - Ayn Rand",
    "When everything seems to be going against you, remember that the airplane takes off against the wind, not with it. - Henry Ford",
    "It's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Change your thoughts and you change your world. - Norman Vincent Peale",
    "Either write something worth reading or do something worth writing. - Benjamin Franklin",
    "Nothing is impossible, the word itself says 'I'm possible'! - Audrey Hepburn",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "If you can dream it, you can achieve it. - Zig Ziglar"
]

@app.get("/")
async def root():
    return {"message": "Quote API is running! Visit /quote to get a random quote."}

@app.get("/quote")
async def get_quote() -> Dict[str, str]:
    """Get a random quote from the hardcoded list."""
    quote = random.choice(QUOTES)
    return {"quote": quote}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 