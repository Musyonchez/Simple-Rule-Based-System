# Rule-Based Chatbot

A beginner-friendly Python chatbot project that uses simple keyword matching to respond to user input. This project demonstrates the core concepts behind conversational systems using predefined rules instead of machine learning or AI models.

---

## Overview

This chatbot works by checking whether specific keywords exist in the user's message and then returning a matching response.

It can:
- Respond to greetings
- Provide help messages
- Handle farewells
- Answer simple predefined questions
- Return a default response when it does not understand the input

The project is ideal for:
- Beginners learning Python
- Students studying Artificial Intelligence fundamentals
- Understanding chatbot logic
- Practicing conditional logic and string processing

---

## Features

- Simple and easy-to-understand structure
- Rule-based response system
- Keyword matching using dictionaries
- Interactive command-line conversation
- Customizable responses
- Beginner-friendly Python concepts

---

## Technologies Used

- Python 3

No external libraries are required.

---

## Project Structure

```bash
rule_based_chatbot/
│
├── chatbot.py
└── README.md
```

---

## How the Chatbot Works

The chatbot contains a dictionary of rules:

```python
self.rules = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "bye": "Goodbye! Have a great day!"
}
```

When the user enters a message:
1. The chatbot converts the input to lowercase
2. It checks whether any keyword exists in the sentence
3. If a match is found, the corresponding response is returned
4. If no match exists, a default response is shown

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rule-based-chatbot.git
```

### 2. Navigate to the Project Folder

```bash
cd rule-based-chatbot
```

### 3. Run the Program

```bash
python chatbot.py
```

---

## Full Source Code

```python
# designing a simple rule based system for a chatbot

class RuleBasedChatbot:
    def __init__(self):
        # Define rules for the chatbot
        self.rules = {
            "hello": "Hello! How can I help you today?",
            "hi": "Hi there! What can I do for you?",
            "bye": "Goodbye! Have a great day!",
            "help": "Sure! I'm here to help. What do you need assistance with?",
            "weather": "The weather is sunny today. Don't forget your sunglasses!",
            "name": "I'm a simple rule-based chatbot. I don't have a name, but you can call me Chatbot!"
        }

        self.default_response = (
            "I'm sorry, I don't understand that. Can you please rephrase?"
        )

    def get_response(self, user_input):
        # Check for keywords in the user input
        for keyword, response in self.rules.items():
            if keyword in user_input.lower():
                return response

        return self.default_response


# Example usage
if __name__ == "__main__":
    chatbot = RuleBasedChatbot()

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")
```

---

## Example Interaction

```bash
You: hello
Chatbot: Hello! How can I help you today?

You: what is your name?
Chatbot: I'm a simple rule-based chatbot. I don't have a name, but you can call me Chatbot!

You: weather today
Chatbot: The weather is sunny today. Don't forget your sunglasses!

You: bye
Chatbot: Goodbye! Have a great day!
```

---

## Learning Objectives

Through this project, learners will understand:
- Python classes and objects
- Dictionaries in Python
- String manipulation
- Conditional logic
- Loops
- User input handling
- Basic Natural Language Processing concepts

---

## Limitations of Rule-Based Chatbots

This chatbot is simple and has some limitations:

- Cannot learn from conversations
- Only responds to predefined keywords
- Cannot understand complex sentences
- No memory of previous interactions
- Limited conversational intelligence

---

## Possible Improvements

You can improve this chatbot by adding:
- More conversation rules
- Better keyword matching
- GUI interface using Tkinter
- Voice recognition
- Database support
- AI/NLP integration
- Machine learning capabilities

---

## Future Enhancements

Potential advanced upgrades include:
- Integration with APIs
- Sentiment analysis
- Context-aware responses
- Web-based chatbot interface
- Deployment on cloud platforms
- Integration with Telegram or WhatsApp

---

## Educational Value

This project is excellent for:
- Python programming practice
- AI and chatbot introduction
- Classroom demonstrations
- Beginner software projects
- Understanding conversational systems

---

## License

This project is open-source and free to use for educational purposes.

---

## Author

Developed as a simple educational project to demonstrate how rule-based chatbot systems work using Python.
