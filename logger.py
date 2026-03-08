"""
Conversation logging module.
"""

import os
from datetime import datetime


class ConversationLogger:
    def __init__(self, log_file="conversation_history.log"):
        self.log_file = log_file
        self.setup_log_file()

    def setup_log_file(self):
        """Create or verify log file exists."""
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write("=" * 60 + "\n")
                f.write(f"Conversation History - Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n\n")

    def log_message(self, sender, message):
        """Log a message to the conversation history."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {sender}: {message}\n"
        
        with open(self.log_file, 'a') as f:
            f.write(log_entry)

    def log_session_end(self):
        """Log the end of a conversation session."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a') as f:
            f.write("\n" + "=" * 60 + "\n")
            f.write(f"Session Ended: {timestamp}\n")
            f.write("=" * 60 + "\n\n")

    def get_history(self):
        """Retrieve conversation history."""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                return f.read()
        return "No conversation history found."
