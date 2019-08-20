from bs4 import BeautifulSoup
import requests
import pandas as pd
from google_images_download import google_images_download

response = requests.get('https://www.ft.com/content/3a3419f4-78b1-11e9-be7d-6d846537acab')
soup = BeautifulSoup(response.text, 'lxml')

name = soup.find_all('tr')
company_name = []
company_type = []

for i in name[1:]:
    i = i.find_all('td')
    company_name.append(i[3].get_text())
    company_type.append(i[4].get_text())


data = pd.DataFrame()
data['Company Name'] = company_name
data['Company Type'] = company_type
data.sort_values(by=['Company Name'] , inplace=True)
data.to_csv('Companies data.csv', index=False)


response = google_images_download.googleimagesdownload()
for i in company_name:
    arguments = {"keywords": i + "company logo", "limit": "5", "size": "medium", "aspect_ratio": "panoramic"}
    response.download(arguments)