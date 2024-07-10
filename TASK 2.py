import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import collections.abc
import time
import os
import requests
from bs4 import BeautifulSoup

if not hasattr(time, 'clock'):
    time.clock = time.perf_counter
collections.Hashable = collections.abc.Hashable

# Create object of ChatBot class
bot = ChatBot('Buddy', 
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database_uri='sqlite:///database.sqlite3',
              logic_adapters=[
                  'chatterbot.logic.MathematicalEvaluation',
                  'chatterbot.logic.BestMatch'
              ])

# Training the bot with some more examples
trainer = ListTrainer(bot)
trainer.train([
    'Hi', 'Hello! How can I assist you today?',
    'Hello', 'Hi there! How can I help?',
    'How are you?', 'I am good, how about you?',
    'I am fine, thank you.', 'You are welcome! How can I assist you?',
    'What is your name?', 'My name is Buddy, your chatbot assistant.',
    'What can you do?', 'I can chat with you and answer your questions.',
    'How can you help me?', 'I can provide information and answer your queries.',
    'Tell me a joke.', 'Why don’t scientists trust atoms? Because they make up everything!',
    'What is AI?', 'AI stands for Artificial Intelligence, the simulation of human intelligence in machines.',
    'What is the capital of France?', 'The capital of France is Paris.',
    'What is 2+2?', '2+2 is 4.',
    'How long it will take to receive an order?', 'An order takes 3-5 Business days to get delivered.',
    'I have a complaint.', 'Please elaborate on your concern.',
    'Thank you', 'You are welcome!',
    'Bye', 'Goodbye! Have a nice day!',
    'Open file', 'Which file would you like me to open?',
    'Search on Google', 'What do you want me to search on Google?',
    'Weather', 'Which city weather do you want to know?'
])

# GUI Setup
class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("600x600")
        self.root.configure(bg="white")

        # Chat history display
        self.chat_history = scrolledtext.ScrolledText(self.root, state='disabled', wrap='word', width=60, height=20, bg="light yellow", font=('Helvetica', 12))
        self.chat_history.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # User input
        self.user_input = tk.StringVar()
        self.entry_box = ttk.Entry(self.root, textvariable=self.user_input, width=50, font=('Helvetica', 12))
        self.entry_box.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Send button
        self.send_button = ttk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Action buttons
        self.open_file_button = ttk.Button(self.root, text="Open File", command=self.open_file)
        self.open_file_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.search_google_button = ttk.Button(self.root, text="Search on Google", command=self.search_google)
        self.search_google_button.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        self.weather_button = ttk.Button(self.root, text="Weather", command=self.get_weather)
        self.weather_button.grid(row=2, column=2, padx=10, pady=5, sticky="ew")

        # Configure row and column weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=0)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Initialize chatbot response
        self.bot_response = ''

    def send_message(self):
        user_message = self.user_input.get()
        if user_message.strip() == '':
            messagebox.showwarning("Input Error", "Please type a message.")
            return

        self.display_user_message(user_message)
        self.get_bot_response(user_message)

    def display_user_message(self, message):
        self.chat_history.config(state='normal')
        self.chat_history.insert('end', f"You: {message}\n")
        self.chat_history.config(state='disabled')
        self.chat_history.yview('end')

    def display_bot_message(self, message):
        self.chat_history.config(state='normal')
        self.chat_history.insert('end', f"Bot: {message}\n")
        self.chat_history.config(state='disabled')
        self.chat_history.yview('end')

    def get_bot_response(self, user_message):
        if user_message.lower() == 'open file':
            self.bot_response = "Which file would you like me to open?"
        elif user_message.lower().startswith('open'):
            self.bot_response = self.open_file(user_message)
        elif user_message.lower() == 'search on google':
            self.bot_response = "What do you want me to search on Google?"
        elif user_message.lower().startswith('search'):
            self.bot_response = self.search_google(user_message)
        elif user_message.lower() == 'weather':
            self.bot_response = "Which city weather do you want to know?"
        elif user_message.lower().startswith('weather'):
            self.bot_response = self.get_weather(user_message)
        else:
            self.bot_response = str(bot.get_response(user_message))

        self.display_bot_message(self.bot_response)

    def open_file(self, user_message=''):
        try:
            if user_message:
                file_name = user_message.split(' ', 1)[1]
                if os.path.exists(file_name):
                    with open(file_name, 'r') as f:
                        content = f.read()
                    return f"Content of {file_name}:\n{content}"
                else:
                    return f"File '{file_name}' not found."
        except Exception as e:
            return f"Error opening file: {str(e)}"

    def search_google(self, user_message=''):
        try:
            if user_message:
                query = user_message.split(' ', 1)[1]
                url = f"https://www.google.com/search?q={query}"
                headers = {'User-Agent': 'Mozilla/5.0'}
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
                    if results:
                        return f"Google search results for '{query}':\n{results[0].get_text(separator=' ')}"
                    else:
                        return f"No results found for '{query}' on Google."
                else:
                    return "Error accessing Google."
        except Exception as e:
            return f"Error searching on Google: {str(e)}"

    def get_weather(self, user_message=''):
        try:
            if user_message:
                city = user_message.split(' ', 1)[1]
                url = f"https://wttr.in/{city}?format=%C+%t"
                response = requests.get(url)
                if response.status_code == 200:
                    return f"Weather in {city.capitalize()}:\n{response.text.strip()}"
                else:
                    return f"Could not fetch weather information for {city.capitalize()}."
        except Exception as e:
            return f"Error fetching weather information: {str(e)}"

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()
