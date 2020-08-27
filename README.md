# Amazon.ca PC Part Price Tracker

## Description

This is a python utility that can track the price of PC parts

## Installation

You will need to have a few components installed (on a Mac) before starting to use this project

- [Brew Package Manager](https://brew.sh)
- [Python 3](https://docs.python-guide.org/starting/install3/osx/)
- You will need to install `pip3` to get python packages
- `pip3 install virtualenv`

Once you have these prerequisites, you can build the project and run the web scraper.

```bash
# To activate environment
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

# To deactivate environment
deactivate
```

## Usage

## Grabbing Data

```bash
scrapy shell '<some-website-url>' --nolog

# In a browser, inspect an element. In the html inspector, right-click and
# copy Xpath. Play around with it until you see a response with the
# following scrapy command. The response is the html paged scraped.
>>> response.xpath('some-xpath').extract()
```


## Acknowledgment

- [Scrape an ecommerce dataset with Scrapy, step-by-step](https://medium.com/@tobritton/scrape-an-ecommerce-dataset-with-scrapy-from-start-to-finish-b31540df9bfa)
