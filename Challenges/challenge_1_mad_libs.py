# Write a story with some words missing
story = """
Roses are {colour}
Violets are {colour2}
Sugar is {adjective}
And so are you
"""

# Ask the user to provide the missing words
colour = input("Give me a colour")
colour2 = input("Give me another colour")
adjective = input("How do you feel?")
# Display the final story
print(story.format(colour=colour, colour2=colour2, adjective=adjective))
