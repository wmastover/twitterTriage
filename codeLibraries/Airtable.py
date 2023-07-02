from airtable import Airtable

def uploadToAirtable(item):
    # Set up your Airtable credentials and base information
    base_key = 'appQXMiEjCRk6LPRr'
    table_name = 'tblogpIX9pxk7Ogn7'
    api_key = 

    # Initialize the Airtable object
    airtable = Airtable(base_key, table_name, api_key)

    # Iterate over each JSON object and upload it to Airtable
    airtable.insert(item)  # Insert the item into the table

    print("Outreach Item Uploaded")

    


