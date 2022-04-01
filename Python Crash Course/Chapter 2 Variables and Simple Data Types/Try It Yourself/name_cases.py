# Personal Message: Use a variable to represent a person's name, and print a message to that person.  Your message
# should be simple, such as, "Hello Eric, would you like to learn some Python today?"
# Name Cases: Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase,
# and title case.
# Famous Quote: Find a quote from a famous person you admire.  Print the quote and the name of its author.  Your
# output should look something like the following, including the quotation marks.
# Famous Quote 2: Repeat above, but this time, represent the famous person's name using a variable called famous_person
# Then compose your message and represent it with a new variable called message.  Print your message.
# Stripping Names: Use a variable to represent a person's name, include some whitespace characters at the beginning and
# end of the name.  Make sure you use each character combination, "\t" and "\n" at least once.

# Personal Message
first_name = "john"
last_name = "smith"
full_name = f"{first_name} {last_name}"
print(f"Hello {full_name.title()}, would you like to learn some Python today?")

# Name Cases
# I will use the above variables
print(full_name.upper())
print(full_name.lower())
print(full_name.title())

# Famous Quote
first_name = "albert"
last_name = "einstein"
full_name = f"{first_name} {last_name}"
print(f'{full_name.title()} once said, "A person who never made a mistake never tried anything new".')

# Famous Quote 2
famous_person = full_name.title()
quote = '"A person who never made a mistake never tried anything new"'
message = f"{famous_person} once said, {quote}."
print(message)

# Stripping Names
full_name = f"\n{first_name}\n{last_name}"
print(full_name)
full_name = f"\t{first_name}\t{last_name}"
print(full_name.lstrip())
print(full_name.rstrip())
print(full_name.strip())
