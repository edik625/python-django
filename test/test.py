import requests
import sys
from tabulate import tabulate

def main():
    book = input(f"Enter the book you are interested in: ")
    return_book = search_book(book)
    book_reponse(return_book)

    continues()

def book_reponse(book):
    if book:
        table = [[book[1], book[0], book[3], book[4], book[6]]]
        headers = ["Title", "Authors", "PageCount", "Categories", "Rating" ]
        print(tabulate(table, headers, tablefmt="simple"))
        print(f"\nDescription: {book[2]}\n\nMore information: {book[5]}\n")
    else:
        print("No data returned from the API.")

def search_book(title):
    url = f"https://www.googleapis.com/books/v1/volumes?q={title}&key=AIzaSyBkIS0OKTZc2R9urz15Dezgy5C2ud-HxNI"
    try:
        response = requests.get(url)
        data = response.json()
        if data["totalItems"] > 0 :
            return  (data["items"][0]["volumeInfo"]['authors'][0],data["items"][0]["volumeInfo"]["title"],
                     data["items"][0]["volumeInfo"]['description'],data["items"][0]["volumeInfo"]["pageCount"],
                     data["items"][0]["volumeInfo"]["categories"][0],
                     data["items"][0]["volumeInfo"]["canonicalVolumeLink"],
                     data["items"][0]["volumeInfo"]["averageRating"])
        else:
            print("There is no such book")
            continues()
    except KeyError:
        print("There is no such book")
        continues()

def continues():
    while True:
        yes_no = input("Interested in another book?(Y/N) ").upper()
        if yes_no == "N" or yes_no == "NO":
            print("Goodbay")
            sys.exit(1)
        elif yes_no == "Y" or yes_no == "YES":
            return main()
        else:
            print("Please, enter only yes/no")
            continue

if __name__ == "__main__" :
    main()