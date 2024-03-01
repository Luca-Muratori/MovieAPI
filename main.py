from boto import DynamoDBHelper

import random

generated_numbers = set()  # Use a set to efficiently track generated numbers

while len(generated_numbers) < 900:  # Generate 900 unique numbers (all possible 3-digit ones)
   number = random.randint(100, 999)  # Generate a random 3-digit number
   generated_numbers.add(number)

# After the loop, all possible 3-digit numbers will be in the set; fetch one randomly
random_id = random.choice(list(generated_numbers))

table_name = "Movies"
primary_key = "id"

element_title = "The Dark Knight"
element_release=2008
element_genre="Action, Drama, Crime"
element_cover="https://upload.wikimedia.org/wikipedia/en/1/1c/The_Dark_Knight_%282008_film%29.jpg"

helper = DynamoDBHelper(table_name=table_name)
# Create the table (if it doesn't exist)
#helper.manage_create_table(primary_key)
#create an item
helper.create_item(str(random_id), element_title, element_release, element_genre, element_cover)

# Update an item with primary key "123"
#helper.update_item("123", attribute_name, "updated data")
print("Table created!")
