# Day 9: Random quote generator

import random

#list of quotes
quotes = [ 
    "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
    "The way to get started is to quit talking and begin doing. -Walt Disney",
    "If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt",
    "Life is what happens when you're busy making other plans. -John Lennon",
    "Spread love everywhere you go. Let no one ever come to you without leaving happier. -Mother Teresa"
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.- Christian D. Larson"
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
    "The best way to predict your future is to create it. - Abraham Lincoln",
    "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "You can't go back and change the beginning, but you can start where you are and change the ending. - C.S. Lewis",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "The greatest wealth is to live content with little. - Plato",
    "The biggest adventure you can ever take is to live the life of your dreams. - Oprah Winfrey",
    "If you want to go fast, go alone. If you want to go far, go together. - African Proverb",
    "I have not failed. I've just found 10,000 ways that won't work. - Thomas Edison",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Life is like riding a bicycle. To keep your balance, you must keep moving. - Albert Einstein",
    "You can never cross the ocean until you have the courage to lose sight of the shore. - Christopher Columbus",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success is not measured by what you accomplish, but by the opposition you have encountered, and the courage with which you have maintained the struggle against overwhelming odds. - Orison Swett Marden",
    "The only thing we have to fear is fear itself. - Franklin D. Roosevelt",
    "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi",
    "Be the change you wish to see in the world. - Mahatma Gandhi",
    "Change your thoughts and you change your world. - Norman Vincent Peale",
    "The only true wisdom is in knowing you know nothing. - Socrates",
    "We cannot solve our problems with the same thinking we used when we created them. - Albert Einstein",
    "Success is stumbling from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "It always seems impossible until it's done. - Nelson Mandela",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "I can't change the direction of the wind, but I can adjust my sails to always reach my destination. - Jimmy Dean",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "We must accept finite disappointment, but never lose infinite hope. - Martin Luther King Jr.",
    "Happiness is not a destination, it's a journey. - Zig Ziglar",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Life is a journey, and if you fall in love with the journey, you will be in love forever. - Peter Hagerty",
    "Success is liking yourself, liking what you do, and liking how you do it. - Maya Angelou",
    "The most important thing in life is to learn how to give out love, and let it come in. - Morrie Schwartz",
    "Do not wait for leaders; do it alone, person to person. - Mother Teresa",
    "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Happiness is not something you postpone for the future; it is something you design for the present. - Jim Rohn",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "If you want to live a happy life, tie it to a goal, not to people or things. - Albert Einstein",
    "Life is too short to waste your time on people who don't respect, appreciate, and value you. - Roy T. Bennett",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett",
    "The only thing necessary for the triumph of evil is for good men to do nothing. - Edmund Burke"
    
] #generated using ChatGPT lol.

#Generate a random quote with random module
random_quote = random.choice(quotes)

#Print the random quote
print(random_quote)
