This code is used to retrieve search results from scryfall, and use them to generate a txt that can be imported to TCGPlayer's Mass Entry tool. My goal was to be able to buy one of each card returned, but you can modify the txt after if you'd like.
Please double check everything before you buy!

To run:
Open cmd.
Navigate to downloaded files, then to the "dist" folder.
Run scryfallToTCGMassEntry "Search Results Url"
Search Resulsts url should look like:
"https://scryfall.com/search?q=set%3Alcc+-is%3Areprint&unique=cards&as=grid&order=set"
There is a 3 second delay between card pulls for internet courtesy, but if you wish to remove this you can set it to 1 or even 0 by adding a number after the command, for example:
scryfallToTCGMassEntry "https://scryfall.com/search?q=set%3Alcc+-is%3Areprint&unique=cards&as=grid&order=set" 1
