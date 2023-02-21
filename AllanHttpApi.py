from flask import Flask
import random

app = Flask(__name__)

bird_facts = [
  "The chicken is the closest living relative to the Tyrannosaurus Rex.",
  "Many birds kept as pets, including doves, parakeets, and lovebirds, enjoy living in pairs for companionship.",
  "The smallest bird egg belongs to the hummingbird and is the size of a pea.",
  "The largest bird egg, from which the ostrich hatches, is the size of a cantaloupe.",
  "The penguin is the only bird that can swim, but not fly.",
  "Owls can turn their heads almost a complete circle, but are unable to move their eyes.",
  "The first bird domesticated by humans was the goose.",
  "Kiwi birds are blind, so they hunt by smell.",
  "Crows have the largest brains relative to body size of any avian family.",
  "Mockingbirds can imitate many sounds, from a squeaking door to a cat meowing."
]

@app.route('/')
def display_bird_fact():
    index = random.randint(0, len(bird_facts) - 1)
    return "Random bird fact: " + bird_facts[index];

app.run(host = "0.0.0.0")