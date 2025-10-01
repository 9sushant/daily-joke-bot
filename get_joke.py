import requests
import re

# URL for the dad joke API
API_URL = "https://icanhazdadjoke.com/"
# Path to your README file
README_PATH = "README.md"

def get_random_joke():
    """Fetches a random joke from the API."""
    try:
        response = requests.get(API_URL, headers={"Accept": "text/plain"})
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")
        return None

def update_readme(joke):
    """Updates the README file with the new joke."""
    with open(README_PATH, "r") as f:
        content = f.read()

    # Use regex to find and replace the content between the markers
    new_content = re.sub(
        r"(?<=\n> \*\*).*(?=\*\*)",
        joke,
        content,
        flags=re.DOTALL
    )

    with open(README_PATH, "w") as f:
        f.write(new_content)
    print("README updated successfully!")

if __name__ == "__main__":
    new_joke = get_random_joke()
    if new_joke:
        update_readme(new_joke)
