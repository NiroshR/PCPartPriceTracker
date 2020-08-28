# Amazon.ca PC Part Price Tracker

## Description

This is a python utility that can track the price of PC parts.

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

To use this scraping tool, create a spider with the specific Amazon link to scrape. For example, `rtx2070.py` scrapes Amazon for a NVIDIA graphics card. With the command `scrape.sh run`, as described below, you can scrape a site and keep a history of it in the `history/` folder. Files here aren't ignored by git so you can make a branch and save all the history online. When you run the `scrape.sh` script, it combines the historical data and the current data into one so you can view it in Excel with cool graphs.

You need to add the `name` attribute of your scraper to the `targets` array in the `scrape.sh` script. These NEED to be unique, otherwise it won't work.

```bash
cd tracker
./scrape.sh <option>
```

```bash
This script will be used to help clean and run the spiders. 
It can also help to create compressed log files  

Syntax: ./scrape.sh [ env | clean | run | rebuild ] 
 options: 
 env           Outlines how to setup environment. 
 clean         Cleans output directories and all python caches in repo. 
 run           Runs spiders on all specified targets. 
 rebuild       Cleans directories and runs spiders on all specified targets. 
```

## Alerts
### macOS Only
The `combine.py` script will notify the user when the price drops by 10% of its first scraped price. Same thing will happen if the price rises by over 5%.

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

## Author

Nirosh Ratnarajah. Literally just me... and StackOverflow.
