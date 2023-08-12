from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import random
app = Flask(__name__)
# Send a GET request to the website

def get(url):
    response = requests.get(f'https://uhdmovies.ink/{url}')

    # Get the HTML content from the response
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract the image URL
    whole = soup.find('article', class_='gridlove-box')
    return whole
def find(url):
    response = requests.get(f'https://uhdmovies.ink/{url}')


    # Get the HTML content from the response
    html_content = response.text
    try:


        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the title
        title = soup.find('h2').get_text()

        # Extract the image URL
        img_tag = soup.find('img', class_='aligncenter')
        image_url = img_tag['src']

        # Extract the image URL
        long_title = soup.find('h1', class_='entry-title')
        long_title = long_title.get_text() 

        # Extract the main description
        main_description = soup.find('div', class_='entry-content').find('p').get_text()

        # Extract the download links, their corresponding texts, and the preceding text
        download_links = []
        download_texts = []
        preceding_texts = []
        download_elements = soup.find_all('a', class_='maxbutton-1 maxbutton maxbutton-download-g-drive')
        for link in download_elements:
            download_links.append(link['href'])
            download_texts.append(link.get_text())
            # Extract the additional text next to the download link (if available)
            additional_text = link.find_next_sibling("span")
            if additional_text:
                download_texts.append(additional_text.get_text())
            # Extract the preceding text for the download link
            parent_p = link.find_parent('p')
            preceding_text = parent_p.find_previous_sibling("p")
            if preceding_text:
                preceding_texts.append(preceding_text.get_text())

        # Extract the description after the download buttons
        description_after_buttons = soup.find_all('p', style='text-align: center;')[2].get_text()

        return {
            "Title": title,
            "Image URL": image_url,
            "Main Description": main_description,
            "Download Links": download_links,
            "Download Texts": download_texts,
            "Preceding Texts": preceding_texts,
            "Description After Buttons": description_after_buttons,
            "long_title": long_title
        }
    except:
        try:
            # Create a Beautiful Soup object to parse the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract the title
            title = soup.find('h2').get_text()

            # Extract the image URL
            img_tag = soup.find('img', class_='aligncenter')
            image_url = img_tag['src']

            #long title
            long_title = soup.find('h1', class_='entry-title')
            long_title = long_title.get_text() 

            # Extract the main description
            main_description = soup.find('div', class_='entry-content').find('p').get_text()

            # Extract the download links, their corresponding texts, and the preceding text
            download_links = []
            download_texts = []
            preceding_texts = []
            download_elements = soup.find_all('a', class_='maxbutton-1 maxbutton maxbutton-gdrive-episode')
            for link in download_elements:
                download_links.append(link['href'])
                download_texts.append(link.find('span', class_='mb-text').get_text())
                # Extract the preceding text for the download link
                parent_p = link.find_parent('p')
                preceding_text = parent_p.find_previous_sibling("p")
                if preceding_text:
                    preceding_texts.append(preceding_text.get_text())

            # Extract the description after the download buttons
            description_after_buttons = soup.find_all('p', style='text-align: center;')[-2].get_text()

            return {
                "Title": title,
                "Image URL": image_url,
                "Main Description": main_description,
                "Download Links": download_links,
                "Download Texts": download_texts,
                "Preceding Texts": preceding_texts,
                "Description After Buttons": description_after_buttons,
                "long_title": long_title
            }

        except:
            return 'none'

