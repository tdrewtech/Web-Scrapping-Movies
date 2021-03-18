# Web-Scrapping using Beautifulsoup

This project is about simple webscrapping from imdb.com to obtain information. I also use a simple dashboard flask to display our scrap and visualization results.

## Dependencies

- beautifulSoup4
- Pandas
- flask
- matplotlib

Install the requirements.txt in the following way :

`` python
pip install -r requirements.txt
``


## Steps of my Web Scrapping

* I scrape using `beautiful soup` in my jupyter notebook first.
* Please open the notebook template in this capstone and fill in according to the directions. I have also provided the analysis needed on the notebook.
* The file in this repository is a file that can be used to create a simple dashboard flask.

`` python
table = soup.find('table', attrs={'class':'table table-striped table-hover table-hover-solid-row table-simple history-data'})
tr = table.find_all('tr')
``

* Use the code below to save the scrap that you made into a dataframe.

`` python
df = pd.DataFrame({'title' : names, 'imdb_ratings' : imdb_ratings , 'votes' : votes})``


* You can also play with the UI in `index.html` where you can follow the comments to find out which parts can be changed.

### Objectives

Data for films released in 2019 from `imdb.com/search/title/? Release_date = 2019-01-01,2019-12-31`

     * From this page, look for `title`,` imdb rating`, and` votes`
     * Make plots from the 10 most popular films of 2019.
