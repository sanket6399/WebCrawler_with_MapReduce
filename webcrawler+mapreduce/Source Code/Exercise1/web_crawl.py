from bs4 import BeautifulSoup # for data scrapnig
import requests # for hitting the pages with HTTP
import time     # for storing info about delay
import csv

# Function to scrape conference data for a given page count and research area
def scrape_all_conf_data(num_pages, research_area):
    # Initialize a list which store data of all the conferences for a particular research area
    all_conference_data = []

    # Define the base URL for the selected research area
    if research_area.lower() == 'ml':
        base_url = "http://www.wikicfp.com/cfp/call?conference=Machine%20Learning"
    elif research_area.lower() == 'bigdata':
        base_url = "http://www.wikicfp.com/cfp/call?conference=Big%20Data"
    elif research_area.lower() == 'ai':
        base_url = "http://www.wikicfp.com/cfp/call?conference=Artificial%20Intelligence"
    else:
        raise ValueError("Invalid research area. Please choose 'ML', 'BigData', or 'AI'.")

    # Loop through the specified number of pages
    for page_number in range(1, num_pages + 2):
        # URL for the current page based on page number in the loop
        url = f"{base_url}&page={page_number}"

        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # if we get 200 OK response from the HTTP requests
        if response.status_code == 200:
            # parse the html content
            html = response.text
            # initialisation of soup lib
            soup = BeautifulSoup(html, 'html.parser')

            # The data on the website is in rows and rows are identified based on the color of the row.
            line = soup.find_all('tr', bgcolor=["#f6f6f6", "#e6e6e6"])

            # Initialize a list to store the extracted data for the current page
            conference_data = []

            # Loop through the rows and extract the information (similar to previous code)
            for i in range(0, len(line), 2):
                event_row = line[i]
                #location is stored in the next sub row
                location_row = line[i + 1]

                event_col = event_row.find_all('td')
                location_col = location_row.find_all('td')
                # Previously I had added below check as well, but thought to do entire data cleaning in OpenRefine only
                # if location_columns[1].text == 'N/A':
                #     continue

                # Column check to data scraping, count should be larger tha 3
                if len(event_col) >= 3 and len(location_col) >= 3:
                    event_name = event_col[0].find('a')
                    # Store conf name if it exists
                    event_fname = event_col[1].text
                    # Store conf location if it exists
                    event_loc = location_col[1].text

                    # Extract the conference acronym name directly from the event name
                    conference_acronym = event_name

                    # Store conf acronym if it exists
                    if event_name:
                        conference_name = event_name.text
                    # data append format
                    conference_data.append({
                        'Conference Acronym': conference_acronym,
                        'Conference Name': event_fname,
                        'Conference Location': event_loc,
                        'Research Area': research_area  
                    })

            # Appending all the data to one list
            all_conference_data.extend(conference_data)

            # To meet the compliance requirement of the web site
            time.sleep(10)

        # If no more pages, break
        else:
            break

    return all_conference_data

# Get user input for the number of pages to scrape
num_pages_input = int(input("Enter the number of pages to scrape (e.g., 3): "))

try:
    # universal list to store data of all conference, we will iterate through this to store entire research areas data
    all_scraped_data = []

    # Data crawling for Ml
    ml_data = scrape_all_conf_data(num_pages_input, 'ML')
    all_scraped_data.extend(ml_data)

    # Data Crawling for BigData
    bigdata_data = scrape_all_conf_data(num_pages_input, 'BigData')
    all_scraped_data.extend(bigdata_data)

    # Data crawlin for AI
    ai_data = scrape_all_conf_data(num_pages_input, 'AI')
    all_scraped_data.extend(ai_data)

    # storing all data in below file, this will be stored in python file directory only
    output_file = "conference_all.tsv"

    # Write the scraped data to a tab-separated file
    with open(output_file, mode='w', newline='') as tsv_file:
        fieldnames = ['Conference Acronym', 'Conference Name', 'Conference Location', 'ResearchArea']
        writer = csv.DictWriter(tsv_file, fieldnames=fieldnames, delimiter='\t')

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for item in all_scraped_data:
            writer.writerow({'Conference Acronym': item['Conference Acronym'],
                             'Conference Name': item['Conference Name'],
                             'Conference Location': item['Conference Location'],
                             'ResearchArea': item['Research Area']})

    print(f"Scraped data has been saved to {output_file}")

except ValueError as e:
    print(e)
