#%% Opgave 1

width = float(input("Width of the house? "))
height = float(input("Height of the house? "))

print(width*height)

#%% Opgave 2
number = int(input("Input an amount of seconds, to convert to Days, Hours, Minutes and Seconds "))

# % dividere med tallet efter og gemmer RESTEN ... ikke det hele tal der kommer efter divisionen.
seconds = number % 60
minutes = number / 60 % 60
hours = number / 60 / 60 % 24
# days = number / 60 / 60 / 24 % 1     # HUH!?!?! Hvorfor bliver den en float når alle de andre virker som de skal
# days = int(number / 60 / 60 / 24) % 1   # Hvorfor?
days = int(number / 60 / 60 / 24)   # Virker..... nogle gange

print(number ," Seconds is ", days, ": %02d" % hours, ": %02d" % minutes, ": %02d" % seconds)
# print(number ," Seconds is ", days, ":" , hours , ":", minutes, ":", seconds)

# %% Opgave 3
