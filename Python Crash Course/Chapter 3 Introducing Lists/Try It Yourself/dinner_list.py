# Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite?  Make a list that
# includes at least three people you'd like to invite to dinner. Then use your list to prin a message to each person,
# inviting them to dinner.
# Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set
# of invitations.  You'll have to think of someone else to invite.
# More Guests: You found a bigger dinner table, so now more space is available.  Think of three more guests to invite.
# Shrinking Guest List: You just found that your new dinner table won't arrive in time for the dinner, and you have
# space for only two guests.

dinner_guests = ['mark', 'john', 'peter']
message = ", would you like to join us for dinner?"

print(f'{dinner_guests[0].title()}{message}')
print(f'{dinner_guests[1].title()}{message}')
print(f'{dinner_guests[2].title()}{message}')

# Changing Guest List:
dinner_guests = ['mark', 'john', 'peter']
cannot_come = 'mark'
dinner_guests.remove(cannot_come)
dinner_guests.insert(0, 'paul')
# I did the below print to make sure 'paul' was added properly
# print(dinner_guests)
message = "can't come, but would you still like to?  I invited Paul."
print(f"{cannot_come.title()} {message}")

# Moving Guest:
dinner_guests = ['paul', 'john', 'peter']
