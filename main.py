import requests

# actors id 1 - 49979

FILM_LIST_PATH = "http://api.themoviedb.org/3/discover/movie"
CREDITS_LIST_PATH = "http://api.themoviedb.org/3/movie"
GET_ACTOR = "https://api.themoviedb.org/3/person"
RELEASE_DATE = "2014-01-01"
BACON_ID = "4724"
PAUL_ID = "781"
WHALB_ID = "13240"

API_KEY = "6682969b2b2104c72d74e04f54de032b"


def get_actor_details(actor_id):
    url = f"{GET_ACTOR}/{actor_id}?"
    params = {"api_key": API_KEY}
    r = requests.get(url=url, params=params)
    data = r.json()
    return data


def get_film_list(actor_id):
    params = {"api_key": API_KEY, "with_people": actor_id, "primary_release_date.gte": RELEASE_DATE}
    r = requests.get(url=FILM_LIST_PATH, params=params)
    data = r.json()
    return data


def data_to_set(data):
    film_set = set()
    for res in data["results"]:
        film_set.add(res["title"])
    return film_set


def main():
    print("====================Welcome====================")

    actor_1 = input("Kindly enter the id of the first actor: ")
    actor_2 = input("Kindly enter the id of the second actor: ")

    actor_1_details = get_actor_details(actor_1)
    actor_2_details = get_actor_details(actor_2)

    actor_1_name = actor_1_details['name']
    actor_2_name = actor_2_details['name']

    actor_1_data = get_film_list(actor_1)
    actor_1_films = data_to_set(actor_1_data)
    actor_2_data = get_film_list(actor_2)
    actor_2_films = data_to_set(actor_2_data)

    actor_1_films_set = set(actor_1_films)
    actor_2_films_set = set(actor_2_films)

    print(f"These are the list of {actor_1_name} films: {list(actor_1_films_set)}")
    print(f"These are the list of {actor_2_name} films: {list(actor_2_films_set)}")

    two_actors_inter = actor_1_films_set.intersection(actor_2_films_set)

    if two_actors_inter:
        print(f"Both actors have this films in common: {list(two_actors_inter)}")
    else:
        print("The two actors have no films in common")


if __name__ == "__main__":
    main()
