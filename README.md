# Scrapy-Alxa-Categories
Contains individual scrapy spiders for all all alexa categories.

Spiders have already created a list of top 500 URLs unde each category. CD into each directory to see the csv files.

To run each spider individually

1. CD into each category directory.
2. run.. $scrapy crawl alexa -o any_file_name.csv -s CLOSESPIDER_PAGECOUNT=25
3.  -o flag is used for output, the format of the output could be either csv or json or xml (see scrapy doc)
4.  -s CLOSESPIDER_PAGECOUNT is used for pagination, in this case the spider paginates through 25 pages (each alexa page contains 21 URLs)
