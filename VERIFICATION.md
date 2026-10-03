# Verification

All checks run on **2026-10-03**. Re-run phase 1 before booking anything (see PLAN.md section 9).

## Method

- **Official site:** fetched every website and booking URL. `scripts/check_links.py` reports 0 broken. OpenTable, Caprice and Nicholson's block scripted requests, so those links were opened by hand in a browser and all resolved.
- **Independent check:** [Hot Dinners closures tracker](https://www.hot-dinners.com/202303199148/Gastroblog/Latest-news/recent-restaurant-closures-shut-london), covering Jan 2025 to Sep 2026. None of the venues below appear on it. Venue-specific sources are linked in the Evidence column where they were used.
- **Pubs:** status and heritage listing from CAMRA WhatPub (the Evidence links). National Inventory (NI) listings were confirmed on CAMRA pages.
- **Bars:** list placings from Time Out reports of The World's 50 Best Bars 2025 and the 2026 51-100 list.
- **Coordinates:** pubs from CAMRA WhatPub; restaurants and bars from OSM Nominatim (1 request/s). Spot-checked against the venue names Nominatim returned.
- **Nearby:** up to 2 pubs and 2 bars within 850 m of each restaurant, as the crow flies.

## Excluded or changed during verification

| Venue | Finding | Action |
|---|---|---|
| FKABAM (Black Axe Mangal) | Closed 20 Dec 2025 (also on the Hot Dinners tracker) | Excluded |
| Le Gavroche | Closed Jan 2024 | Excluded |
| Mangal 2 | Not a chop house; chef has left | Not included |
| The Game Bird (The Stafford) | Replaced by Michael Caines at The Stafford (opened 17 Sep 2025) | Dropped; replaced by Boisdale of Belgravia |
| Goodman Canary Wharf | Closed Jun 2025 | Only the Mayfair and City sites are used |
| Christopher's (Covent Garden) | Closing end Sep 2026 to relocate | Not included |
| Kwānt (Mayfair bar) | Europe's 50 Best 2026 No. 40, but its official site shows only 'Coming Soon' | Left out until the site is back |
| Oriole (bar) | Has moved from Smithfield to Covent Garden | Not used for Farringdon |
| Jerusalem Tavern | Renamed Holy Tavern (2022), operator changed | Not used |
| Ye Grapes, Ye Olde Watling | No NI or current GBG evidence found | Not used |
| sweetingsrestaurant.com | An archive/parasite site, not Sweetings' own | Real site is sweetingsrestaurant.co.uk (HTTP only) |
| Guessed URLs | Several guessed Nicholson's and pub domains turned out wrong or parked (e.g. yeoldecheshirecheese.co.uk) | Website left empty and CAMRA page used as evidence |

## Restaurant scoring (30)

Weights: food 40%, character 25%, group suitability 20%, meat 15%. Group suitability is judged for **a party of five**: how easily you get a good table (online booking, lead time, deposits, no-reservations policies). Sub-scores out of 10 are **editorial judgement** informed by guide listings (Michelin, World's 101 Best Steaks 2026, Time Out), heritage, and what each venue's own site says about booking. They are not taken from any single published rating. A total of 8.5 or more sets `highlight`.

| # | Restaurant | Type | Area | Food | Char. | Group | Meat | **Total** | Book |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [Lutyens Grill](https://www.thened.com/london/restaurants/lutyens-grill) | Chop/steak | City | 8 | 10 | 9 | 10 | **9.0** | [book](https://www.thened.com/london/restaurants/lutyens-grill) |
| 2 | [St. JOHN Smithfield](https://stjohnrestaurant.com/a/restaurants/smithfield) | Chop/steak | Smithfield | 9 | 9 | 8 | 10 | **8.95** | [book](https://stjohnrestaurant.com/a/restaurants/smithfield) |
| 3 | [Savoy Grill](https://www.thesavoylondon.com/restaurants-and-bars/savoy-grill) | Chop/steak | Strand | 8 | 10 | 9 | 9 | **8.85** | [book](https://www.opentable.co.uk/r/savoy-grill-gordon-ramsay-london) |
| 4 | [Hawksmoor St Pancras](https://thehawksmoor.com/locations/st-pancras/) | Chop/steak | King's Cross | 8 | 9 | 9 | 10 | **8.75** | [book](https://thehawksmoor.com/book-a-table/?location=450966) |
| 5 | [Ibai](https://ibai.london/) | Chop/steak | Farringdon | 9 | 8 | 8 | 10 | **8.7** | [book](https://www.sevenrooms.com/landing/ibailondon) |
| 6 | [Quality Chop House](https://thequalitychophouse.com/) | Chop/steak | Farringdon | 8 | 10 | 8 | 9 | **8.65** | [book](https://www.opentable.co.uk/the-quality-chop-house-reservations-london?restref=96150) |
| 7 | [The Guinea Grill](https://www.theguinea.co.uk/) | Chop/steak | Mayfair | 8 | 10 | 7 | 10 | **8.6** | ⚠️ phone/email |
| 8 | [The Devonshire](https://www.devonshiresoho.co.uk/) | Chop/steak | Soho | 9 | 9 | 7 | 9 | **8.6** | [book](https://onsass.designmynight.com/?background-color=%2334533b&primary-color=%23ffffff&body-text-color=%23ffffff&outer-border-color=white) |
| 9 | [Simpson's in the Strand](https://www.simpsonsinthestrand.co.uk/) | Fine dining | Strand | 7 | 10 | 9 | 10 | **8.6** | [book](https://www.sevenrooms.com/explore/granddivan/reservations/create/search) |
| 10 | [The Ritz Restaurant](https://www.theritzlondon.com/dine-with-us/the-ritz-restaurant/) | Fine dining | Piccadilly | 9 | 10 | 7 | 7 | **8.55** | [book](https://www.sevenrooms.com/explore/theritzrestaurant/reservations/create/search) |
| 11 | [Hawksmoor Seven Dials](https://thehawksmoor.com/locations/seven-dials/) | Chop/steak | Covent Garden | 8 | 8 | 9 | 10 | **8.5** | [book](https://thehawksmoor.com/book-a-table/?location=45565) |
| 12 | [Hawksmoor Guildhall](https://thehawksmoor.com/locations/guildhall/) | Chop/steak | City | 8 | 8 | 9 | 10 | **8.5** | [book](https://thehawksmoor.com/book-a-table/?location=71086) |
| 13 | [Rules](https://rules.co.uk/) | Fine dining | Covent Garden | 7 | 10 | 9 | 9 | **8.45** | [book](https://www.sevenrooms.com/reservations/rules) |
| 14 | [Brat](https://bratrestaurant.co.uk/redchurch-st) | Chop/steak | Shoreditch | 10 | 8 | 6 | 8 | **8.4** | [book](https://www.sevenrooms.com/reservations/bratshoreditch) |
| 15 | [Wiltons](https://wiltons.co.uk/) | Fine dining | St James's | 8 | 10 | 8 | 7 | **8.35** | [book](https://www.sevenrooms.com/reservations/wiltons) |
| 16 | [Kerridge's Bar & Grill](https://www.corinthia.com/en-gb/london/kerridges/) | Fine dining | Whitehall | 8 | 8 | 9 | 9 | **8.35** | [book](https://www.sevenrooms.com/explore/kerridgesatcorinthia/reservations/create/search/) |
| 17 | [Charlie's at Brown's](https://www.roccofortehotels.com/hotels-and-resorts/brown-s-hotel/dining/charlies-at-browns/) | Fine dining | Mayfair | 8 | 9 | 8 | 8 | **8.25** | [book](https://www.roccofortehotels.com/hotels-and-resorts/brown-s-hotel/dining/charlies-at-browns/) |
| 18 | [Mountain](https://mountainbeakstreet.com/) | Chop/steak | Soho | 9 | 8 | 7 | 8 | **8.2** | [book](https://www.sevenrooms.com/reservations/mountain) |
| 19 | [Kitty Fisher's](https://www.kittyfishers.com/) | Chop/steak | Mayfair | 8 | 8 | 8 | 9 | **8.15** | [book](https://www.sevenrooms.com/reservations/kittyfishers) |
| 20 | [Goodman Mayfair](https://www.goodmanrestaurants.com/mayfair) | Chop/steak | Mayfair | 8 | 7 | 8 | 10 | **8.05** | [book](https://www.sevenrooms.com/explore/goodmanmayfair/reservations/create/search) |
| 21 | [Goodman City](https://www.goodmanrestaurants.com/city) | Chop/steak | City | 8 | 7 | 8 | 10 | **8.05** | [book](https://www.sevenrooms.com/reservations/goodmancity) |
| 22 | [Holborn Dining Room](https://holborndiningroom.com/) | Chop/steak | Holborn | 8 | 8 | 8 | 8 | **8.0** | [book](https://www.sevenrooms.com/reservations/rwldnholborndiningroom) |
| 23 | [Boisdale of Belgravia](https://www.boisdale.co.uk/restaurant/belgravia) | Fine dining | Belgravia | 7 | 9 | 8 | 9 | **8.0** | ⚠️ phone/email |
| 24 | [Bentley's Oyster Bar & Grill](https://www.bentleys.org/) | Fine dining | Piccadilly | 8 | 9 | 8 | 6 | **7.95** | [book](https://www.sevenrooms.com/explore/bentleys/reservations/create/search/) |
| 25 | [J. Sheekey](https://j-sheekey.co.uk/) | Fine dining | Covent Garden | 8 | 9 | 8 | 5 | **7.8** | [book](https://www.opentable.co.uk/j-sheekey-the-restaurant-reservations-london?restref=111285) |
| 26 | [Blacklock Soho](https://theblacklock.com/restaurants/blacklock-soho/) | Chop/steak | Soho | 7 | 7 | 8 | 10 | **7.65** | [book](https://theblacklock.com/soho-reservations/) |
| 27 | [Blacklock City](https://theblacklock.com/restaurants/city/) | Chop/steak | City | 7 | 7 | 8 | 10 | **7.65** | [book](https://theblacklock.com/city-reservations/) |
| 28 | [Scott's](https://scotts-mayfair.com/) | Fine dining | Mayfair | 8 | 9 | 7 | 5 | **7.6** | [book](https://scotts_mayfair.capricebookings.com/) |
| 29 | [Arlington](https://www.arlington.london/) | Fine dining | St James's | 7 | 9 | 8 | 6 | **7.55** | [book](https://www.sevenrooms.com/reservations/arlingtonrestaurant) |
| 30 | [Sweetings](http://www.sweetingsrestaurant.co.uk/) | Fine dining | City | 7 | 10 | 3 | 4 | **6.5** | ⚠️ phone/email |

Split: 18 chop/steak, 12 fine dining.

## Trading status: every venue

| Venue | Type | Status | Checked | Evidence | Nearby (m) |
|---|---|---|---|---|---|
| Lutyens Grill | Chop/steak | trading | 2026-10-03 | [source](https://www.thened.com/london/restaurants/lutyens-grill) | Jamaica Wine House 326, Lamb Tavern 478, The Nickel Bar 0 |
| St. JOHN Smithfield | Chop/steak | trading | 2026-10-03 | [source](https://stjohnrestaurant.com/a/restaurants/smithfield) | Fox & Anchor 43, Ye Olde Mitre 479, The Parlour at The Zetter 345, Tayēr + Elementary 843 |
| Savoy Grill | Chop/steak | trading | 2026-10-03 | [source](https://www.thesavoylondon.com/restaurants-and-bars/savoy-grill) | The Harp 383, Lamb & Flag 400, American Bar at The Savoy 0, Bar Termini Soho 753 |
| Hawksmoor St Pancras | Chop/steak | trading | 2026-10-03 | [source](https://thehawksmoor.com/locations/st-pancras/) | Euston Tap 576, Booking Office 1869 23 |
| Ibai | Chop/steak | trading | 2026-10-03 | [source](https://www.timeout.com/london/news/9-london-steak-restaurants-have-been-named-in-the-101-best-in-the-world-for-2026-040126) | Fox & Anchor 264, Ye Olde Mitre 547, The Parlour at The Zetter 630, The Nickel Bar 819 |
| Quality Chop House | Chop/steak | trading | 2026-10-03 | [source](https://thequalitychophouse.com/) | The Lamb 649, Cittie of Yorke 722, The Parlour at The Zetter 464 |
| The Guinea Grill | Chop/steak | trading | 2026-10-03 | [source](https://www.theguinea.co.uk/) | The Audley 490, Red Lion 674, Donovan Bar 302, Connaught Bar 372 |
| The Devonshire | Chop/steak | trading | 2026-10-03 | [source](https://www.devonshiresoho.co.uk/) | Red Lion 265, The French House 341, Donovan Bar 504, Bar Termini Soho 510 |
| Simpson's in the Strand | Fine dining | trading | 2026-10-03 | [source](https://www.simpsonsinthestrand.co.uk/reservations/) | Lamb & Flag 374, The Harp 382, American Bar at The Savoy 43, Bar Termini Soho 724 |
| The Ritz Restaurant | Fine dining | trading | 2026-10-03 | [source](https://www.theritzlondon.com/dine-with-us/the-ritz-restaurant/) | Red Lion 371, The Audley 759, Rivoli Bar 0, Donovan Bar 216 |
| Hawksmoor Seven Dials | Chop/steak | trading | 2026-10-03 | [source](https://thehawksmoor.com/locations/seven-dials/) | Lamb & Flag 195, The Salisbury 294, Bar Termini Soho 280, Three Sheets Soho 389 |
| Hawksmoor Guildhall | Chop/steak | trading | 2026-10-03 | [source](https://thehawksmoor.com/locations/guildhall/) | Jamaica Wine House 474, Lamb Tavern 607, The Nickel Bar 208 |
| Rules | Fine dining | trading | 2026-10-03 | [source](https://rules.co.uk/) | Lamb & Flag 198, The Harp 233, American Bar at The Savoy 201, Bar Termini Soho 554 |
| Brat | Chop/steak | trading | 2026-10-03 | [source](https://guide.michelin.com/mt/en/greater-london/london/restaurant/brat) | Pride of Spitalfields 704, Seed Library 158 |
| Wiltons | Fine dining | trading | 2026-10-03 | [source](https://wiltons.co.uk/) | Red Lion 208, The French House 763, Rivoli Bar 163, Dukes Bar 249 |
| Kerridge's Bar & Grill | Fine dining | trading | 2026-10-03 | [source](https://www.corinthia.com/en-gb/london/kerridges/) | The Harp 375, The Salisbury 541, American Bar at The Savoy 463 |
| Charlie's at Brown's | Fine dining | trading | 2026-10-03 | [source](https://www.roccofortehotels.com/hotels-and-resorts/brown-s-hotel/dining/charlies-at-browns/) | Red Lion 408, The Audley 661, Donovan Bar 0, Rivoli Bar 216 |
| Mountain | Chop/steak | trading | 2026-10-03 | [source](https://mountainbeakstreet.com/) | Red Lion 423, The French House 456, Donovan Bar 422, Rivoli Bar 575 |
| Kitty Fisher's | Chop/steak | trading | 2026-10-03 | [source](https://www.kittyfishers.com/) | The Audley 508, Red Lion 713, Rivoli Bar 342, Donovan Bar 401 |
| Goodman Mayfair | Chop/steak | trading | 2026-10-03 | [source](https://www.goodmanrestaurants.com/mayfair) | Red Lion 664, Dog & Duck 695, Donovan Bar 461, Connaught Bar 665 |
| Goodman City | Chop/steak | trading | 2026-10-03 | [source](https://www.goodmanrestaurants.com/city) | Jamaica Wine House 389, Lamb Tavern 538, The Nickel Bar 73 |
| Holborn Dining Room | Chop/steak | trading | 2026-10-03 | [source](https://www.rosewoodhotels.com/en/london/dining/holborn-dining-room) | Cittie of Yorke 394, The Lamb 632, Scarfes Bar 0, American Bar at The Savoy 825 |
| Boisdale of Belgravia | Fine dining | trading | 2026-10-03 | [source](https://www.boisdale.co.uk/restaurant/belgravia) | Star Tavern 703, The Cocktail Bar at The Goring 409 |
| Bentley's Oyster Bar & Grill | Fine dining | trading | 2026-10-03 | [source](https://www.bentleys.org/) | Red Lion 157, The French House 549, Donovan Bar 312, Rivoli Bar 363 |
| J. Sheekey | Fine dining | trading | 2026-10-03 | [source](https://j-sheekey.co.uk/) | The Salisbury 38, Lamb & Flag 162, Bar Termini Soho 337, Three Sheets Soho 482 |
| Blacklock Soho | Chop/steak | trading | 2026-10-03 | [source](https://theblacklock.com/restaurants/blacklock-soho/) | The French House 228, Dog & Duck 309, Bar Termini Soho 396, Three Sheets Soho 417 |
| Blacklock City | Chop/steak | trading | 2026-10-03 | [source](https://theblacklock.com/restaurants/city/) | Lamb Tavern 228, Jamaica Wine House 244, The Nickel Bar 517 |
| Scott's | Fine dining | trading | 2026-10-03 | [source](https://scotts-mayfair.com/) | The Audley 58, Connaught Bar 64, Donovan Bar 611 |
| Arlington | Fine dining | trading | 2026-10-03 | [source](https://www.arlington.london/) | Red Lion 353, The Audley 848, Rivoli Bar 101, Dukes Bar 136 |
| Sweetings | Fine dining | trading | 2026-10-03 | [source](https://www.cityam.com/a-love-letter-to-sweetings-the-citys-oldest-restaurant/) | Jamaica Wine House 504, Lamb Tavern 659, The Nickel Bar 239 |
| American Bar at The Savoy | Cocktail bar | trading | 2026-10-03 | [source](https://www.thesavoylondon.com/restaurants-and-bars/american-bar) |  |
| Bar Termini Soho | Cocktail bar | trading | 2026-10-03 | [source](https://bar-termini-soho.com/) |  |
| Booking Office 1869 | Cocktail bar | trading | 2026-10-03 | [source](https://www.booking-office.co.uk/) |  |
| Connaught Bar | Cocktail bar | trading | 2026-10-03 | [source](https://www.timeout.com/london/news/its-official-4-london-bars-are-in-the-50-best-in-the-world-right-now-100825) |  |
| Donovan Bar | Cocktail bar | trading | 2026-10-03 | [source](https://www.roccofortehotels.com/hotels-and-resorts/brown-s-hotel/dining/donovan-bar/) |  |
| Dukes Bar | Cocktail bar | trading | 2026-10-03 | [source](https://www.dukeshotel.com/dukesbar.html) |  |
| Rivoli Bar | Cocktail bar | trading | 2026-10-03 | [source](https://www.theritzlondon.com/dine-with-us/rivoli-bar/) |  |
| Scarfes Bar | Cocktail bar | trading | 2026-10-03 | [source](https://www.timeout.com/london/news/worlds-50-best-bars-2026-longlist-scarfes-three-sheets-soho-092326) |  |
| Seed Library | Cocktail bar | trading | 2026-10-03 | [source](https://www.onehundredshoreditch.com/eat-drink/seed-library/) |  |
| Tayēr + Elementary | Cocktail bar | trading | 2026-10-03 | [source](https://www.timeout.com/london/news/its-official-4-london-bars-are-in-the-50-best-in-the-world-right-now-100825) |  |
| The Cocktail Bar at The Goring | Cocktail bar | trading | 2026-10-03 | [source](https://www.thegoring.com/food-drink/the-goring-cocktail-bar/) |  |
| The Nickel Bar | Cocktail bar | trading | 2026-10-03 | [source](https://www.thened.com/london/restaurants/the-nickel-bar) |  |
| The Parlour at The Zetter | Cocktail bar | trading | 2026-10-03 | [source](https://thezetter.com/clerkenwell/the-parlour/) |  |
| Three Sheets Soho | Cocktail bar | trading | 2026-10-03 | [source](https://www.timeout.com/london/news/worlds-50-best-bars-2026-longlist-scarfes-three-sheets-soho-092326) |  |
| Cittie of Yorke ★ | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/cittie-of-yorke-london-125495) |  |
| Dog & Duck | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/dog-duck-london-128663) |  |
| Euston Tap | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/euston-tap-london-125165) |  |
| Fox & Anchor | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/fox-anchor-london-156298) |  |
| Jamaica Wine House | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/jamaica-wine-house-london-156624) |  |
| Lamb & Flag | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/lamb-flag-london-128715) |  |
| Lamb Tavern | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/lamb-tavern-london-156616) |  |
| Pride of Spitalfields | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/pride-of-spitalfields-london-155017) |  |
| Red Lion ★ | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/red-lion-london-128701) |  |
| Star Tavern ★ | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/star-tavern-london-128650) |  |
| The Audley | Pub | trading | 2026-10-03 | [source](https://pubheritage.camra.org.uk/pubs/2131) |  |
| The Black Friar ★ | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/black-friar-london-156696) |  |
| The French House ★ | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/french-house-london-129160) |  |
| The Harp ★ | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/harp-london-128660) |  |
| The Lamb ★ | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/lamb-london-125487) |  |
| The Salisbury | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/salisbury-london-128829) |  |
| Ye Olde Cheshire Cheese ★ | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/olde-cheshire-cheese-london-156637) |  |
| Ye Olde Mitre ★ | Pub | trading | 2026-10-03 | [source](https://camra.org.uk/pubs/olde-mitre-london-156323) |  |

## Empty fields (flagged in the UI)

- **The Guinea Grill**: no booking_url confirmed. Three private rooms: Gallery (10), Wine Room (14), Boardroom (20). Book by phone or email (020 7409 1728).
- **Sweetings**: no booking_url confirmed. Lunch only, Mon-Fri 11:30-15:00. No reservations: arrive before noon. Not suitable for a booked group dinner.
- **Boisdale of Belgravia**: no booking_url confirmed. Private dining rooms and published group menus. Book by phone (020 7730 6922) or reservations@boisdale.co.uk.
- **Cittie of Yorke**: no website confirmed. See the CAMRA evidence link.
- **Ye Olde Cheshire Cheese**: no website confirmed. See the CAMRA evidence link.
- **The Salisbury**: no website confirmed. See the CAMRA evidence link.
- **Red Lion**: no website confirmed. See the CAMRA evidence link.
- **Pride of Spitalfields**: no website confirmed. See the CAMRA evidence link.

## Photo credits

Photos are freely licensed images from Wikimedia Commons, hotlinked from upload.wikimedia.org. Each one is the lead image of a Wikipedia article whose coordinates are within 250 m of the venue (`scripts/fetch_images.py`). Where a venue sits inside a larger building (hotel bars, Leadenhall Market), the photo shows that building, and the dialog says what is pictured.

| Venue | Pictured | Credit | Licence |
|---|---|---|---|
| American Bar at The Savoy | [Savoy Hotel](https://commons.wikimedia.org/wiki/File:H%C3%B4tel_Savoy_The_Strand_Londres_-_edited.jpg) | Photo by CVB, edited and cropped by Cart | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| Bentley's Oyster Bar & Grill | [Bentley's Oyster Bar and Grill](https://commons.wikimedia.org/wiki/File:Bentleys_sign_2.jpg) | Emmaccm1 | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| Booking Office 1869 | [St Pancras London Hotel](https://commons.wikimedia.org/wiki/File:St_Pancras_Renaissance_London_Hotel_2011-06-19.jpg) | LepoRello | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) |
| Charlie's at Brown's | [Brown's Hotel, London](https://commons.wikimedia.org/wiki/File:Brown%27s_Hotel_London.jpg) | Londonmatt | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0) |
| Cittie of Yorke | [Cittie of Yorke](https://commons.wikimedia.org/wiki/File:Cittie_of_Yorke_pub,_London_-_2023-01-27.jpg) | The wub | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| Dog & Duck | [Dog and Duck, Soho](https://commons.wikimedia.org/wiki/File:Dog_and_Duck,_Soho,_W1_(2534053077).jpg) | Ewan Munro from London, UK | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |
| Donovan Bar | [Brown's Hotel, London](https://commons.wikimedia.org/wiki/File:Brown%27s_Hotel_London.jpg) | Londonmatt | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0) |
| Dukes Bar | [Dukes Hotel](https://commons.wikimedia.org/wiki/File:Hotel_Dukes_London.jpg) | Ricardalovesmonuments | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| Fox & Anchor | [Fox and Anchor](https://commons.wikimedia.org/wiki/File:Fox_and_Anchor,_Farringdon,_EC1_(2486430867).jpg) | Ewan Munro from London, UK | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |
| Hawksmoor St Pancras | [St Pancras London Hotel](https://commons.wikimedia.org/wiki/File:St_Pancras_Renaissance_London_Hotel_2011-06-19.jpg) | LepoRello | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) |
| Holborn Dining Room | [Rosewood London](https://commons.wikimedia.org/wiki/File:The_Renaissance_Chancery_Court_Hotel,_High_Holborn-4846480310.jpg) | Robert Cutts | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0) |
| Jamaica Wine House | [Jamaica Wine House](https://commons.wikimedia.org/wiki/File:Jamaica_Wine_House_20130323_049.jpg) | Elisa.rolle | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| Kerridge's Bar & Grill | [Corinthia Hotel London](https://commons.wikimedia.org/wiki/File:Corinthia_Hotel_London.jpg) | Vitor Y | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0) |
| Lamb & Flag | [Lamb and Flag, Covent Garden](https://commons.wikimedia.org/wiki/File:Lamb_and_Flag,_Covent_Garden,_WC2_(3578392482).jpg) | Ewan Munro from London, UK | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |
| Lamb Tavern | [Leadenhall Market](https://commons.wikimedia.org/wiki/File:Leadenhall_Market_In_London_-_Feb_2006_rotated.jpg) | Diliff | [CC BY 2.5](https://creativecommons.org/licenses/by/2.5) |
| Lutyens Grill | [Midland Bank, Poultry](https://commons.wikimedia.org/wiki/File:Midland_Bank,_City_of_London.jpg) | Steve Cadman | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |
| Pride of Spitalfields | [The Pride of Spitalfields](https://commons.wikimedia.org/wiki/File:The_Pride_of_Spitalfields.jpg) | Clavileno | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) |
| Red Lion | [Red Lion, Duke of York Street](https://commons.wikimedia.org/wiki/File:Red_Lion,_St_Jamess,_SW1_(3400213792).jpg) | Ewan Munro from London, UK | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |
| Rivoli Bar | [The Ritz Hotel, London](https://commons.wikimedia.org/wiki/File:The_Ritz_(6902790412).jpg) | Tony Hisgett from Birmingham, UK | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0) |
| Rules | [Rules (restaurant)](https://commons.wikimedia.org/wiki/File:Rules,_London%27s_oldest_restaurant._-_geograph.org.uk_-_510375.jpg) | Steve F | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |
| Savoy Grill | [Savoy Hotel](https://commons.wikimedia.org/wiki/File:H%C3%B4tel_Savoy_The_Strand_Londres_-_edited.jpg) | Photo by CVB, edited and cropped by Cart | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| Scarfes Bar | [Rosewood London](https://commons.wikimedia.org/wiki/File:The_Renaissance_Chancery_Court_Hotel,_High_Holborn-4846480310.jpg) | Robert Cutts | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0) |
| Scott's | [Scott's (restaurant)](https://commons.wikimedia.org/wiki/File:Scott%27s_Restaurant,_Mount_Street,_London_-_geograph.org.uk_-_948875.jpg) | Oast House Archive | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |
| Simpson's in the Strand | [Simpson's-in-the-Strand](https://commons.wikimedia.org/wiki/File:Simpson%27s-in-the-Strand_2023-12-04.jpg) | Matt Brown | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0) |
| St. JOHN Smithfield | [St. John (restaurant)](https://commons.wikimedia.org/wiki/File:26_St_John_Street,_Clerkenwell,_April_2023.jpg) | No Swan So Fine | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| Star Tavern | [Star Tavern, Belgravia](https://commons.wikimedia.org/wiki/File:Star_Tavern,_Belgravia,_SW1_(4588158213).jpg) | Ewan Munro from London, UK | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |
| Sweetings | [Sweetings](https://commons.wikimedia.org/wiki/File:Sweetings,_Queen_Victoria_Street.jpg) | Gareth E. Kegg | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| The Black Friar | [The Black Friar, Blackfriars](https://commons.wikimedia.org/wiki/File:Black-Friar-Pub-Londres-230819.jpg) | FDV | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| The Cocktail Bar at The Goring | [Goring Hotel](https://commons.wikimedia.org/wiki/File:Goring_Hotel_Londres.jpg) | CVB | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| The Devonshire | [The Devonshire, London](https://commons.wikimedia.org/wiki/File:Devonshire,_Soho,_W1.jpg) | Ewan-M | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) |
| The French House | [The French House, Soho](https://commons.wikimedia.org/wiki/File:French_House,_Soho,_W1_(2711027655).jpg) | Ewan Munro from London, UK | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |
| The Harp | [The Harp](https://commons.wikimedia.org/wiki/File:Harp,_Covent_Garden,_WC2_(2913857439).jpg) | Ewan Munro from London, UK | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |
| The Lamb | [The Lamb, Bloomsbury](https://commons.wikimedia.org/wiki/File:The_Lamb_-_Bloomsbury_-_WC1.jpg) | Ewan Munro from London, UK | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |
| The Nickel Bar | [Midland Bank, Poultry](https://commons.wikimedia.org/wiki/File:Midland_Bank,_City_of_London.jpg) | Steve Cadman | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |
| The Parlour at The Zetter | [Zetter Hotel](https://commons.wikimedia.org/wiki/File:Zetter_Hotel_2.jpg) | Mx. Granger | [CC0](http://creativecommons.org/publicdomain/zero/1.0/deed.en) |
| The Ritz Restaurant | [The Ritz Hotel, London](https://commons.wikimedia.org/wiki/File:The_Ritz_(6902790412).jpg) | Tony Hisgett from Birmingham, UK | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0) |
| The Salisbury | [The Salisbury, Covent Garden](https://commons.wikimedia.org/wiki/File:Salisbury,_Covent_Garden,_WC2_(2913856903).jpg) | Ewan Munro from London, UK | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |
| Ye Olde Cheshire Cheese | [Ye Olde Cheshire Cheese](https://commons.wikimedia.org/wiki/File:Yeoldcheshirecheese.jpg) | Banjobacon at English Wikipedia | [CC BY 2.5](https://creativecommons.org/licenses/by/2.5) |
| Ye Olde Mitre | [Ye Olde Mitre](https://commons.wikimedia.org/wiki/File:Ye_Olde_Mitre_Tavern_-_geograph.org.uk_-_763877.jpg) | Row17 | [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0) |

23 venues have no photo, because no freely licensed image of the venue itself could be confirmed.

## Caveats

- Michelin star counts are not quoted. Sources disagreed (e.g. Brat), so venues are just described as 'Michelin-starred'.
- `group_notes` come from each venue's own site on the check date. Treat them as prompts to call, not as fact.
- Sweetings is lunch-only and takes no bookings, so it is a weekday-lunch option, not a group dinner.
- Distances are straight-line. Walking routes are 10-30% longer.
