import pandas as pd
from pymongo import MongoClient

# MongoDB connection details
MONGO_URI="mongodb+srv://sushantrajbhar:D3clare!@cluster0.l6tpy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_NAME = "APS"
COLLECTION_NAME = "mongoclass"

def download_data_from_mongodb():
    # Create a MongoDB client
    client = MongoClient(MONGO_URI)

    # Access the database
    db = client[DATABASE_NAME]

    # Access the collection
    collection = db[COLLECTION_NAME]

    # Fetch all documents from the collection
    documents = list(collection.find())

    # Check if there are any documents
    if not documents:
        print("No documents found in the collection.")
        return

    # Convert documents to a DataFrame
    df = pd.DataFrame(documents)

    # Remove the default MongoDB '_id' field if necessary
    if '_id' in df.columns:
        df.drop(columns=['_id'], inplace=True)

    # Save DataFrame to CSV
    csv_file_path = "data_downloaded.csv"
    df.to_csv(csv_file_path, index=False)
    
    print(f"Data downloaded and saved to {csv_file_path}")

# Run the function to download data
if __name__ == "__main__":
    download_data_from_mongodb()
