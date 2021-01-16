# web-scrap-project

## Project Description

This is a scrapping application that scraps various websites for data related to the Mission to Mars and display the information in a single HTML page. The screen shot of the application is shown in the "sample" figure. 

* All the project files are contained in this repo.


### Sample Webpage Screenshot


![images](images/sample.jpg "Screenshot")


## Instructions

### Steps


By running the app.py file, you will enter the web page "Mission to Mars" where there is a  "Scrape New Data" button. By clicking the button, the application will scrape the information from various related webpage for you and display the information in the web page.

1. Make sure that all these Python libraries are installed
 - flask
 - flask_pymongo
 - time
 - bs4
 - splinter
 - pandas
2. Download all the files from the repository
3. Run the `Missions_to_Mars\app.py` file
4. Open Google Chrome and visit the URL: `http://127.0.0.1:5000/` and click the "Scrape New Data" button
the application will scrape the information from various related webpage for you and display the information in the web page.



## File Description

### 1. `images`

* `sample.jpg`
It is the screenshot of final webpage with scraped data

### 2. `Missions_to_Mars`
* `templates`
Contains the HTML code that constructs and prepares the basic structure for scraped data
* `app.py`
Contains Python app that uses the flask library that runs the server in the URL: `http://127.0.0.1:5000/` and calls the `Missions_to_Mars\templates\index.html` file
* `chromedriver`
It is the driver that drives the browser to visit webpage and scrape data
* `facts_table.html`
Contains the HTML code that constructs the table in the final webpage
* `mission_to_mars.ipynb`
Contains the Jupyter Notebook with the explained code for scrapping the different URLs used in the project
* `scrape_mars.py`
Contains Python routine used and called by the main routine `\Missions_to_Mars\app.py` and it is called by pressing the `Scrape New Data`button in the URL: `http://127.0.0.1:5000/`




