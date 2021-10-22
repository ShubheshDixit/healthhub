import wikipedia

while(True):

    print("Enter your search :- ", end="")
    search = input("")

    #print(wikipedia.summary(search, sentences=2))
    page = wikipedia.page(search)
    pagecontent =page.content
    pageurl = page.url

    print(pagecontent)
    print(pageurl)
    
   