def hi():
    response = requests.get('https://uhdmovies.ink/')

    # Get the HTML content from the response
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find all the page number elements
    page_numbers = soup.find_all('a', class_='page-numbers')

    # Extract page numbers as integers
    page_numbers = [int(page.get_text()) for page in page_numbers if page.get_text().isdigit()]

    # Find the highest page number
    highest_page_number = max(page_numbers)
    return highest_page_number
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.route('/1')
def one():
    response = requests.get('https://uhdmovies.ink/')

    # Get the HTML content from the response
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find all the page number elements
    page_numbers = soup.find_all('a', class_='page-numbers')

    # Extract page numbers as integers
    page_numbers = [int(page.get_text()) for page in page_numbers if page.get_text().isdigit()]

    # Find the highest page number
    highest_page_number = max(page_numbers)
    # Find all the article elements
    article_elements = soup.find_all('article', class_='gridlove-post')
    # Loop through each article and extract information

    raw = ''
    links = []
    div_elements = soup.find_all('div', class_='box-inner-p')
    for div in div_elements:
        a_tag = div.find('a')
        link = a_tag['href']
        links.append(link)
    for article in article_elements or link in links:
        # Extract the title text
        title_element = article.find('h1', class_='sanket')
        title_text = title_element.get_text(strip=True) if title_element else "Title not found"

        # Extract the link
        link_element = article.find('a', title=title_text)
        link_url = link_element['href'] if link_element else "Link not found"
        # link_url = link
        link_url = link_url.replace('https://uhdmovies.ink', '')
        link_url = link_url.rstrip('/')
        # Extract the thumbnail URL
        thumbnail_element = article.find('img', class_='attachment-gridlove-a3-orig')
        thumbnail_url = thumbnail_element['src'] if thumbnail_element else "Thumbnail not found"

        # Print the extracted information for each article
        # print("Title:", title_text)
        # print("Link:", link_url)
        # print("Thumbnail URL:", thumbnail_url)
        # print("-" * 40)  # Separating each article's information

        raw = f""" {raw}

    <div class="col-md-3 col-6" onclick="window.location = '/movies{link_url}'">
            <div class="trend_2im clearfix position-relative">
            <div class="trend_2im1 clearfix">
                <div class="grid">
            <figure class="effect-jazz mb-0">
                <a href="/movies{link_url}"><img src="{thumbnail_url}" class="w-100" alt="img25"></a>
            </figure>
        </div>
            </div>
            
            </div>
            <div class="trend_2ilast bg_grey p-3 clearfix">
                <h5><a class="col_red" href="/movies{link_url}">Semper</a></h5>
                <p class="mb-2">{title_text}</p>
                <span class="col_red">
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            </span>
            <p class="mb-0">1 Views</p>
            </div>  
            </div>
        """

    return raw
@app.route('/hd-m')
def hdm():
    response = requests.get('https://uhdmovies.ink/1080p-10bit/')

    # Get the HTML content from the response
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the article elements
    article_elements = soup.find_all('article', class_='gridlove-post')
    # Loop through each article and extract information

    raw = ''
    for article in article_elements:
        # Extract the title text
        title_element = article.find('h1', class_='sanket')
        title_text = title_element.get_text(strip=True) if title_element else "Title not found"

        # Extract the link
        link_element = article.find('a', title=title_text)
        link_url = link_element['href'] if link_element else "Link not found"
        link_url = link_url.replace('https://uhdmovies.ink', '')
        link_url = link_url.rstrip('/')
        

        # Extract the thumbnail URL
        thumbnail_element = article.find('img', class_='attachment-gridlove-a3-orig')
        thumbnail_url = thumbnail_element['src'] if thumbnail_element else "Thumbnail not found"

        # Print the extracted information for each article
        # print("Title:", title_text)
        # print("Link:", link_url)
        # print("Thumbnail URL:", thumbnail_url)
        # print("-" * 40)  # Separating each article's information

        raw = f""" {raw}
    <div class="col-md-3 col-6" onclick="window.location = '/movies/{link_url}'">
            <div class="trend_2im clearfix position-relative">
            <div class="trend_2im1 clearfix">
                <div class="grid">
            <figure class="effect-jazz mb-0">
                <a href="/movies/{link_url}"><img src="{thumbnail_url}" class="w-100" alt="img25"></a>
            </figure>
        </div>
            </div>
            
            </div>
            <div class="trend_2ilast bg_grey p-3 clearfix">
                <h5><a class="col_red" href="/movies/{link_url}">Semper</a></h5>
                <p class="mb-2">{title_text}</p>
                <span class="col_red">
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            </span>
            <p class="mb-0">1 Views</p>
            </div>  
            </div>
        """

    return raw
