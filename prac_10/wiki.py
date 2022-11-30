"""CP1404 Practical 10
Wikipedia API & Python Library
Tahlia Clennar"""
import wikipedia

page_title = input("Enter page title or search phrase: ")
while page_title != "":
    try:
        details_abstracted = wikipedia.page(page_title, auto_suggest=False)
        print(f"Title: {details_abstracted.title}")
        print(f"Summary: {details_abstracted.summary}")
        print(f"URL: {details_abstracted.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
        page_title = input("Enter page title or search phrase: ")
