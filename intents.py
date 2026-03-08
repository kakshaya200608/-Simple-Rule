"""
Intent patterns and responses for the rule-based chatbot.
"""

INTENTS = {
    "greeting": {
        "patterns": [
            r"hello", r"hi", r"hey", r"good morning",
            r"good afternoon", r"good evening", r"howdy",
            r"greetings", r"what's up"
        ],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Nice to talk to you. How can I assist?",
            "Greetings! What brings you here?"
        ]
    },
    "farewell": {
        "patterns": [
            r"goodbye", r"bye", r"see you", r"take care",
            r"farewell", r"quit", r"exit", r"see you later"
        ],
        "responses": [
            "Goodbye! Have a great day!",
            "Bye! Thanks for chatting with me.",
            "See you later! Feel free to come back anytime.",
            "Take care!"
        ]
    },
    "help": {
        "patterns": [
            r"help", r"can you help", r"what can you do",
            r"capabilities", r"assist", r"support"
        ],
        "responses": [
            "I'm here to help! I can answer questions about Python, provide general information, and have a friendly chat. Try asking me about Python, weather, or just say hello!",
            "Sure! I can help with topics like Python programming, general knowledge questions, and more. What would you like to know?"
        ]
    },
    "python": {
        "patterns": [
            r"python", r"programming", r"code", r"function",
            r"variable", r"loop", r"conditional"
        ],
        "responses": [
            "I'm happy to discuss Python! Python is a versatile programming language known for its readability and ease of use. What specific Python topic interests you?",
            "Python is great! It's widely used for web development, data science, and automation. Do you have a specific question about Python?",
            "Are you interested in learning Python or need help with a specific concept?"
        ]
    },
    "weather": {
        "patterns": [
            r"weather", r"temperature", r"rain", r"sunny",
            r"forecast", r"climate", r"hot", r"cold"
        ],
        "responses": [
            "I don't have access to real weather data, but I can discuss weather patterns and climate! What would you like to know?",
            "Weather can be fascinating! While I can't provide current forecasts, I'm happy to discuss meteorology or climate topics."
        ]
    },
    "small_talk": {
        "patterns": [
            r"how are you", r"how are you doing", r"how do you feel",
            r"what's your name", r"who are you"
        ],
        "responses": [
            "I'm doing great, thanks for asking! I'm a simple chatbot here to help and chat. What's on your mind?",
            "I'm functioning well and ready to help! I'm a rule-based chatbot. How about you?",
            "I'm good! My name is SimplBot. How are you doing today?"
        ]
    },
    "thanks": {
        "patterns": [
            r"thanks", r"thank you", r"appreciate", r"grateful",
            r"thx", r"thanks a lot"
        ],
        "responses": [
            "You're welcome! Happy to help.",
            "Anytime! Let me know if you need anything else.",
            "Glad I could help! Feel free to ask more questions."
        ]
    }
}
