#%% Opgave 1

width = float(input("Width of the house?"))
height = float(input("Height of the house"))

print(width*height)

# %% Opgave 2
user = int(input("Input an amount of seconds, to convert to Days, Hours, Minutes and Seconds"))

# % dividere med tallet efter og gemmer RESTEN ... ikke det hele tal der kommer efter divisionen.
seconds = user % 60
minutes = user / 60 % 60
hours = (seconds / 60 / 60) % 24
days = hours % 24
