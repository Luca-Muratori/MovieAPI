from boto import DynamoHelper

table_name = "my-table"
primary_key = "id"
attribute_name = "data"
attribute_type = "S"


#dfdfdf
helper = DynamoHelper(table_name)

# Create the table (if it doesn't exist)
try:
    helper.manage_creation("id", attribute_name, attribute_type)
except Exception as e:
    print("Table creation failed:", e)
# Update an item with primary key "123"
#helper.update_item("123", attribute_name, "updated data")
