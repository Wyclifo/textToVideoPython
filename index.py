from gtts import gTTS
# pip install gTTS

# dialogue = """
# Welcome back to Tails from the Wild. I’m Leo the Lion — king of the savannah, protector of the pride.
# And I’m Riley the Rabbit — burrow boss, carrot connoisseur, and part-time podcast producer!
# Today, we tackle a serious topic — why our planet is begging for help.
# Yeah! I mean, the trees are whispering, the rivers are shrinking, and the bees? Buzzing out of town!
# Once, I roared across green plains. Now, I step on plastic wrappers.
# I found a soda can in my burrow yesterday! I thought it was a shiny mushroom… until it hissed at me.
# Deforestation, pollution, climate change… It’s not just a problem for humans. We’re all in this jungle together.
# So what can YOU do, listener? Plant a tree! Pick up litter! Switch to eco-batteries! Say no to single-use lettuce bags!
# I think you meant plastic bags, Riley.
# Oops. Lettuce is fine. Eat more of that, too.
# If we don’t protect nature… there won’t be a wild left to podcast from.
# And that, my furry friends, would be a real tragedy.
# Stay wild. Stay green. And stop throwing trash in our streams!
# """
# get dialogue from the user input
dialogue = str(input("Enter the podcast dialogue: "))


tts = gTTS(text=dialogue, lang='en')
# Save as fileName.mp3
tts.save("lion_rabbit_podcast.mp3")

print("🎧 Podcast audio saved as 'lion_rabbit_podcast.mp3'")
