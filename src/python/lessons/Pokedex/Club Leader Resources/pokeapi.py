import io
import urllib.request
from urllib.request import urlopen
from PIL import Image, ImageTk

#function to get the data for a pokemon
def getPokemonData(num):
    data = urllib.request.urlopen("http://pokeapi.co/api/v1/pokemon/"+str(num)).read()
    pokemonDict = eval(data)
    return pokemonDict

#function to get the image for a pokemon
def getPokemonImage(num):
    data = urllib.request.urlopen("http://pokeapi.co/api/v1/sprite/"+str(num)).read()
    spriteDict = eval(data)
    imgURL = "http://pokeapi.co" + spriteDict["image"]
    image_bytes = urlopen(imgURL).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    tk_image = ImageTk.PhotoImage(pil_image)
    return tk_image
