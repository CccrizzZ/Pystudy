import random
import urllib

def download_web_img(url):
    # Generates random number for downloaded file
    name = random.randrange(1,1000)
    # Set the name of the file to .jpg
    full_name = str(name) + ".jpg"
    # Downloading image
    # Change path by changing the second parameter
    urllib.urlretrieve(url, "./Python/" + full_name)

download_web_img("https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2749386478,3983218336&fm=26&gp=0.jpg")
