# UdemyProjectExercise2-glassesShop

This is a Udemy tutorial to learn Scrapy. Modern Web Scraping with Python using Scrapy Splash Selenium

Link to scrapy: http://www.glassesshop.com/bestsellers/

# Scrapy command:
- run scrapy script -----> scrapy crawl products

- run scrapy shell ------> scrapy shell

- Create New Scrpay Project -------> scrapy startproject glassesShop

- You can start your first spider with: 
      - cd glassesShop 
      - scrapy genspider example example.com

- Create Scrapy spider -------> scrapy genspider products http://www.glassesshop.com/bestsellers/

- Export Excel Command -----> scrapy crawl products -o products_dataset.csv

# Anaconda command:
- install dependencies ----> conda install -c conda-forge scrapy==1.6 pylint autopep8 -y
- install iPython ---------> conda install iPython
