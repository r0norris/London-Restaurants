#!/usr/bin/env python3
"""Build data/venues.json from the verified records below.

Every URL, address and coordinate here was checked on 2026-10-03 (see VERIFICATION.md).
Coordinates: pubs from CAMRA WhatPub; restaurants and bars from OSM Nominatim.
Empty strings mean "could not be confirmed" -- never fill them with a guess.
"""
import json, math, pathlib

TODAY = "2026-10-03"
NEARBY_M = 850  # ~10 minutes' walk
ROOT = pathlib.Path(__file__).resolve().parent.parent
HD_CLOSURES = "https://www.hot-dinners.com/202303199148/Gastroblog/Latest-news/recent-restaurant-closures-shut-london"

# id, name, category, area, address, lat, lng, website, booking_url, price, group8, group_notes, why, evidence_url, score
# score = (food, character, group, meat) each /10 -- editorial judgement, see VERIFICATION.md
R = [
 # ---- chop / steak / grill ----
 ("quality-chop-house","Quality Chop House","chop","Farringdon","94 Farringdon Road, London EC1R 3EA",51.5247707,-0.1100541,
  "https://thequalitychophouse.com/","https://www.opentable.co.uk/the-quality-chop-house-reservations-london?restref=96150","£££",True,
  "Has a private room (see site). Check capacity and set-menu terms.","Victorian working-class chop house (since 1869) with a famous confit potato and big sharing cuts.",
  "https://thequalitychophouse.com/",(8,10,7,9)),
 ("st-john-smithfield","St. JOHN Smithfield","chop","Smithfield","26 St John Street, London EC1M 4AY",51.5204809,-0.1012748,
  "https://stjohnrestaurant.com/a/restaurants/smithfield","https://stjohnrestaurant.com/a/restaurants/smithfield","£££",True,
  "Private events offered (see /pages/private-events). Large-format feasts for groups are worth asking about.","Fergus Henderson's nose-to-tail temple; roast bone marrow and parsley salad is mandatory.",
  "https://stjohnrestaurant.com/a/restaurants/smithfield",(9,9,7,10)),
 ("ibai","Ibai","chop","Farringdon","92 Bartholomew Close, London EC1A 7BN",51.5181623,-0.0994888,
  "https://ibai.london/","https://www.sevenrooms.com/landing/ibailondon","££££",False,
  "Group policy not stated online. Check with the venue.","Basque grill house, ranked No. 7 in the World's 101 Best Steak Restaurants 2026 and Time Out's top London steak.",
  "https://www.timeout.com/london/news/9-london-steak-restaurants-have-been-named-in-the-101-best-in-the-world-for-2026-040126",(9,8,6,10)),
 ("hawksmoor-seven-dials","Hawksmoor Seven Dials","chop","Covent Garden","11 Langley Street, London WC2H 9JG",51.5134572,-0.1257487,
  "https://thehawksmoor.com/locations/seven-dials/","https://thehawksmoor.com/book-a-table/?location=45565","££££",True,
  "Private dining rooms bookable via the Hawksmoor private-dining page.","Flagship-feel Hawksmoor in a former brewery, with a strong bar for pre-dinner martinis.",
  "https://thehawksmoor.com/locations/seven-dials/",(8,8,9,10)),
 ("hawksmoor-guildhall","Hawksmoor Guildhall","chop","City","10 Basinghall Street, London EC2V 5BQ",51.5155147,-0.0909278,
  "https://thehawksmoor.com/locations/guildhall/","https://thehawksmoor.com/book-a-table/?location=71086","££££",True,
  "Dedicated Guildhall private-dining rooms.","City Hawksmoor with dark-wood booths, built for long business dinners.",
  "https://thehawksmoor.com/locations/guildhall/",(8,8,9,10)),
 ("hawksmoor-st-pancras","Hawksmoor St Pancras","chop","King's Cross","St Pancras London, Euston Road, London NW1 2AR",51.529901,-0.1258012,
  "https://thehawksmoor.com/locations/st-pancras/","https://thehawksmoor.com/book-a-table/?location=450966","££££",True,
  "Dedicated St Pancras private-dining page.","Newest Hawksmoor (opened late 2025) in the Gothic St Pancras hotel. The highest-ranked Hawksmoor in the 2026 World's 101 Best Steak list.",
  "https://thehawksmoor.com/locations/st-pancras/",(8,9,9,10)),
 ("blacklock-soho","Blacklock Soho","chop","Soho","24 Great Windmill Street, London W1D 7LG",51.5117726,-0.1346407,
  "https://theblacklock.com/restaurants/blacklock-soho/","https://theblacklock.com/soho-reservations/","££",False,
  "Group policy not stated online. Ask about 'All In' sharing for big tables.","Basement chop house: piles of skinny chops on toast at sane prices.",
  "https://theblacklock.com/restaurants/blacklock-soho/",(7,7,6,10)),
 ("blacklock-city","Blacklock City","chop","City","13 Philpot Lane, London EC3M 8AA",51.5108697,-0.0841331,
  "https://theblacklock.com/restaurants/city/","https://theblacklock.com/city-reservations/","££",False,
  "Group policy not stated online. Email cityreservations@theblacklock.com.","Bigger City Blacklock in an old bank vault, with the same chops and a Sunday roast that has a cult following.",
  "https://theblacklock.com/restaurants/city/",(7,7,7,10)),
 ("brat","Brat","chop","Shoreditch","First floor, 4 Redchurch Street, London E1 6JL",51.5242656,-0.0766909,
  "https://bratrestaurant.co.uk/redchurch-st","https://www.sevenrooms.com/reservations/bratshoreditch","£££",False,
  "Small room, online booking only. Book 6-8 weeks ahead for weekends and pre-order the whole turbot.","Tomos Parry's Michelin-starred wood-fire grill. No. 17 in the World's 101 Best Steak Restaurants 2026.",
  "https://guide.michelin.com/mt/en/greater-london/london/restaurant/brat",(10,8,5,8)),
 ("guinea-grill","The Guinea Grill","chop","Mayfair","30 Bruton Place, London W1J 6NL",51.5111247,-0.1450479,
  "https://www.theguinea.co.uk/","","£££",True,
  "Three private rooms: Gallery (10), Wine Room (14), Boardroom (20). Book by phone or email (020 7409 1728).","Mayfair pub-steakhouse with award-winning steak and kidney pies and a proper bar at the front.",
  "https://www.theguinea.co.uk/",(8,10,9,10)),
 ("goodman-mayfair","Goodman Mayfair","chop","Mayfair","24-26 Maddox Street, London W1S 1QH",51.5132239,-0.1419269,
  "https://www.goodmanrestaurants.com/mayfair","https://www.sevenrooms.com/explore/goodmanmayfair/reservations/create/search","££££",True,
  "Private dining offered (goodmanrestaurants.com/private-dining).","New York-style steakhouse with in-house dry-ageing and a serious red wine list.",
  "https://www.goodmanrestaurants.com/mayfair",(8,7,8,10)),
 ("goodman-city","Goodman City","chop","City","11 Old Jewry, London EC2R 8DU",51.5142317,-0.0907172,
  "https://www.goodmanrestaurants.com/city","https://www.sevenrooms.com/reservations/goodmancity","££££",True,
  "Private dining offered (goodmanrestaurants.com/private-dining).","City outpost of Goodman: same dry-aged beef, built for expense-account tables.",
  "https://www.goodmanrestaurants.com/city",(8,7,8,10)),
 ("lutyens-grill","Lutyens Grill","chop","City","The Ned, 27 Poultry, London EC2R 8AJ",51.5137266,-0.090038,
  "https://www.thened.com/london/restaurants/lutyens-grill","https://www.thened.com/london/restaurants/lutyens-grill","££££",True,
  "Parties of 7+ can book online. Unlimited prime rib on Fridays and Sundays. Open to non-members.","Wood-panelled former bank manager's office with trolley carving. No. 35 in the World's 101 Best Steak Restaurants.",
  "https://www.thened.com/london/restaurants/lutyens-grill",(8,10,8,10)),
 ("the-devonshire","The Devonshire","chop","Soho","17 Denman Street, London W1D 7HW",51.5106407,-0.1353307,
  "https://www.devonshiresoho.co.uk/","https://onsass.designmynight.com/?background-color=%2334533b&primary-color=%23ffffff&body-text-color=%23ffffff&outer-border-color=white","£££",True,
  "Private events: privateevents@devonshiresoho.co.uk (events brochure on site).","London's hottest pub-grill: perfect Guinness downstairs and a wood-fired grill room upstairs. No. 45 in the World's 101 Best Steak Restaurants.",
  "https://www.devonshiresoho.co.uk/",(9,9,8,9)),
 ("holborn-dining-room","Holborn Dining Room","chop","Holborn","Rosewood London, 252 High Holborn, London WC1V 7EN",51.5174168,-0.1182219,
  "https://holborndiningroom.com/","https://www.sevenrooms.com/reservations/rwldnholborndiningroom","£££",True,
  "Rosewood London offers group bookings and event spaces. Ask about the private dining room.","Grand British brasserie famous for its pies and Scotch eggs. Scarfes Bar is across the courtyard.",
  "https://www.rosewoodhotels.com/en/london/dining/holborn-dining-room",(8,8,8,8)),
 ("kitty-fishers","Kitty Fisher's","chop","Mayfair","10 Shepherd Market, London W1J 7QF",51.5065224,-0.146262,
  "https://www.kittyfishers.com/","https://www.sevenrooms.com/reservations/kittyfishers","£££",True,
  "Private hire offered (/private-hire).","Cosy, clubby Shepherd Market wood-grill room known for aged beef.",
  "https://www.kittyfishers.com/",(8,8,7,9)),
 ("savoy-grill","Savoy Grill","chop","Strand","The Savoy, Strand, London WC2R 0EU",51.5101273,-0.1204993,
  "https://www.thesavoylondon.com/restaurants-and-bars/savoy-grill","https://www.opentable.co.uk/r/savoy-grill-gordon-ramsay-london","££££",True,
  "Private dining and events page run by Gordon Ramsay Restaurants. Ask about the beef Wellington masterclass.","Art-deco grill room serving beef Wellington and trolley classics, with the American Bar upstairs.",
  "https://www.thesavoylondon.com/restaurants-and-bars/savoy-grill",(8,10,8,9)),
 ("mountain","Mountain","chop","Soho","16-18 Beak Street, London W1F 9RD",51.5119723,-0.1382219,
  "https://mountainbeakstreet.com/","https://www.sevenrooms.com/reservations/mountain","£££",False,
  "Group policy not stated online. Email bookings@mountainbeakstreet.com.","Tomos Parry's Soho follow-up to Brat: open-fire Welsh/Spanish cooking and big-ticket shared cuts.",
  "https://mountainbeakstreet.com/",(9,8,6,8)),
 # ---- traditional fine dining ----
 ("rules","Rules","fine_dining","Covent Garden","34-35 Maiden Lane, London WC2E 7LB",51.5108285,-0.1231906,
  "https://rules.co.uk/","https://www.sevenrooms.com/reservations/rules","£££",True,
  "Private rooms: the Graham Greene Room and the John Betjeman Room.","London's oldest restaurant (1798): game from its own estate, pies and puddings in a room full of antlers.",
  "https://rules.co.uk/",(7,10,9,9)),
 ("wiltons","Wiltons","fine_dining","St James's","55 Jermyn Street, London SW1Y 6LX",51.5076994,-0.1392041,
  "https://wiltons.co.uk/","https://www.sevenrooms.com/reservations/wiltons","££££",True,
  "Private dining offered (/private-dining). Jacket is the expected dress.","Since 1742. The grandest old-school fish and game house in St James's.",
  "https://wiltons.co.uk/",(8,10,8,7)),
 ("ritz-restaurant","The Ritz Restaurant","fine_dining","Piccadilly","The Ritz, 150 Piccadilly, London W1J 9BR",51.5071911,-0.1414246,
  "https://www.theritzlondon.com/dine-with-us/the-ritz-restaurant/","https://www.sevenrooms.com/explore/theritzrestaurant/reservations/create/search","££££",False,
  "Strict dress code (jacket and tie). Ask the hotel about private dining for 8+.","The most opulent dining room in London, with Michelin-starred classical cooking and tableside carving.",
  "https://www.theritzlondon.com/dine-with-us/the-ritz-restaurant/",(9,10,6,7)),
 ("simpsons-in-the-strand","Simpson's in the Strand","fine_dining","Strand","100 Strand, London WC2R 0EZ",51.5105048,-0.1206359,
  "https://www.simpsonsinthestrand.co.uk/","https://www.sevenrooms.com/explore/granddivan/reservations/create/search","£££",True,
  "Grand Divan (classic) and Romano's (relaxed). Large private ballroom.","Reopened in March 2026 by Jeremy King. Roast-beef trolleys carved at the table in the Grand Divan.",
  "https://www.simpsonsinthestrand.co.uk/reservations/",(7,10,9,10)),
 ("scotts","Scott's","fine_dining","Mayfair","20 Mount Street, London W1K 2HE",51.5098163,-0.1509327,
  "https://scotts-mayfair.com/","https://scotts_mayfair.capricebookings.com/","££££",True,
  "Private dining offered (/private-dining-at-scotts/). Booking page: card required, £50pp deposit for 4+.","Glamorous Mayfair seafood institution with an oyster bar at its heart.",
  "https://scotts-mayfair.com/",(8,9,8,5)),
 ("bentleys","Bentley's Oyster Bar & Grill","fine_dining","Piccadilly","11-15 Swallow Street, London W1B 4DG",51.5094977,-0.1377087,
  "https://www.bentleys.org/","https://www.sevenrooms.com/explore/bentleys/reservations/create/search/","£££",True,
  "Private dining and events offered (/private-dining-events).","Since 1916: Richard Corrigan's oyster bar and upstairs grill.",
  "https://www.bentleys.org/",(8,9,8,6)),
 ("j-sheekey","J. Sheekey","fine_dining","Covent Garden","28-32 St Martin's Court, London WC2N 4AL",51.5109233,-0.1276968,
  "https://j-sheekey.co.uk/","https://www.opentable.co.uk/j-sheekey-the-restaurant-reservations-london?restref=111285","£££",True,
  "Private dining offered (/private-dining-events-at-j-sheekey/).","Theatreland fish institution. The fish pie is the order.",
  "https://j-sheekey.co.uk/",(8,9,8,5)),
 ("sweetings","Sweetings","fine_dining","City","39 Queen Victoria Street, London EC4N 4SF",51.512397,-0.0927667,
  "http://www.sweetingsrestaurant.co.uk/","","£££",False,
  "Lunch only, Mon-Fri 11:30-15:00. No reservations: arrive before noon. Not suitable for a booked group dinner.","Fish restaurant in the City since 1889. Black Velvet in tankards and counter seating.",
  "https://www.cityam.com/a-love-letter-to-sweetings-the-citys-oldest-restaurant/",(7,10,3,4)),
 ("charlies-browns","Charlie's at Brown's","fine_dining","Mayfair","Brown's Hotel, Albemarle Street, London W1S 4BP",51.5090781,-0.1421697,
  "https://www.roccofortehotels.com/hotels-and-resorts/brown-s-hotel/dining/charlies-at-browns/","https://www.roccofortehotels.com/hotels-and-resorts/brown-s-hotel/dining/charlies-at-browns/","££££",False,
  "Book via the widget on the hotel page or reservations.browns@roccofortehotels.com. Ask about group menus.","Adam Byatt's trolley-service British dining room, with the Donovan Bar next door.",
  "https://www.roccofortehotels.com/hotels-and-resorts/brown-s-hotel/dining/charlies-at-browns/",(8,9,6,8)),
 ("arlington","Arlington","fine_dining","St James's","Arlington House, 20 Arlington Street, London SW1A 1RJ",51.5064801,-0.140511,
  "https://www.arlington.london/","https://www.sevenrooms.com/reservations/arlingtonrestaurant","£££",True,
  "Private events offered (/private-events/).","Jeremy King's revival of the old Le Caprice room. Polished, buzzy, with live piano at night.",
  "https://www.arlington.london/",(7,9,8,6)),
 ("kerridges","Kerridge's Bar & Grill","fine_dining","Whitehall","Corinthia London, 10 Northumberland Avenue, London WC2N 5AE",51.5065322,-0.1238974,
  "https://www.corinthia.com/en-gb/london/kerridges/","https://www.sevenrooms.com/explore/kerridgesatcorinthia/reservations/create/search/","££££",True,
  "Corinthia meetings and events team handles groups.","Tom Kerridge's grand British grill room: rotisserie, pies and a big bar.",
  "https://www.corinthia.com/en-gb/london/kerridges/",(8,8,8,9)),
 ("boisdale-belgravia","Boisdale of Belgravia","fine_dining","Belgravia","15 Eccleston Street, London SW1W 9LX",51.4943218,-0.1481672,
  "https://www.boisdale.co.uk/restaurant/belgravia","","£££",True,
  "Private dining rooms and published group menus. Book by phone (020 7730 6922) or reservations@boisdale.co.uk.","Scottish steak and whisky house with a cigar terrace and live music six nights a week.",
  "https://www.boisdale.co.uk/restaurant/belgravia",(7,9,9,9)),
]

