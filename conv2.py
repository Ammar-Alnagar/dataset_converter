from datasets import load_dataset
from huggingface_hub import login

# Load the dataset from Hugging Face.
dataset = load_dataset("your_dataset_name")

def transform_to_conversations(example):
    """
    Transforms an example with 'problem' and 'answer' fields into a new field
    'conversations', which is a list of two dictionaries.
    """
    conversation = [
        {
            "from": "user",
            "value": example["problem"]
        },
        {
            "from": "assistant",
            "value": example["answer"]
        }
    ]
    example["conversations"] = conversation
    return example

# Apply the transformation to every example in the dataset.
transformed_dataset = dataset.map(transform_to_conversations)

# Optionally, remove the original 'problem' and 'answer' columns.
transformed_dataset = transformed_dataset.remove_columns(["problem", "answer"])

# Log in to your Hugging Face account using your token.
login(token="YOUR_HUGGINGFACE_TOKEN")

# Push the transformed dataset to your Hugging Face account.
# Replace "username/my_transformed_dataset" with your desired repository name.
transformed_dataset.push_to_hub("username/my_transformed_dataset", token="YOUR_HUGGINGFACE_TOKEN")
