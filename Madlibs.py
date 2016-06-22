""""
This is a Madlibs app
Written in Python

By Matt H
"""

print "Starting Mad Lib..."

name = raw_input("Enter a name: ")
adj1 = raw_input("Enter an adjective: ")
adj2 = raw_input("Enter a second adjective: ")
adj3 = raw_input("Enter a third adjective: ")
v1 = raw_input("Enter a verb: ")
v2 = raw_input("Enter a second verb: ")
v3 = raw_input("Enter a third verb: ")
n1 = raw_input("Enter a noun: ")
n2 = raw_input("Enter a second noun: ")
n3 = raw_input("Enter a third noun: ")
n4 = raw_input("Enter a fourth noun: ")
animal = raw_input("Name an animal: ")
food = raw_input("Name a food: ")
fruit = raw_input("Name a fruit: ")
number = raw_input("Insert a number: ")
hero = raw_input("Name a Super Hero: ")
country = raw_input("Name a country: ")
dessert = raw_input("Name a dessert: ")
year = raw_input("Insert a year: ")


#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %s s protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %s s very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %s s ruled the world."

print STORY % (adj1, name, v1, adj2, n1, n2, animal, food, v2, n3, fruit, adj3, name, v3, number, name, hero, hero, name, country, name, dessert, name, year, n4)