# Pubs: id, name, area, address, lat, lng (CAMRA), website, highlight, why, evidence (CAMRA)
P = [
 ("ye-olde-mitre","Ye Olde Mitre","Hatton Garden","1 Ely Court, Ely Place, London EC1N 6SJ",51.518440199467,-0.107387347221,"https://www.yeoldemitreholborn.co.uk/",True,
  "Hidden 1546-founded tavern in an alley. CAMRA East London & City Pub of the Year 2025, nationally important interior.","https://camra.org.uk/pubs/olde-mitre-london-156323"),
 ("fox-and-anchor","Fox & Anchor","Smithfield","115 Charterhouse Street, London EC1M 6AA",51.520426255194,-0.100646830688,"https://www.foxandanchor.com/",False,
  "Art Nouveau Smithfield market pub with tiny snugs. CAMRA National Inventory (one star).","https://camra.org.uk/pubs/fox-anchor-london-156298"),
 ("cittie-of-yorke","Cittie of Yorke","Holborn","22 High Holborn, London WC1V 6BN",51.5185,-0.1128,"",True,
  "Vast mock-medieval hall with drinking booths and Sam Smith's prices. CAMRA National Inventory (three star).","https://camra.org.uk/pubs/cittie-of-yorke-london-125495"),
 ("the-lamb","The Lamb","Bloomsbury","94 Lamb's Conduit Street, London WC1N 3LZ",51.5230834,-0.1190469,"https://www.thelamblondon.com/",True,
  "Victorian snob screens intact. Young's cask. CAMRA National Inventory (one star).","https://camra.org.uk/pubs/lamb-london-125487"),
 ("ye-olde-cheshire-cheese","Ye Olde Cheshire Cheese","Fleet Street","145 Fleet Street, London EC4A 2BU",51.514360090815,-0.107158601189,"",True,
  "Rebuilt after the Great Fire of 1666. Warren of fire-lit rooms, Dickens's local. CAMRA National Inventory (three star).","https://camra.org.uk/pubs/olde-cheshire-cheese-london-156637"),
 ("black-friar","The Black Friar","Blackfriars","174 Queen Victoria Street, London EC4V 4EG",51.512112307297,-0.10371917791,"https://www.nicholsonspubs.co.uk/restaurants/london/theblackfriarblackfriarslondon",True,
  "Arts and Crafts marble-and-mosaic friars everywhere. CAMRA National Inventory (three star).","https://camra.org.uk/pubs/black-friar-london-156696"),
 ("jamaica-wine-house","Jamaica Wine House","Bank","St Michael's Alley, Cornhill, London EC3V 9DS",51.512893630619,-0.085519076057,"https://www.jamaicawinehouse.co.uk/",False,
  "Victorian 'Jampot' on the site of London's first coffee house. CAMRA National Inventory (three star).","https://camra.org.uk/pubs/jamaica-wine-house-london-156624"),
 ("lamb-tavern","Lamb Tavern","Leadenhall Market","10-12 Leadenhall Market, London EC3V 1LR",51.512848361683,-0.083267061342,"https://www.lambtavernleadenhall.com/",False,
  "Grade II* pub in the middle of Leadenhall Market. CAMRA National Inventory (one star).","https://camra.org.uk/pubs/lamb-tavern-london-156616"),
 ("the-harp","The Harp","Covent Garden","47 Chandos Place, London WC2N 4HS",51.509653,-0.125988,"https://www.harpcoventgarden.com/",True,
  "Narrow cask-ale shrine and former CAMRA National Pub of the Year.","https://camra.org.uk/pubs/harp-london-128660"),
 ("lamb-and-flag","Lamb & Flag","Covent Garden","33 Rose Street, London WC2E 9EB",51.5117,-0.1257,"https://www.lambandflagcoventgarden.co.uk/",False,
  "Timber-framed, licensed since 1623, once the 'Bucket of Blood'. CAMRA National Inventory (three star).","https://camra.org.uk/pubs/lamb-flag-london-128715"),
 ("the-salisbury","The Salisbury","Covent Garden","90 St Martin's Lane, London WC2N 4AP",51.51096,-0.127146,"",False,
  "Glittering 1898 gin-palace glass and Art Nouveau lamps. CAMRA National Inventory (three star).","https://camra.org.uk/pubs/salisbury-london-128829"),
 ("red-lion-st-james","Red Lion","St James's","2 Duke of York Street, London SW1Y 6JP",51.508344,-0.136379,"",True,
  "Tiny Victorian jewel box of etched and cut mirrors. CAMRA National Inventory.","https://camra.org.uk/pubs/red-lion-london-128701"),
 ("the-audley","The Audley","Mayfair","43 Mount Street, London W1K 2RX",51.509603,-0.151698,"https://theaudleypublichouse.com/",False,
  "Grade II 1889 Victorian pub revamped by Artfarm, with a Phyllida Barlow ceiling. Listed on CAMRA's Pub Heritage site; not National Inventory.","https://pubheritage.camra.org.uk/pubs/2131"),
 ("dog-and-duck","Dog & Duck","Soho","18 Bateman Street, London W1D 3AJ",51.514006828999,-0.131962338623,"https://www.nicholsonspubs.co.uk/restaurants/london/thedogandducksoholondon",False,
  "1897 tiles and mirrors, Orwell's Soho local. CAMRA National Inventory.","https://camra.org.uk/pubs/dog-duck-london-128663"),
 ("french-house","The French House","Soho","49 Dean Street, London W1D 5BG",51.512755085185,-0.131742915344,"https://www.frenchhousesoho.com/",True,
  "Soho's bohemian institution: half pints only, Ricard and wine. CAMRA National Inventory (two star). No cask ale.","https://camra.org.uk/pubs/french-house-london-129160"),
 ("euston-tap","Euston Tap","Euston","West & East Lodges, 190 Euston Road, London NW1 2EF",51.5269,-0.1326,"https://eustontap.com/",False,
  "Craft and cask house in the Grade II lodges of the old Euston Arch.","https://camra.org.uk/pubs/euston-tap-london-125165"),
 ("star-tavern","Star Tavern","Belgravia","6 Belgrave Mews West, London SW1X 8HT",51.498487,-0.155825,"https://www.star-tavern-belgravia.co.uk/",True,
  "Mews pub in every Good Beer Guide edition (45-year certificate, 2017). Reputedly where the Great Train Robbery was planned.","https://camra.org.uk/pubs/star-tavern-london-128650"),
 ("pride-of-spitalfields","Pride of Spitalfields","Spitalfields","3 Heneage Street, London E1 5LJ",51.51893633098,-0.071185195107,"",False,
  "Tiny no-frills free house off Brick Lane. Listed in the current Good Beer Guide per CAMRA WhatPub.","https://camra.org.uk/pubs/pride-of-spitalfields-london-155017"),
]

