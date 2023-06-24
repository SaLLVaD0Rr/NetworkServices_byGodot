import requests

def check_website_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The website {url} is online.")
        else:
            print(f"The website {url} is offline. Status code: {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"An error occurred while trying to access the website {url}.")

def main():
    url = input("Enter the URL of the website you want to check: ")
    check_website_status(url)

if __name__ == "__main__":
    main()
