my_list = [1, 2, 3, 4, 5]
print(my_list)

friends = ["Mir", "Siam", "Rafi", "Shawon"]
print(friends)
print(friends[1]) # Siam

#Functions for lists
print(friends.count("Siam")) # 1
print(friends.index("Mir")) # 0
print(len(friends)) # 4
print(friends.append("Sifat")) # None
print(friends) # ['Mir', 'Siam', 'Rafi', 'Shawon', 'Sifat']
print(friends.insert(2, "Sifat")) # None
print(friends) # ['Mir', 'Siam', 'Sifat', 'Rafi', 'Shawon', 'Sifat']
print(friends.remove("Sifat")) # None
print(friends) # ['Mir', 'Siam', 'Rafi', 'Shawon', 'Sifat']
print(friends.pop()) # Sifat
print(friends) # ['Mir', 'Siam', 'Rafi', 'Shawon']
print(friends.sort()) # None
print(friends) # ['Mir', 'Rafi', 'Shawon', 'Siam']
print(friends.reverse()) # None
print(friends) # ['Siam', 'Shawon', 'Rafi', 'Mir']
print(friends.clear()) # None
print(friends) # []