# Bars: id, name, area, address, lat, lng, website, booking_url, highlight, why, evidence
B = [
 ("connaught-bar","Connaught Bar","Mayfair","The Connaught, Carlos Place, London W1K 2AL",51.5101816,-0.1502153,
  "https://www.maybourne.com/en/hotels/the-connaught/restaurants-bars/connaught-bar","",True,
  "No. 6 in the World's 50 Best Bars 2025. Martini trolley theatre.","https://www.timeout.com/london/news/its-official-4-london-bars-are-in-the-50-best-in-the-world-right-now-100825"),
 ("scarfes-bar","Scarfes Bar","Holborn","Rosewood London, 252 High Holborn, London WC1V 7EN",51.5174168,-0.1182219,
  "https://www.rosewoodhotels.com/en/london/dining/scarfes-bar","",True,
  "World's 50 Best Bars No. 31 (2025) and No. 77 on the 2026 51-100 list. Library-bar armchairs and live jazz.","https://www.timeout.com/london/news/worlds-50-best-bars-2026-longlist-scarfes-three-sheets-soho-092326"),
 ("tayer-elementary","Tayēr + Elementary","Old Street","152 Old Street, London EC1V 9BW",51.5250193,-0.0915052,
  "https://tayer-elementary.com/","",True,
  "No. 5 in the World's 50 Best Bars 2025.","https://www.timeout.com/london/news/its-official-4-london-bars-are-in-the-50-best-in-the-world-right-now-100825"),
 ("three-sheets-soho","Three Sheets Soho","Soho","13 Manette Street, London W1D 4AP",51.5147523,-0.1309725,
  "https://www.threesheets-bar.com/","",False,
  "No. 73 on the World's 50 Best Bars 2026 51-100 list.","https://www.timeout.com/london/news/worlds-50-best-bars-2026-longlist-scarfes-three-sheets-soho-092326"),
 ("american-bar-savoy","American Bar at The Savoy","Strand","The Savoy, Strand, London WC2R 0EZ",51.5101273,-0.1204993,
  "https://www.thesavoylondon.com/restaurants-and-bars/american-bar","",True,
  "Oldest surviving cocktail bar in London and home of the Hanky Panky.","https://www.thesavoylondon.com/restaurants-and-bars/american-bar"),
 ("dukes-bar","Dukes Bar","St James's","Dukes Hotel, 35-36 St James's Place, London SW1A 1NY",51.5054602,-0.1394238,
  "https://www.dukeshotel.com/dukesbar.html","",True,
  "Ian Fleming's martini bar, mixed at your table. Two-drink limit.","https://www.dukeshotel.com/dukesbar.html"),
 ("donovan-bar","Donovan Bar","Mayfair","Brown's Hotel, Albemarle Street, London W1S 4BP",51.5090781,-0.1421697,
  "https://www.roccofortehotels.com/hotels-and-resorts/brown-s-hotel/dining/donovan-bar/","",False,
  "Classic Brown's Hotel cocktail bar lined with Terence Donovan photographs.","https://www.roccofortehotels.com/hotels-and-resorts/brown-s-hotel/dining/donovan-bar/"),
 ("rivoli-bar","Rivoli Bar","Piccadilly","The Ritz, 150 Piccadilly, London W1J 9BR",51.5071911,-0.1414246,
  "https://www.theritzlondon.com/dine-with-us/rivoli-bar/","https://www.sevenrooms.com/explore/therivolibar/reservations/create/search","",False,
  "Art-deco cocktail bar inside the Ritz.","https://www.theritzlondon.com/dine-with-us/rivoli-bar/"),
 ("bar-termini-soho","Bar Termini Soho","Soho","7 Old Compton Street, London W1D 5JE",51.5136688,-0.1297828,
  "https://bar-termini-soho.com/","",False,
  "Tony Conigliaro's tiny Italian espresso-and-negroni bar.","https://bar-termini-soho.com/"),
 ("zetter-parlour","The Parlour at The Zetter","Clerkenwell","The Zetter, St John's Square, London EC1M 4AJ",51.5231282,-0.1038808,
  "https://thezetter.com/clerkenwell/the-parlour/","","",False,
  "Eccentric Clerkenwell parlour bar, with live music on Tuesdays and Wednesdays.","https://thezetter.com/clerkenwell/the-parlour/"),
 ("booking-office-1869","Booking Office 1869","King's Cross","St Pancras London, Euston Road, London NW1 2AR",51.5301049,-0.125717,
  "https://www.booking-office.co.uk/","",False,
  "Cathedral-scale cocktail bar in the restored St Pancras ticket hall.","https://www.booking-office.co.uk/"),
 ("goring-bar","The Cocktail Bar at The Goring","Victoria","The Goring, 15 Beeston Place, London SW1W 0JW",51.4976151,-0.1455304,
  "https://www.thegoring.com/food-drink/the-goring-cocktail-bar/","",False,
  "Royal-warrant hotel bar, unchanged in the best way.","https://www.thegoring.com/food-drink/the-goring-cocktail-bar/"),
 ("nickel-bar","The Nickel Bar","City","The Ned, 27 Poultry, London EC2R 8AJ",51.5137266,-0.090038,
  "https://www.thened.com/london/restaurants/the-nickel-bar","",False,
  "American-style bar in the Ned's old banking hall, with live music every day.","https://www.thened.com/london/restaurants/the-nickel-bar"),
 ("seed-library","Seed Library","Shoreditch","One Hundred Shoreditch, 100 Shoreditch High Street, London E1 6JQ",51.5256536,-0.0772199,
  "https://www.onehundredshoreditch.com/eat-drink/seed-library/","https://www.sevenrooms.com/reservations/seedlibrary","",False,
  "Mr Lyan's lo-fi basement cocktail bar.","https://www.onehundredshoreditch.com/eat-drink/seed-library/"),
]

