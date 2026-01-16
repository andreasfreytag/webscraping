from urllib.request import urlopen

url = "https://www.berkshirehathaway.com"

with urlopen(url) as response:
    html = response.read().decode("utf-8")

with open("Elnar/berkshire_extracted.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved: Elnar/berkshire_extracted.html")
