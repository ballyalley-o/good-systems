import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

# FIXME: fiex this function

def csv_to_markdown(csv_file_path, md_file_path):
    """
    Convert CSV file to Markdown format and save it to the specified Markdown file.

    Args:
        csv_file_path (str): Path to the input CSV file.
        md_file_path (str): Path to save the output Markdown file.

    Returns:
        None
    """
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Convert DataFrame to markdown
    markdown_content = df.to_markdown(index=False)

    # Save markdown content to the specified file
    with open(md_file_path, 'w') as md_file:
        md_file.write(markdown_content)

if __name__ == "__main__":
    # Example usage with the provided paths
    csv_file_path = os.getenv('PATH_PROGRESS_CSV')
    md_file_path = os.getenv('PATH_SAMPLE_MD')

    csv_to_markdown(csv_file_path, md_file_path)
    print(f"CSV file at {csv_file_path} successfully converted to Markdown and saved at {md_file_path}.")