def hav(a, b):
    R_ = 6371000
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R_*math.asin(math.sqrt(h))

def score(s):
    f, c, g, m = s
    return round(0.40*f + 0.25*c + 0.20*g + 0.15*m, 2)

venues = []
for (i, n, cat, area, addr, lat, lng, web, book, price, g8, gn, why, ev, s) in R:
    venues.append(dict(id=i, name=n, category=cat, highlight=score(s) >= 8.5, area=area, address=addr,
        lat=lat, lng=lng, website=web, booking_url=book, price_band=price, groups_8plus=g8, group_notes=gn,
        why=why, nearby=[], status="trading", verified_on=TODAY, evidence_url=ev,
        score=dict(food=s[0], character=s[1], group=s[2], meat=s[3], total=score(s))))
for (i, n, area, addr, lat, lng, web, hl, why, ev) in P:
    venues.append(dict(id=i, name=n, category="pub", highlight=hl, area=area, address=addr, lat=lat, lng=lng,
        website=web, booking_url="", price_band="", group_notes="", why=why, nearby=[], status="trading",
        verified_on=TODAY, evidence_url=ev))
for (i, n, area, addr, lat, lng, web, book, *rest) in B:
    hl, why, ev = rest[-3:]  # some rows carry an extra "" placeholder before these
    venues.append(dict(id=i, name=n, category="cocktail_bar", highlight=hl,
        area=area, address=addr, lat=lat, lng=lng, website=web, booking_url=book, price_band="",
        group_notes="", why=why, nearby=[], status="trading", verified_on=TODAY, evidence_url=ev))

