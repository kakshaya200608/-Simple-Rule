"""
Simple Rule-Based Chatbot.
Pattern matching and intent-based responses.
"""

import re
import random
from intents import INTENTS
from knowledge_base import KNOWLEDGE_BASE
from logger import ConversationLogger


class SimpleBotChatbot:
    def __init__(self):
        self.logger = ConversationLogger()
        self.conversation_count = 0

    def extract_intent(self, user_input):
        """
        Extract intent from user input using pattern matching.
        Returns intent name or None if no match found.
        """
        user_input_lower = user_input.lower()
        
        for intent_name, intent_data in INTENTS.items():
            for pattern in intent_data["patterns"]:
                if re.search(pattern, user_input_lower):
                    return intent_name
        
        return None

    def get_intent_response(self, intent):
        """Get a random response for the matched intent."""
        if intent in INTENTS:
            responses = INTENTS[intent]["responses"]
            return random.choice(responses)
        return None

    def search_knowledge_base(self, user_input):
        """
        Search the knowledge base for relevant answers.
        Returns answer if found, None otherwise.
        """
        user_input_lower = user_input.lower()
        
        for question, qa_pair in KNOWLEDGE_BASE.items():
            # Check if question keywords match
            for keyword in qa_pair["keywords"]:
                if keyword in user_input_lower:
                    return qa_pair["answer"]
        
        return None

    def get_response(self, user_input):
        """
        Generate a response based on user input.
        Priority: Knowledge base > Intent matching > Default response
        """
        # First, try to find answer in knowledge base
        kb_answer = self.search_knowledge_base(user_input)
        if kb_answer:
            return kb_answer

        # Then, try to match intent
        intent = self.extract_intent(user_input)
        if intent:
            response = self.get_intent_response(intent)
            if response:
                return response

        # Default response if no match
        return "I'm not sure I understood that. Can you rephrase? Try asking about Python, or type 'help' for more information."

    def chat(self):
        """Main chat loop."""
        print("\n" + "=" * 60)
        print("Welcome to SimplBot - A Rule-Based Chatbot!")
        print("=" * 60)
        print("Type 'exit' or 'quit' to end the conversation.")
        print("Type 'history' to see conversation history.")
        print("Type 'help' for more information about what I can do.")
        print("=" * 60 + "\n")

        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue

                # Log user input
                self.logger.log_message("User", user_input)
                self.conversation_count += 1

                # Check for special commands
                if user_input.lower() in ["exit", "quit"]:
                    farewell = "Thank you for chatting with me! Goodbye!"
                    print(f"\nBot: {farewell}\n")
                    self.logger.log_message("Bot", farewell)
                    self.logger.log_session_end()
                    print(f"Conversation logged to: conversation_history.log")
                    break

                if user_input.lower() == "history":
                    print("\n--- Conversation History ---")
                    print(self.logger.get_history())
                    print("--- End of History ---\n")
                    continue

                # Get and display bot response
                bot_response = self.get_response(user_input)
                print(f"\nBot: {bot_response}\n")

                # Log bot response
                self.logger.log_message("Bot", bot_response)

            except KeyboardInterrupt:
                print("\n\nConversation interrupted by user.")
                self.logger.log_session_end()
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                self.logger.log_message("System", f"Error: {e}")


def main():
    """Entry point for the chatbot."""
    bot = SimpleBotChatbot()
    bot.chat()


if __name__ == "__main__":
    main()
