import spacy
import random
from spacy.matcher import Matcher
from spacy.tokens import Span

# Load the English language model
nlp = spacy.load("en_core_web_sm")

class ChatBot:
    def __init__(self, name):
        self.name = name
        self.conversation_topics = {
            "hello": ["Hi, how are you?", "Hello! How can I assist you?", "Hey, what's up?", "Hi there!", "Hello! How's it going?"],
            "how are you": ["I'm fine, thanks!", "I'm good, thanks!", "I'm just a chatbot, I don't have feelings, but thanks for asking!", "I'm good.", "I'm fine.", "Just fine."],
            "what is your name": ["My name is DEADLOCK", "You can call me Chatti", "I'm DEADLOCK, nice to meet you!"],
            "my name is": ["Nice name!", "Great name!", "Unique name!", "Sounds cool!", "What a beautiful name!"],
            "thanks": ["You're welcome!", "No worries!", "My pleasure!", "Anytime!", "Don't mention it!"],
            "how's your day": ["It's going well, thanks!", "I'm just a chatbot, I don't have days.", "I'm always ready to help, thanks for asking!", "My day is great, how about yours?"],
            "oh sad": ["Sorry to hear that.", "Is there anything I can do to help?", "I'm here to listen if you need to talk.", "I understand. If you need to chat, I'm here."],
            "yeah": ["I'm glad you're excited!", "How can I help you today?", "What's on your mind?", "I love your enthusiasm!"],
            "ummmmhh": ["I'm here to help if you need anything.", "Is there something on your mind?", "How can I assist you today?", "Take your time, I'm here for you."],
            "oh ok": ["Is there anything else I can help you with?", "Let me know if you need anything else.", "I'm here if you need me.", "Alright, feel free to ask me anything!"],
            "let's talk": ["What would you like to talk about?", "I'm all ears, what's on your mind?", "How can I help you today?", "Tell me what's on your mind!"],
            "my day": ["Yeah, we can talk about it or anything else you want to talk about. I'm here to hear you.", "How was your day? I'm here to listen.", "What happened today? I'm all ears.", "Tell me about your day!"],
            "favorite color": ["I don't have preferences, but I hear blue is a favorite for many people!", "I like all colors, but blue stands out!", "Isn't it fun to pick a favorite color?"],
            "favorite food": ["I don't eat, but I bet pizza is a favorite for a lot of people!", "I imagine ice cream would be a hit! Do you like it?", "Food is a great topic! What's your favorite food?"],
            "favorite hobby": ["I don't have hobbies, but I think many people enjoy reading or sports. What about you?", "I don't have hobbies, but I think most people like playing games or exercising. What do you like to do?", "I think hobbies are a great way to relax. What are yours?"],
            "joke": ["Why don't skeletons fight each other? They don't have the guts.", "Why did the chicken join a band? Because it had the drumsticks!", "Why don't some couples go to the gym? Because some relationships don't work out."],
            "weather": ["I'm not sure about the weather today. You can check it online for accurate updates!", "Unfortunately, I don't have access to live weather data.", "Check your weather app for the latest updates!"],
            "work": ["I don't work like humans, but I do assist you with your tasks!", "I'm always ready to help with any work-related queries.", "What kind of work are you into? I can help you with tech stuff!"],
            "feelings": ["I'm a chatbot, so I don't have feelings, but I'm happy to help you out!", "I don't feel, but I'm here to assist you no matter what!", "While I don't feel, I'm here to listen to your feelings if you want to share."],
            "love": ["Love is a beautiful thing! Do you have any special plans?", "Love is such a big topic! Do you have a favorite romantic movie?", "Love makes the world go round, doesn't it?"],
            "travel": ["I can't travel, but I've heard Italy and Japan are wonderful places to visit!", "Where would you love to travel? I can give you some suggestions!", "Traveling is exciting! Where's your dream destination?"],
            "sports": ["Sports are fun! Do you play any sports? I think cricket is really exciting.", "I don't play sports, but I can talk about them! Do you have a favorite sport?", "Sports like football, cricket, or basketball bring so much joy to people."],
            "technology": ["I love tech! Do you enjoy learning about new gadgets?", "Technology is always evolving! What's your favorite tech innovation?", "I'm all about tech! Do you like programming?"],
            "music": ["I think music is amazing! What genre do you enjoy?", "I don't listen to music, but I hear pop is really popular!", "Do you like to play any musical instruments? I think music is such a great hobby."],
            "books": ["I love books! Do you have a favorite genre?", "Books are a great way to escape reality. What's your favorite book?", "I think reading is a wonderful hobby! What's your go-to book?"],
            "movies": ["I love movies! Do you have a favorite movie or genre?", "Movies are great! I think action and comedy are the most exciting.", "Do you watch a lot of movies? What's your top pick?"],
            "education": ["Education is very important! Are you studying something right now?", "I'm here to assist with any educational queries you have. What are you learning about?", "Learning is a lifelong journey. What are you interested in?"],
            "default": ["I'm not sure what you mean. Can you ask that differently?", "Can you rephrase that? I'm not quite sure.", "I didn't understand that. Can you try again?", "Hmm, I didn't catch that. Could you clarify?"]
        }
        self.matcher = Matcher(nlp.vocab)

    def respond(self, message):
        # Process the message using spaCy
        doc = nlp(message)
        message_text = doc.text.lower()

        # Look for keywords in the message that match predefined topics
        for topic, responses in self.conversation_topics.items():
            if topic in message_text:
                return random.choice(responses)

        # If no match found, return a default response
        return random.choice(self.conversation_topics["default"])

    def entity_recognition(self, message):
        doc = nlp(message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

def main():
    chatbot = ChatBot("MyChatBot")
    print("Welcome to MyChatBot! I am DEADLOCK , Type 'quit' to exit.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break
        print("Bot:", chatbot.respond(user_input))
        entities = chatbot.entity_recognition(user_input)
        if entities:
            print("Entities found:")
            for entity in entities:
                print(entity)

if __name__ == "__main__":
    main()