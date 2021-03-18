from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31')
soup = BeautifulSoup(url_get.content,"html.parser")

table = soup.find('div', attrs={'class':'lister-list'})
div = table.find_all('a')

movie_title = soup.find_all('div', class_ = 'lister-item mode-advanced')
movie_rating = soup.find_all('div', class_ = 'inline-block ratings-imdb-rating')
movie_votes = soup.find_all('div', class_ = 'inline-block ratings-imdb-rating')

names = [] #initiating a tuple
imdb_ratings = []
votes = [] 

for container in movie_title:
# If the movie has Metascore, then extract:
#     container.find('div', class_ = 'ratings-metascore') is not None:
# The name
        name = container.h3.a.text
        names.append(name)
# The IMDB rating
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)
# The number of votes
        vote = container.find('span', attrs = {'name':'nv'})['data-value']
        votes.append(int(vote))



#change into dataframe
df = pd.DataFrame({'title' : names, 'imdb_ratings' : imdb_ratings , 'votes' : votes})


@app.route("/")
def index(): 
	

	# generate plot
	ax = df.plot(figsize = (20,9))
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]


	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)