@app.route('/4k-m')
def km4():
    response = requests.get('https://uhdmovies.ink/4k-hdr/')

    # Get the HTML content from the response
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the article elements
    article_elements = soup.find_all('article', class_='gridlove-post')
    # Loop through each article and extract information

    raw = ''

    links = []
    div_elements = soup.find_all('div', class_='box-inner-p')
    for div in div_elements:
        a_tag = div.find('a')
        link = a_tag['href']
        links.append(link)
    for article in article_elements or link in links:
        # Extract the title text
        title_element = article.find('h1', class_='sanket')
        title_text = title_element.get_text(strip=True) if title_element else "Title not found"
 
        link = link_url
        # link_element = article.find('a', title=title_text)
        # link_url = link_element['href'] if link_element else "Link not found"
        link_url = link_url.replace('https://uhdmovies.ink', '')
        link_url = link_url.rstrip('/')
        

        # Extract the thumbnail URL
        thumbnail_element = article.find('img', class_='attachment-gridlove-a3-orig')
        thumbnail_url = thumbnail_element['src'] if thumbnail_element else "Thumbnail not found"

        # Print the extracted information for each article
        # print("Title:", title_text)
        # print("Link:", link_url)
        # print("Thumbnail URL:", thumbnail_url)
        # print("-" * 40)  # Separating each article's information

        raw = f""" {raw}
    <div class="col-md-3 col-6" onclick="window.location = '/movies/{link_url}'">
            <div class="trend_2im clearfix position-relative">
            <div class="trend_2im1 clearfix">
                <div class="grid">
            <figure class="effect-jazz mb-0">
                <a href="/movies/{link_url}"><img src="{thumbnail_url}" class="w-100" alt="img25"></a>
            </figure>
        </div>
            </div>
            
            </div>
            <div class="trend_2ilast bg_grey p-3 clearfix">
                <h5><a class="col_red" href="/movies/{link_url}">Semper</a></h5>
                <p class="mb-2">{title_text}</p>
                <span class="col_red">
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            </span>
            <p class="mb-0">1 Views</p>
            </div>  
            </div>
        """

    return raw
@app.route('/eng-m')
def engm():
    response = requests.get('https://uhdmovies.ink/movies/english-movies/')

    # Get the HTML content from the response
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the article elements
    article_elements = soup.find_all('article', class_='gridlove-post')
    # Loop through each article and extract information

    raw = ''
    for article in article_elements:
        # Extract the title text
        title_element = article.find('h1', class_='sanket')
        title_text = title_element.get_text(strip=True) if title_element else "Title not found"

        # Extract the link
        link_element = article.find('a', title=title_text)
        link_url = link_element['href'] if link_element else "Link not found"
        link_url = link_url.replace('https://uhdmovies.ink', '')
        link_url = link_url.rstrip('/')
        

        # Extract the thumbnail URL
        thumbnail_element = article.find('img', class_='attachment-gridlove-a3-orig')
        thumbnail_url = thumbnail_element['src'] if thumbnail_element else "Thumbnail not found"

        # Print the extracted information for each article
        # print("Title:", title_text)
        # print("Link:", link_url)
        # print("Thumbnail URL:", thumbnail_url)
        # print("-" * 40)  # Separating each article's information

        raw = f""" {raw}
    <div class="col-md-3 col-6" onclick="window.location = '/movies/{link_url}'">
            <div class="trend_2im clearfix position-relative">
            <div class="trend_2im1 clearfix">
                <div class="grid">
            <figure class="effect-jazz mb-0">
                <a href="/movies/{link_url}"><img src="{thumbnail_url}" class="w-100" alt="img25"></a>
            </figure>
        </div>
            </div>
            
            </div>
            <div class="trend_2ilast bg_grey p-3 clearfix">
                <h5><a class="col_red" href="/movies/{link_url}">Semper</a></h5>
                <p class="mb-2">{title_text}</p>
                <span class="col_red">
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            </span>
            <p class="mb-0">1 Views</p>
            </div>  
            </div>
        """

    return raw
