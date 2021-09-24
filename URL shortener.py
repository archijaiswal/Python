#8e49668ea2fac42e2214eb6799cddcb313fa71cf
from pyshorteners import Shortener

API_KEY='8e49668ea2fac42e2214eb6799cddcb313fa71cf'

obj = Shortener(api_key = API_KEY)

long_url="https://www.google.com/search?q=wallpaper&tbm=isch&hl=en&chips=q:wallpaper,g_1:galaxy:gHxkaGWDx2M%3D&sa=X&ved=2ahUKEwi9i-bFoZDzAhVC0nMBHV4gDXoQ4lYoBnoECAEQHA&biw=771&bih=661#imgrc=yIGiED8WIxN3lM"

short_url= obj.bitly.short(long_url)

print(short_url)

Long_url = obj.bitly.expand(short_url)

# print(Long_url)