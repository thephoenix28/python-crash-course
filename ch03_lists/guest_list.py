# I practiced using claude for these exercices 
# Exercise 3-4: Original invitations
guests = ['Marie Curie', 'Leonardo da Vinci', 'Maya Angelou']

for guest in guests:
    print(f"Dear {guest}, I would love to have you join me for dinner. Please come!")

# Exercise 3-5: One guest can't make it
print(f"\n{guests[1]} can't make it to dinner.")
guests[1] = 'Nikola Tesla'

print()
for guest in guests:
    print(f"Dear {guest}, I would love to have you join me for dinner. Please come!")

# Exercise 3-6: Bigger table
print("\nGreat news — I found a bigger table! I can invite more guests.")

guests.insert(0, 'Ada Lovelace')
guests.insert(len(guests) // 2, 'Albert Einstein')
guests.append('Frida Kahlo')

print()
for guest in guests:
    print(f"Dear {guest}, I would love to have you join me for dinner. Please come!")

# Exercise 3-7: Table won't arrive in time — only 2 spots
print("\nUnfortunately, the new table won't arrive in time. I can only invite two guests.")

while len(guests) > 2:
    uninvited = guests.pop()
    print(f"Sorry, {uninvited}, I'm afraid I can't invite you to dinner after all.")

print()
for guest in guests:
    print(f"Dear {guest}, you're still invited to dinner. I look forward to seeing you!")

del guests[0]
del guests[0]
print(f"\nGuest list: {guests}")