by = {v["id"]: v for v in venues}
problems = []
for v in venues:
    if v["category"] not in ("chop", "fine_dining"):
        continue
    here = (v["lat"], v["lng"])
    for cat, k in (("pub", 2), ("cocktail_bar", 2)):
        cands = sorted((hav(here, (o["lat"], o["lng"])), o["id"]) for o in venues if o["category"] == cat)
        pick = [oid for d, oid in cands if d <= NEARBY_M][:k]
        if not pick:
            d, oid = cands[0]
            problems.append(f"{v['id']}: no {cat} within {NEARBY_M} m (nearest {oid} at {int(d)} m)")
            pick = [oid]
        v["nearby"] += pick
    v["nearby_distances_m"] = {oid: int(hav(here, (by[oid]["lat"], by[oid]["lng"]))) for oid in v["nearby"]}

restaurants = [v for v in venues if v["category"] in ("chop", "fine_dining")]
assert len(restaurants) == 30, len(restaurants)
assert len({v["id"] for v in venues}) == len(venues)
out = dict(generated_on=TODAY, nearby_radius_m=NEARBY_M,
           secondary_check=dict(source="Hot Dinners closures tracker (2025-2026)", url=HD_CLOSURES, checked_on=TODAY,
                                result="None of the listed venues appear as closed."),
           venues=venues)
(ROOT/"data"/"venues.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
print(f"{len(restaurants)} restaurants, {sum(v['category']=='pub' for v in venues)} pubs, "
      f"{sum(v['category']=='cocktail_bar' for v in venues)} bars")
for p in problems:
    print("WARN", p)
for v in sorted(restaurants, key=lambda v: -v["score"]["total"]):
    print(f"{v['score']['total']:5.2f}  {v['category']:11} {v['name']:28} -> {', '.join(f'{k} {d}m' for k, d in v['nearby_distances_m'].items())}")
