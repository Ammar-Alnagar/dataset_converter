from datasets import load_dataset
from huggingface_hub import login

# Load the dataset from Hugging Face.
# Replace 'your_dataset_name' with the actual dataset identifier.
dataset = load_dataset("your_dataset_name")

def transform_to_conversations(example):
    """
    Transforms an example with 'problem', 'solution', and 'answer' fields into a new field
    'conversations'. The assistant's message combines the 'solution' and 'answer' fields.
    """
    conversation = [
        {
            "from": "user",
            "value": example["problem"]
        },
        {
            "from": "assistant",
            "value": example["solution"] + "\n\n" + example["answer"]
        }
    ]
    example["conversations"] = conversation
    return example

# Apply the transformation to every example in the dataset.
transformed_dataset = dataset.map(transform_to_conversations)

# Optionally, remove the original 'problem', 'solution', and 'answer' columns.
transformed_dataset = transformed_dataset.remove_columns(["problem", "solution", "answer"])

# Log in to your Hugging Face account using your token.
login(token="YOUR_HUGGINGFACE_TOKEN")

# Push the transformed dataset to your Hugging Face account.
# Replace "username/my_transformed_dataset" with your desired repository name.
transformed_dataset.push_to_hub("username/my_transformed_dataset", token="YOUR_HUGGINGFACE_TOKEN")
