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

Weights: food 40%, character 25%, group suitability 20%, meat 15%. Sub-scores out of 10 are **editorial judgement** informed by guide listings (Michelin, World's 101 Best Steaks 2026, Time Out), heritage, and what each venue's own site says about groups. They are not taken from any single published rating. A total of 8.5 or more sets `highlight`.

| # | Restaurant | Type | Area | Food | Char. | Group | Meat | **Total** | 8+ group | Book |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [The Guinea Grill](https://www.theguinea.co.uk/) | Chop/steak | Mayfair | 8 | 10 | 9 | 10 | **9.0** | yes | ⚠️ phone/email |
| 2 | [Lutyens Grill](https://www.thened.com/london/restaurants/lutyens-grill) | Chop/steak | City | 8 | 10 | 8 | 10 | **8.8** | yes | [book](https://www.thened.com/london/restaurants/lutyens-grill) |
| 3 | [The Devonshire](https://www.devonshiresoho.co.uk/) | Chop/steak | Soho | 9 | 9 | 8 | 9 | **8.8** | yes | [book](https://onsass.designmynight.com/?background-color=%2334533b&primary-color=%23ffffff&body-text-color=%23ffffff&outer-border-color=white) |
| 4 | [St. JOHN Smithfield](https://stjohnrestaurant.com/a/restaurants/smithfield) | Chop/steak | Smithfield | 9 | 9 | 7 | 10 | **8.75** | yes | [book](https://stjohnrestaurant.com/a/restaurants/smithfield) |
| 5 | [Hawksmoor St Pancras](https://thehawksmoor.com/locations/st-pancras/) | Chop/steak | King's Cross | 8 | 9 | 9 | 10 | **8.75** | yes | [book](https://thehawksmoor.com/book-a-table/?location=450966) |
| 6 | [Savoy Grill](https://www.thesavoylondon.com/restaurants-and-bars/savoy-grill) | Chop/steak | Strand | 8 | 10 | 8 | 9 | **8.65** | yes | [book](https://www.opentable.co.uk/r/savoy-grill-gordon-ramsay-london) |
| 7 | [Simpson's in the Strand](https://www.simpsonsinthestrand.co.uk/) | Fine dining | Strand | 7 | 10 | 9 | 10 | **8.6** | yes | [book](https://www.sevenrooms.com/explore/granddivan/reservations/create/search) |
| 8 | [Hawksmoor Seven Dials](https://thehawksmoor.com/locations/seven-dials/) | Chop/steak | Covent Garden | 8 | 8 | 9 | 10 | **8.5** | yes | [book](https://thehawksmoor.com/book-a-table/?location=45565) |
| 9 | [Hawksmoor Guildhall](https://thehawksmoor.com/locations/guildhall/) | Chop/steak | City | 8 | 8 | 9 | 10 | **8.5** | yes | [book](https://thehawksmoor.com/book-a-table/?location=71086) |
| 10 | [Quality Chop House](https://thequalitychophouse.com/) | Chop/steak | Farringdon | 8 | 10 | 7 | 9 | **8.45** | yes | [book](https://www.opentable.co.uk/the-quality-chop-house-reservations-london?restref=96150) |
| 11 | [Rules](https://rules.co.uk/) | Fine dining | Covent Garden | 7 | 10 | 9 | 9 | **8.45** | yes | [book](https://www.sevenrooms.com/reservations/rules) |
| 12 | [Wiltons](https://wiltons.co.uk/) | Fine dining | St James's | 8 | 10 | 8 | 7 | **8.35** | yes | [book](https://www.sevenrooms.com/reservations/wiltons) |
| 13 | [The Ritz Restaurant](https://www.theritzlondon.com/dine-with-us/the-ritz-restaurant/) | Fine dining | Piccadilly | 9 | 10 | 6 | 7 | **8.35** | check | [book](https://www.sevenrooms.com/explore/theritzrestaurant/reservations/create/search) |
| 14 | [Ibai](https://ibai.london/) | Chop/steak | Farringdon | 9 | 8 | 6 | 10 | **8.3** | check | [book](https://www.sevenrooms.com/landing/ibailondon) |
| 15 | [Brat](https://bratrestaurant.co.uk/redchurch-st) | Chop/steak | Shoreditch | 10 | 8 | 5 | 8 | **8.2** | check | [book](https://www.sevenrooms.com/reservations/bratshoreditch) |
| 16 | [Boisdale of Belgravia](https://www.boisdale.co.uk/restaurant/belgravia) | Fine dining | Belgravia | 7 | 9 | 9 | 9 | **8.2** | yes | ⚠️ phone/email |
| 17 | [Kerridge's Bar & Grill](https://www.corinthia.com/en-gb/london/kerridges/) | Fine dining | Whitehall | 8 | 8 | 8 | 9 | **8.15** | yes | [book](https://www.sevenrooms.com/explore/kerridgesatcorinthia/reservations/create/search/) |
| 18 | [Goodman Mayfair](https://www.goodmanrestaurants.com/mayfair) | Chop/steak | Mayfair | 8 | 7 | 8 | 10 | **8.05** | yes | [book](https://www.sevenrooms.com/explore/goodmanmayfair/reservations/create/search) |
| 19 | [Goodman City](https://www.goodmanrestaurants.com/city) | Chop/steak | City | 8 | 7 | 8 | 10 | **8.05** | yes | [book](https://www.sevenrooms.com/reservations/goodmancity) |
| 20 | [Holborn Dining Room](https://holborndiningroom.com/) | Chop/steak | Holborn | 8 | 8 | 8 | 8 | **8.0** | yes | [book](https://www.sevenrooms.com/reservations/rwldnholborndiningroom) |
| 21 | [Mountain](https://mountainbeakstreet.com/) | Chop/steak | Soho | 9 | 8 | 6 | 8 | **8.0** | check | [book](https://www.sevenrooms.com/reservations/mountain) |
| 22 | [Kitty Fisher's](https://www.kittyfishers.com/) | Chop/steak | Mayfair | 8 | 8 | 7 | 9 | **7.95** | yes | [book](https://www.sevenrooms.com/reservations/kittyfishers) |
| 23 | [Bentley's Oyster Bar & Grill](https://www.bentleys.org/) | Fine dining | Piccadilly | 8 | 9 | 8 | 6 | **7.95** | yes | [book](https://www.sevenrooms.com/explore/bentleys/reservations/create/search/) |
| 24 | [Charlie's at Brown's](https://www.roccofortehotels.com/hotels-and-resorts/brown-s-hotel/dining/charlies-at-browns/) | Fine dining | Mayfair | 8 | 9 | 6 | 8 | **7.85** | check | [book](https://www.roccofortehotels.com/hotels-and-resorts/brown-s-hotel/dining/charlies-at-browns/) |
| 25 | [Scott's](https://scotts-mayfair.com/) | Fine dining | Mayfair | 8 | 9 | 8 | 5 | **7.8** | yes | [book](https://scotts_mayfair.capricebookings.com/) |
| 26 | [J. Sheekey](https://j-sheekey.co.uk/) | Fine dining | Covent Garden | 8 | 9 | 8 | 5 | **7.8** | yes | [book](https://www.opentable.co.uk/j-sheekey-the-restaurant-reservations-london?restref=111285) |
| 27 | [Arlington](https://www.arlington.london/) | Fine dining | St James's | 7 | 9 | 8 | 6 | **7.55** | yes | [book](https://www.sevenrooms.com/reservations/arlingtonrestaurant) |
| 28 | [Blacklock City](https://theblacklock.com/restaurants/city/) | Chop/steak | City | 7 | 7 | 7 | 10 | **7.45** | check | [book](https://theblacklock.com/city-reservations/) |
| 29 | [Blacklock Soho](https://theblacklock.com/restaurants/blacklock-soho/) | Chop/steak | Soho | 7 | 7 | 6 | 10 | **7.25** | check | [book](https://theblacklock.com/soho-reservations/) |
| 30 | [Sweetings](http://www.sweetingsrestaurant.co.uk/) | Fine dining | City | 7 | 10 | 3 | 4 | **6.5** | check | ⚠️ phone/email |

Split: 18 chop/steak, 12 fine dining.

## Trading status: every venue

| Venue | Type | Status | Checked | Evidence | Nearby (m) |
|---|---|---|---|---|---|
| The Guinea Grill | Chop/steak | trading | 2026-10-03 | [source](https://www.theguinea.co.uk/) | The Audley 490, Red Lion 674, Donovan Bar 302, Connaught Bar 372 |
| Lutyens Grill | Chop/steak | trading | 2026-10-03 | [source](https://www.thened.com/london/restaurants/lutyens-grill) | Jamaica Wine House 326, Lamb Tavern 478, The Nickel Bar 0 |
| The Devonshire | Chop/steak | trading | 2026-10-03 | [source](https://www.devonshiresoho.co.uk/) | Red Lion 265, The French House 341, Donovan Bar 504, Bar Termini Soho 510 |
| St. JOHN Smithfield | Chop/steak | trading | 2026-10-03 | [source](https://stjohnrestaurant.com/a/restaurants/smithfield) | Fox & Anchor 43, Ye Olde Mitre 479, The Parlour at The Zetter 345, Tayēr + Elementary 843 |
| Hawksmoor St Pancras | Chop/steak | trading | 2026-10-03 | [source](https://thehawksmoor.com/locations/st-pancras/) | Euston Tap 576, Booking Office 1869 23 |
| Savoy Grill | Chop/steak | trading | 2026-10-03 | [source](https://www.thesavoylondon.com/restaurants-and-bars/savoy-grill) | The Harp 383, Lamb & Flag 400, American Bar at The Savoy 0, Bar Termini Soho 753 |
| Simpson's in the Strand | Fine dining | trading | 2026-10-03 | [source](https://www.simpsonsinthestrand.co.uk/reservations/) | Lamb & Flag 374, The Harp 382, American Bar at The Savoy 43, Bar Termini Soho 724 |
| Hawksmoor Seven Dials | Chop/steak | trading | 2026-10-03 | [source](https://thehawksmoor.com/locations/seven-dials/) | Lamb & Flag 195, The Salisbury 294, Bar Termini Soho 280, Three Sheets Soho 389 |
| Hawksmoor Guildhall | Chop/steak | trading | 2026-10-03 | [source](https://thehawksmoor.com/locations/guildhall/) | Jamaica Wine House 474, Lamb Tavern 607, The Nickel Bar 208 |
| Quality Chop House | Chop/steak | trading | 2026-10-03 | [source](https://thequalitychophouse.com/) | The Lamb 649, Cittie of Yorke 722, The Parlour at The Zetter 464 |
| Rules | Fine dining | trading | 2026-10-03 | [source](https://rules.co.uk/) | Lamb & Flag 198, The Harp 233, American Bar at The Savoy 201, Bar Termini Soho 554 |
| Wiltons | Fine dining | trading | 2026-10-03 | [source](https://wiltons.co.uk/) | Red Lion 208, The French House 763, Rivoli Bar 163, Dukes Bar 249 |
| The Ritz Restaurant | Fine dining | trading | 2026-10-03 | [source](https://www.theritzlondon.com/dine-with-us/the-ritz-restaurant/) | Red Lion 371, The Audley 759, Rivoli Bar 0, Donovan Bar 216 |
| Ibai | Chop/steak | trading | 2026-10-03 | [source](https://www.timeout.com/london/news/9-london-steak-restaurants-have-been-named-in-the-101-best-in-the-world-for-2026-040126) | Fox & Anchor 264, Ye Olde Mitre 547, The Parlour at The Zetter 630, The Nickel Bar 819 |
| Brat | Chop/steak | trading | 2026-10-03 | [source](https://guide.michelin.com/mt/en/greater-london/london/restaurant/brat) | Pride of Spitalfields 704, Seed Library 158 |
| Boisdale of Belgravia | Fine dining | trading | 2026-10-03 | [source](https://www.boisdale.co.uk/restaurant/belgravia) | Star Tavern 703, The Cocktail Bar at The Goring 409 |
| Kerridge's Bar & Grill | Fine dining | trading | 2026-10-03 | [source](https://www.corinthia.com/en-gb/london/kerridges/) | The Harp 375, The Salisbury 541, American Bar at The Savoy 463 |
| Goodman Mayfair | Chop/steak | trading | 2026-10-03 | [source](https://www.goodmanrestaurants.com/mayfair) | Red Lion 664, Dog & Duck 695, Donovan Bar 461, Connaught Bar 665 |
| Goodman City | Chop/steak | trading | 2026-10-03 | [source](https://www.goodmanrestaurants.com/city) | Jamaica Wine House 389, Lamb Tavern 538, The Nickel Bar 73 |
| Holborn Dining Room | Chop/steak | trading | 2026-10-03 | [source](https://www.rosewoodhotels.com/en/london/dining/holborn-dining-room) | Cittie of Yorke 394, The Lamb 632, Scarfes Bar 0, American Bar at The Savoy 825 |
| Mountain | Chop/steak | trading | 2026-10-03 | [source](https://mountainbeakstreet.com/) | Red Lion 423, The French House 456, Donovan Bar 422, Rivoli Bar 575 |
| Kitty Fisher's | Chop/steak | trading | 2026-10-03 | [source](https://www.kittyfishers.com/) | The Audley 508, Red Lion 713, Rivoli Bar 342, Donovan Bar 401 |
| Bentley's Oyster Bar & Grill | Fine dining | trading | 2026-10-03 | [source](https://www.bentleys.org/) | Red Lion 157, The French House 549, Donovan Bar 312, Rivoli Bar 363 |
| Charlie's at Brown's | Fine dining | trading | 2026-10-03 | [source](https://www.roccofortehotels.com/hotels-and-resorts/brown-s-hotel/dining/charlies-at-browns/) | Red Lion 408, The Audley 661, Donovan Bar 0, Rivoli Bar 216 |
| Scott's | Fine dining | trading | 2026-10-03 | [source](https://scotts-mayfair.com/) | The Audley 58, Connaught Bar 64, Donovan Bar 611 |
| J. Sheekey | Fine dining | trading | 2026-10-03 | [source](https://j-sheekey.co.uk/) | The Salisbury 38, Lamb & Flag 162, Bar Termini Soho 337, Three Sheets Soho 482 |
| Arlington | Fine dining | trading | 2026-10-03 | [source](https://www.arlington.london/) | Red Lion 353, The Audley 848, Rivoli Bar 101, Dukes Bar 136 |
| Blacklock City | Chop/steak | trading | 2026-10-03 | [source](https://theblacklock.com/restaurants/city/) | Lamb Tavern 228, Jamaica Wine House 244, The Nickel Bar 517 |
| Blacklock Soho | Chop/steak | trading | 2026-10-03 | [source](https://theblacklock.com/restaurants/blacklock-soho/) | The French House 228, Dog & Duck 309, Bar Termini Soho 396, Three Sheets Soho 417 |
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

## Caveats

- Michelin star counts are not quoted. Sources disagreed (e.g. Brat), so venues are just described as 'Michelin-starred'.
- `group_notes` come from each venue's own site on the check date. Treat them as prompts to call, not as fact.
- Sweetings is lunch-only and takes no bookings, so it is a weekday-lunch option, not a group dinner.
- Distances are straight-line. Walking routes are 10-30% longer.
