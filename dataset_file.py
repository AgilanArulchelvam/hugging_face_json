from datasets import load_dataset, Dataset
from huggingface_hub import HfApi

def upload_to_huggingface(dataset_file, repo_id, token):
    # Load the JSON file into a Hugging Face dataset
    dataset = Dataset.from_json(dataset_file)

    # Push dataset to Hugging Face Hub
    dataset.push_to_hub(repo_id, token=token)

    print(f"Dataset successfully uploaded to https://huggingface.co/datasets/{repo_id}")

# Example usage
dataset_file = ""  # Replace with your JSON file
repo_id = ""       # Replace with your Hugging Face dataset repo
token = ""           # Replace with your HF token

upload_to_huggingface(dataset_file, repo_id, token)
