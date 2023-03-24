# Day 50: Wikipedia article loader (based on user input)

import wikipedia

def search_wikipedia():
    search_term = input("Enter a search term: ")
    try:
        page = wikipedia.page(search_term)
        print(page.summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print("There are multiple results for this search term. Please be more specific.")
        print(e.options)

if __name__ == "__main__":
    search_wikipedia()
