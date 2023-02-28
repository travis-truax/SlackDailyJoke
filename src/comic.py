import requests
from datetime import datetime
from bs4 import BeautifulSoup
import pytz


GO_COMICS_URL = "https://www.gocomics.com"
XKCD_URL = "https://xkcd.com/info.0.json"

def get_xkcd():
    xkcd_response = requests.get(url=XKCD_URL)
    data = xkcd_response.json()
    return f"Comic Number: {str(data['num'])}\nTitle: {data['title']}\nAlt Text: {data['alt']}\n{data['img']}"



def get_go_comic(comic):
    endpoint = comic
    date = datetime.now(tz=pytz.timezone('US/Pacific')).strftime("%Y/%m/%d")

    req_url = f"{GO_COMICS_URL}/{endpoint}/{date}"
    r = requests.get(url=req_url)
    comic_html = BeautifulSoup(r.content, "html.parser")
    comic_img = comic_html.find("div", {"class": "comic__image"})
    return (
        comic_img.find("picture", {"class": "item-comic-image"})
        .find("img")["data-srcset"]
        .split(" ")
        .pop(0)
    )

def get(comic_name):
    if comic_name == "xkcd":
        return get_xkcd()
    elif comic_name == "calvinandhobbes":
        return get_go_comic(comic_name)
