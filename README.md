# Scripting-and-automation-task
In this task,I wrote a scrapy spider  for a website URL:  https://www.midsouthshooterssupply.com/dept/reloading/primers

Points to keep in mind:
Make sure all the pages and all items are scraped.
It is possible you could not find values for a few data points, in that case, you shouldn't add the key to the final JSON.
If you are scraping a paragraph, make sure new lines must be replaced by '__ '. Multiple paras should be concatenated using '__'.
First, scrape the required fields that are listed below:
1. Price in dollars
2. Description
3. Review
4. Delivery Info
5. Title
6. Stock status i.e. in-stock or out-stock. If in-stock then the value would true and for out-stock value should be false.
7. Manufacturer i.e. Remington, Winchester, etc.
For this scraper, use rotating proxies from this website http://www.freeproxylists.net/ (only US )

**The output should be in the list of dictionaries, finally represented in JSON.**
