# CurrencyRatesScraper

It's a currency Rates scraper usign fixerio REST API


#dependencies
  -mysqlclient
  -fixerio
  
#installing
    
    pip install mysqlclient
    pip install fixerio
     
    easy_install mysqlclient
    easy_install fixerio
 
 #Usage 
    After getting the dependencies run app.py in /app passing to it a currency code and it will show you the current Rate
    EX : python app.py USD
    
    PS: don't forget to change the app/config.py paramaters accordeing to your Database and if you gonna use the docker image don't foreget to add the pramter port=3307 to the function connect() inside app/config.py   
