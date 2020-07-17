from googlesearch import search
query="python tutorial"

for i in search(query,tld="co.in",num=10,stop=10,pause=2):
    print(i)


#query : query string that we want to search for.
#tld : tild standfor top level domain whichmeans we want to search our result on googl.in
#num :  of results we eant
#stop : Last result to retrieve.Use Noneto keepsearching forever.
#pause :Lapse to wait between Http requests.