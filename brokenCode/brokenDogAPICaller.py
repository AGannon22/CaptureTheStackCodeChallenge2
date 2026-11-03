import requests
#API DOCS YOU SHOULD PROBABLY READ:
#https://breedhealthscore.com/developers/
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def getSpecificDog(slug):
    url = "" + slug + ".json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
def get_all_dog_data():
    breedLocation = ""
    base_url = "https://breedhealthscore.com/api" + breedLocation
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()
        return [breed["slug"] for breed in data["breeds"]]
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    allBreed_info = get_all_dog_data()
    print(allBreed_info)
    slugs = []
    for slug in slugs:
        getSpecificDog(slug)
