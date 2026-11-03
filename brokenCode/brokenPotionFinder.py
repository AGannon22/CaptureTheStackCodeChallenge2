import requests
#I want the FIRST NAME of the woman who helped invent the potion with an ID of f45278ef-1338-4ff0-b22a-e9813f33b64f
#API DOCS
#https://docs.potterdb.com/apis/rest
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def potionGrabber():
    url = ""
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    thePotion = potionGrabber()
    print(thePotion)
