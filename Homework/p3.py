# Carson Chadwick, Bodhe Melver, Caleb Stephenson, John Gibson, Matthew Diamond, Ryan Hagerty
# Section 04
# This program scrapes data from churchofjesuschrist.org's general conference talks from october 2023.

# Imports
from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plot

# define the connection parameters:
database_name = "is303"
db_user = "testuser"
db_password = "test"
db_host = "localhost" #this just means the database is stored on your own computer
db_port = "5432" # default setting
# Connect to the PostgreSQL database
engine = sqlalchemy.create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{database_name}')


# Have the user input their choice
iChoice = 1
# While loop to allowing them to keep selecting an option.
while iChoice == 1 or iChoice == 2 :
  
    iChoice = int(input("If you want to scrape data, enter 1. If you want to see summaries of stored data, enter 2. Enter any other value to exit the program: "))

    print()
    # for option 1
    if iChoice == 1 :
        drop_table_query = sqlalchemy.text('drop table if exists general_conference;')
        conn = engine.connect()
        conn.execute(drop_table_query)
        conn.commit()
        conn.close()
        # Connect to website
        oResponse = requests.get("https://www.churchofjesuschrist.org/study/general-conference/2023/10?lang=eng")
        # Make Soup
        soup = BeautifulSoup(oResponse.content, 'html.parser')
        # Filter Soup
        oData = soup.find_all('nav', attrs={'class' : 'manifest'})
        # Dictionary
        original_dict = {'Speaker_Name' : '', 'Talk_Name' : '', 'Kicker' : '', 'Matthew': 0, 'Mark': 0, 'Luke': 0, 'John': 0, 
                                 'Acts': 0, 'Romans': 0, '1 Corinthians': 0, '2 Corinthians': 0, 'Galatians': 0, 'Ephesians': 0, 
                                 'Philippians': 0, 'Colossians': 0, '1 Thessalonians': 0, '2 Thessalonians': 0, '1 Timothy': 0, 
                                 '2 Timothy': 0, 'Titus': 0, 'Philemon': 0, 'Hebrews': 0, 'James': 0, '1 Peter': 0, '2 Peter': 0, 
                                 '1 John': 0, '2 John': 0, '3 John': 0, 'Jude': 0, 'Revelation': 0, 'Genesis': 0, 'Exodus': 0, 
                                 'Leviticus': 0, 'Numbers': 0, 'Deuteronomy': 0, 'Joshua': 0, 'Judges': 0, 'Ruth': 0, '1 Samuel': 0, 
                                 '2 Samuel': 0, '1 Kings': 0, '2 Kings': 0, '1 Chronicles': 0, '2 Chronicles': 0, 'Ezra': 0, 'Nehemiah': 0, 
                                 'Esther': 0, 'Job': 0, 'Psalm': 0, 'Proverbs': 0, 'Ecclesiastes': 0, 'Song of Solomon': 0, 'Isaiah': 0, 
                                 'Jeremiah': 0, 'Lamentations': 0, 'Ezekiel': 0, 'Daniel': 0, 'Hosea': 0, 'Joel': 0, 'Amos': 0, 'Obadiah': 0, 
                                 'Jonah': 0, 'Micah': 0, 'Nahum': 0, 'Habakkuk': 0, 'Zephaniah': 0, 'Haggai': 0, 'Zechariah': 0, 'Malachi': 0, 
                                 '1 Nephi': 0, '2 Nephi': 0, 'Jacob': 0, 'Enos': 0, 'Jarom': 0, 'Omni': 0, 'Words of Mormon': 0, 'Mosiah': 0, 
                                 'Alma': 0, 'Helaman': 0, '3 Nephi': 0, '4 Nephi': 0, 'Mormon': 0, 'Ether': 0, 'Moroni': 0, 
                                 'Doctrine and Covenants': 0, 'Moses': 0, 'Abraham': 0, 'Joseph Smith—Matthew': 0, 
                                 'Joseph Smith—History': 0, 'Articles of Faith': 0}
        
        # Get website for each of the talks
        for oChild in oData:
            for link in oChild.find_all('a', href=True):
                title_tag = link.find('p', class_='title')
                if 'session' not in link['href'] and (title_tag.string.strip() != "Sustaining of General Authorities, Area Seventies, and General Officers"):
                    fullUrl = "https://www.churchofjesuschrist.org" + link['href']
                    print(f"trying to scrape url: {fullUrl}")
                    response = requests.get(fullUrl)
                    # For each new website make a soup
                    newSoup = BeautifulSoup(response.content, 'html.parser')
                    # Copy of Dictionary
                    standard_works_dict = original_dict.copy()
                    footnotes_section = newSoup.find('footer', attrs={'class' : 'notes'})
                    # Collect the text from the footer
                    if footnotes_section is not None :
                        footnotes_text = footnotes_section.get_text()
                        # Match and count the keys from the dictionary
                        for key in standard_works_dict :
                            count = footnotes_text.count(key)
                            standard_works_dict[key] = count
                    # Assign the speaker name, kicker, and talk name to the dictionary
                    standard_works_dict['Speaker_Name'] = newSoup.find('p', attrs={'id' : 'author1'}).text.strip().split("By")[1].strip()
                    standard_works_dict['Kicker'] = newSoup.find('p', attrs={'class' : 'kicker'}).text.strip()
                    standard_works_dict['Talk_Name'] = newSoup.find('h1', attrs={'id': 'title1'}).text.strip()
                    # Make dataframe
                    df = pd.DataFrame([standard_works_dict])
                    # Write the dictionary to the database
                    df.to_sql('general_conference', engine, if_exists='append', index=False)

        print("You've saved the scraped data to your postgres database.\n")

    # for option 2
    if iChoice == 2 :
        iSelect = int(input("You selected to see summaries. Enter 1 to see a summary of all talks. Enter 2 to see a specific talk. Enter anything else to exit: "))
        print()
        # Option 1
        if iSelect == 1 :
            # grab data from database and save as dataframe
            sql_query = 'select * from general_conference'
            df_from_postgres = pd.read_sql_query(sql_query, engine)
            # Drop speaker name, talk name, and kicker and filter out those that have less than 2
            df_sums = df_from_postgres.drop(['Speaker_Name', 'Talk_Name', 'Kicker'], axis=1).sum()
            df_sums_filtered = df_sums[df_sums > 2]
            # make bar chart
            df_sums_filtered.plot(kind='bar', color='orange')
            plot.title('Standard Works Referenced in General Conference')
            plot.xlabel('Standard Works Books')
            plot.ylabel('# Times Referenced')
            plot.tight_layout()
            plot.show()
       # Option 2
        if iSelect == 2 :
            # Make panda datafram from database
            sql_query = 'select * from general_conference'
            df_from_postgres = pd.read_sql_query(sql_query, engine)
            dctTalks = {}
            # For row add it to the dctTalks and print out the speaker and name
            for index, row in df_from_postgres.iterrows():
                dctTalks[index] = row['Talk_Name']
                print(f"{index+1}: {row["Speaker_Name"]} - {row["Talk_Name"]}")
            # If talk doesn't have data do the try and except
            try:
                # Ask what talk they want
                numTalk = int(input("Please enter the number of the talk you want to see summarized: "))
                print()
                requested_talk = dctTalks[numTalk-1]
                # Filter out name, talkname, and kicker
                df_filtered = df_from_postgres.query(f"Talk_Name == '{requested_talk}'")
                df_filtered = df_filtered.drop(['Speaker_Name', 'Talk_Name', 'Kicker'], axis=1).sum()
                df_filtered_sums = df_filtered[df_filtered > 0]
                # Make bar chart
                df_filtered_sums.plot(kind='bar', color='orange', rot=25)
                plot.title(f"Standard works Referenced in: {requested_talk}")
                plot.xlabel('Standard Works Books')
                plot.ylabel('# Times Referenced')
                plot.tight_layout()
                plot.show()
            except:
                print("This talk has has no references.\n")
# Exit loop
print("Closing the program.")
