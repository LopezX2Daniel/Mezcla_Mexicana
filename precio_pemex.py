import requests
from bs4 import BeautifulSoup
    
url = "https://www.pemex.com/Paginas/default.aspx"
serveresponse = requests.get(url)
soup = BeautifulSoup(serveresponse.content, "html.parser")
divprecio = soup.findAll("div", {"class": "left precio-mezcla"})
divprecio = str(divprecio).replace('[<div class="left precio-mezcla">','')
divprecio = divprecio.replace("*</div>]","") + " USD"
