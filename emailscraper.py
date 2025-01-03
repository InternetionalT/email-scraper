import requests
import re
import pyfiglet
import os

def print_colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def display_ascii_art():
    ascii_art = pyfiglet.figlet_format("Email Scraper", font="slant")
    colored_ascii_art = print_colored(ascii_art, 92)
    print(colored_ascii_art)

def fetch_html(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

def extract_emails(html_content):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return set(re.findall(email_pattern, html_content))

def save_emails(emails):
    filename = os.path.join(os.getcwd(), "scrapedemails.txt")
    try:
        with open(filename, "w") as file:
            for email in emails:
                file.write(email + "\n")
        print(f"Emails successfully saved to '{filename}'.")
    except PermissionError:
        print(f"Permission denied. Unable to write to '{filename}'.")
    except Exception as e:
        print(f"Error saving the file: {e}")

def main():
    os.system('title Email Scraper Tool, made by @puttyc2')
    display_ascii_art()

    url = input("Please enter the URL of the webpage to scrape emails from: ")

    print("\033[92mScraping is in progress...\033[0m")

    html_content = fetch_html(url)

    if html_content:
        print("\033[92mExtracting email addresses...\033[0m")
        emails = extract_emails(html_content)

        if emails:
            print(f"\033[92mFound {len(emails)} email(s).\033[0m")
            save_emails(emails)
        else:
            print("\033[91mNo email addresses found.\033[0m")

    print("\n\033[92mScraping completed! Press any key to exit.\033[0m")
    input()

if __name__ == "__main__":
    main()
