import random
import time
while True:
    y = "p"
    g = "r"
    n = "t"
    s = "h"
    jokes =(
        "Why did the chicken cross the road? I don't know, go ask the chicken!",
        "The Letter Challenge: What appears once in a minute, twice in a moment, but never in a thousand years? Answer: The letter M.",
        "The Living Paradox: I love to be fed, but water kills me. What am I? Answer: Fire.",
        "The Moving Canvas: I have cities, but no houses; forests, but no trees; and water, but no fish. What am I? Answer: A map.",
        "The Daily Shrink: What gets shorter as it gets older? Answer: A candle.",
        "The Fragile Entity: What is so fragile that saying its name breaks it? Answer: Silence.",
        "The Mailbox Trick: What starts with a P, ends with an E, and has thousands of letters? Answer: The Post Office.",
        "The Tech-Savvy Bird: Why do elephants never use computers? Answer: Because they are afraid of the mouse!",
        "The Ocean Greeting: What did the sushi say to the bee? Answer: Wasabi!",
        "The Music Mix-up: What kind of band never plays music? Answer: A rubber band.",
        "The Class Prank: Why did the math book look sad? Answer: Because it had too many problems.",
        "The Architectural Feat: What building has the most stories? Answer: The library!",
        "When teaching the planets, teach them about gas giants. Then, tell them that Uranus is a gas giant. It really is, and I'm telling you, that joke slaps every single time I tell it.",
        "What's brown and sticky? A stick.")
    print(random.choice(y, g, n, s))
    again = input("Do you want to see another joke/riddle? (Y/N): ")
    if again.lower() == 'n':
        break
print("Why did the chicken cross the road?") 
time.sleep(3)
print("I don't know, go ask the chicken!")