@app.route('/')
def index():
    num = hi()
    return render_template('index.html', num = num, page='',status1 = 'disabled', next1 = '/page/2')
@app.route('/1080p-10bit')
def hd():
    return render_template('hd.html')
@app.route('/4k-HDR')
def hdk():
    return render_template('4k.html')
@app.route('/english-movies')
def eng():
    return render_template('eng.html')

@app.route('/page/<no>/')
def no(no):
    num = hi()
    pre = int(no) - 1
    next1 = int(no) + 1
    if next1 == no:
        next1 = int(no)
    return render_template('index.html',num = num, page = no, pre = f'/page/{pre}',next1 = f'/page/{next1}')
@app.route('/ft/<no>/')
def ft(no):
    response = requests.get(f'https://uhdmovies.ink/page/{no}/')
    # Get the HTML content from the response
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the article elements
    article_elements = soup.find_all('article', class_='gridlove-post')
    # Loop through each article and extract information

    raw = ''
    for article in article_elements:
        # Extract the title text
        title_element = article.find('h1', class_='sanket')
        title_text = title_element.get_text(strip=True) if title_element else "Title not found"

        # Extract the link
        link_element = article.find('a', title=title_text)
        link_url = link_element['href'] if link_element else "Link not found"
        link_url = link_url.replace('https://uhdmovies.ink', '')
        link_url = link_url.rstrip('/')
        

        # Extract the thumbnail URL
        thumbnail_element = article.find('img', class_='attachment-gridlove-a3-orig')
        thumbnail_url = thumbnail_element['src'] if thumbnail_element else "Thumbnail not found"

        # Print the extracted information for each article
        # print("Title:", title_text)
        # print("Link:", link_url)
        # print("Thumbnail URL:", thumbnail_url)
        # print("-" * 40)  # Separating each article's information

        raw = f""" {raw}
    <div class="col-md-3 col-6" onclick="window.location = '/movies/{link_url}'">
            <div class="trend_2im clearfix position-relative">
            <div class="trend_2im1 clearfix">
                <div class="grid">
            <figure class="effect-jazz mb-0">
                <a href="/movies/{link_url}"><img src="{thumbnail_url}" class="w-100" alt="img25"></a>
            </figure>
        </div>
            </div>
            
            </div>
            <div class="trend_2ilast bg_grey p-3 clearfix">
                <h5><a class="col_red" href="/movies/{link_url}">Semper</a></h5>
                <p class="mb-2">{title_text}</p>
                <span class="col_red">
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            <i class="fa fa-star"></i>
            </span>
            <p class="mb-0">1 Views</p>
            </div>  
            </div>
        """

    return raw

# @app.route('/m/<mo>')
@app.route('/movies/<mo>')
def movie(mo):

    # da = find(mo)
    # if da != 'none':
    #     title = da['Title']
    #     thumb = da['Image URL']
    #     description = da['Main Description']
    #     download_links = da['Download Links']
    #     btn_text = da['Download Texts']
    #     link_desc = da['Preceding Texts']
    #     long_title = da['long_title']
    #     btn = ''
    #     m = ['asdf','sadf']
    #     # return link_desc
    #     for i in range(len(btn_text)):
    #         btn= f'''{btn}
    #         <p style="color: white; font-size: 20px;font-weight: bold;">{link_desc[i]}</p>
    #         <a href = "{download_links[i]}" target="_blank"><button class="btn btn-primary" style="width: 5cm;">{btn_text[i]}</button><a>
    #         <br>
    #         <br>

    #         '''
    #     # return f"{title}<br><br> {da}"
    #     return render_template('movies.html',thumb = thumb,title = title,long_title = long_title,description=description, btn = btn)

    tmt = get(mo)
    if tmt != 'none':
        return render_template('mov2.html', tmt = tmt)
    return render_template('404.html'), 404
    # return render_template('movies.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
