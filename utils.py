import requests
import os


def fetch_input(year, day, session_cookie):
    """
    Fetches Advent of Code input for a specific year and day.

    Args:
        year (int): Year of the event (e.g., 2023).
        day (int): Day of the event (1-25).
        session_cookie (str): Your AoC session cookie.

    Returns:
        str: The puzzle input for the given day.
    """
    # URL for the input
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    # Headers with session cookie for authentication
    headers = {
        "Cookie": f"session={session_cookie}",
        "User-Agent": "Python AoC Fetcher"  # Optional but polite
    }

    # Fetch the input
    response = requests.get(url, headers=headers)

    # Check for errors
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch input: {response.status_code} - {response.reason}")


# Example Usage
if __name__ == "__main__":
    # Replace this with your actual session cookie
    session_cookie = os.getenv("SESSION_COOKIE")

    # Specify the year and day
    year = 2024
    day = 1

    try:
        puzzle_input = fetch_input(year, day, session_cookie)
        print(f"Puzzle Input for Day {day}:\n{puzzle_input}")
    except Exception as e:
        print(f"Error: {e}")