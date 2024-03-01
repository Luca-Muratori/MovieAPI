import boto3

class DynamoHelper:

    def __init__(self, table_name, region_name="eu-central-1"):
        self.dynamodb = boto3.resource('dynamodb', region_name=region_name)
        self.table = self.dynamodb.Table(table_name)

    def manage_creation(self, primary_key, attribute_name, attribute_type):
        """
        Creates a DynamoDB table with a primary key and an attribute.

        Args:
            primary_key (str): The name of the primary key attribute.
            attribute_name (str): The name of the additional attribute.
            attribute_type (str): The data type of the additional attribute (e.g., "S", "N", "B").
        """

        key_schema = [
            {
                'AttributeName': primary_key,
                'KeyType': 'HASH'
            }
        ]

        attribute_definitions = [
            {
                'AttributeName': primary_key,
                'AttributeType': 'S'
            },
            {
                'AttributeName': attribute_name,
                'AttributeType': attribute_type
            }
        ]

        self.table.create_table(
            TableName=self.table.table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

    def update_item(self, primary_key_value, attribute_name, attribute_value):
        """
        Updates an item in the DynamoDB table.

        Args:
            primary_key_value (str): The value of the primary key for the item to update.
            attribute_name (str): The name of the attribute to update.
            attribute_value (str): The new value for the attribute.
        """

        update_expression = "SET {} = :{}".format(attribute_name, attribute_name)
        expression_attribute_values = {
            ":{}".format(attribute_name): attribute_value
        }

        self.table.update_item(
            Key={
                primary_key: primary_key_value
            },
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )


