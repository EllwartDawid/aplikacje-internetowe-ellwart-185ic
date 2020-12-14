from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
from django.views import generic
from lxml import html

class HomePageView(generic.ListView):
    template_name = 'home.html'

def search(request):
    if request.method == "POST":
        website_link = request.POST.get('web_link', None)
        element = request.POST.get('element', None)
        url = website_link
        source=requests.get(url).text 
        all_elements = []
        
        soup = BeautifulSoup(source, "html.parser")

        # Wszystkie elementy
        items = soup.find_all(element)
        amount = len(items)     

        for i in items:
            # Szukanie klasy
            find_class = i.get('class')
            if find_class is None:
                find_class = "Nie ma"   

            # Szukanie id
            find_id = i.get('id')
            find_id = find_id.strip() if find_id is not None else "Nie ma"

            # Szukanie linków
            find_href = i.get('href')
            find_href = find_href.strip() if find_href is not None else "Nie ma"

            # Szukanie tekstu
            get_text = i.text
            get_text = get_text.strip() if get_text is not None else "Nie ma"

            find_src = i.get('src')            
            if find_src is None:
                find_src = "Nie ma"
            
            find_alt = i.get('alt')
            find_alt = find_alt.strip() if find_alt is not None else "Nie ma"


            all_elements.append({"find_id": find_id, "find_class": find_class, "find_href": find_href, "get_text": get_text, 'find_alt':find_alt, 'find_src': find_src})

        return render(request, 'scrapped.html', {'all_elements':all_elements, 'amount': amount, 'url': url, 'element':element})

    return render(request, 'scrapped.html')

def xml(request):

    # zad1 szukanie elementu przy pomocy xml 
    url = 'https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/'     
    path = '/html/body/div[1]/div[2]/div/div' 
    # odpowiedź na zapytanie   
    response = requests.get(url)             
    source = html.fromstring(response.content)    
    # element na stronie
    tree = source.xpath(path)
    # wybranie pierwszego elementu
    lxml1 = tree[0].text_content()
    
    # zad2 szukanie elementu przez nazwę klasy  
    url = 'https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/'    
    path = '//*[@class="wrapper"]' 
    response = requests.get(url)    
    data = response.content        
    source = html.fromstring(data)    
    tree = source.xpath(path)
    lxml2 = tree[0].text_content()

    return render(request, 'xpath.html', {'lxml1': lxml1,'lxml2': lxml2 })

def zad(request):   
    #przykład 1 
    page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, "html.parser")


    all_p_tags = []
    pierwszy = soup.select("p")[0].text
    drugi = soup.select("p")[2].text
    ilosc = len(soup.select("p"))
    
    #przykład 2 
    page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"  
    )
    soup = BeautifulSoup(page.content, "html.parser")  

    top_items = []

    products = soup.select("div.thumbnail")
    for elem in products:
        title = elem.select("h4 > a.title")[0].text
        review_label = elem.select("div.ratings")[0].text
        info = {"title": title.strip(), "review": review_label.strip()}
        top_items.append(info)

    #przykład 3 

    page = requests.get(
        "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"  
    )
    soup = BeautifulSoup(page.content, "html.parser")  

    image_data = []

    images = soup.select("img")
    for image in images:
        src = image.get("src")
        alt = image.get("alt")
        image_data.append({"src": src, "alt": alt})

    #przykład 4 

    all_products = []
    products = soup.select('div.thumbnail')
    for product in products:
        name = product.select('h4 > a')[0].text.strip()
        description = product.select('p.description')[0].text.strip()
        price = product.select('h4.price')[0].text.strip()
        reviews = product.select('div.ratings')[0].text.strip()
        image = product.select('img')[0].get('src')

        all_products.append({
            "name": name,
            "description": description,
            "price": price,
            "reviews": reviews,
            "image": image
        })


    return render(request,'home.html',{'pierwszy':pierwszy, 'drugi':drugi, 'ilosc':ilosc, 'top_items':top_items, 'image_data':image_data, 'all_products':all_products}) 