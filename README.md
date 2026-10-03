# London Lads' Dinner Map

An interactive map of 30 London chop houses and traditional fine-dining rooms, each paired with strong pubs and cocktail bars within about 10 minutes' walk. Tap any venue for its website, booking link, directions, group notes and what's nearby.

**Open it:** `index.html` works straight from disk, because the data is inlined. Once deployed, use the GitHub Pages URL.

| File | Purpose |
|---|---|
| `index.html` | The map: Leaflet 1.9.4 + markercluster 1.5.3 (pinned, from cdnjs with SRI), greyscale OpenStreetMap tiles, Google Fonts (IM Fell English, EB Garamond), vanilla JS. Venue data is inlined. |
| `data/venues.json` | Single source of truth: every venue, its scores, nearby links and verification evidence. Generated, so don't hand-edit it. |
| `VERIFICATION.md` | Trading status, evidence links, scoring table and exclusions. Generated. |
| `scripts/build_venues.py` | The verified venue records. Edit this file, then rebuild. |
| `scripts/write_verification.py` | Regenerates `VERIFICATION.md` from the JSON. |
| `scripts/build_site.py` | Inlines `data/venues.json` into `index.html`. |
| `scripts/check_links.py` | HEAD/GET-checks every URL and logs 4xx/5xx. Exit code 1 if anything is broken. |
| `PLAN.md` | The original brief. |

## Using the map

- **Filters:** category chips, *Highlights only*, *Groups of 8+*, and price bands. Price and group filters apply to restaurants only.
- **Markers:** red for chop/steak, navy for fine dining, amber for pubs (labelled "Taverns"), purple for cocktail bars. A gold star marks a highlight, and grey means trading status is uncertain.
- **Pop-up:** Website, Book and Directions buttons all open in a new tab. Missing links are shown as dashed ⚠️ buttons instead of guessed ones. Tap a venue under *Nearby* to jump to it.
- **List view:** a sortable table of the 30 restaurants for planning without the map.
- **Charter:** the third toggle sets out why the selection rules are what they are (scoring weights, tavern and bar criteria, the ten-minute walk, the verification rules, and who was struck off). Its counts and date are filled in from the data.
- **Landmarks:** St Paul's, Smithfield, Leadenhall and others are lettered on the map from zoom 14 for orientation. Their coordinates (from OSM Nominatim) are in the `LANDMARKS` constant in `index.html`.
- **Deep links:** `index.html#rules` opens that venue directly, which is handy for sharing in the group chat. `#charter` opens the Charter.

## Refreshing the data

Trading status goes stale. Re-verify before any real booking.

1. Re-check each venue (official site, plus one independent source such as the Hot Dinners closures tracker, Time Out or CAMRA WhatPub) and update its record in `scripts/build_venues.py`. Bump `TODAY`.
2. **Never invent a URL, address or coordinate.** If one can't be confirmed, use `""` and set the status to `"uncertain"`. The UI flags both.
3. Rebuild and check:
   ```bash
   python3 scripts/build_venues.py && python3 scripts/write_verification.py && python3 scripts/build_site.py && python3 scripts/check_links.py
   ```
   OpenTable, SevenRooms, Caprice and Nicholson's block scripted requests. They're reported as `BLOCKED`, not `BROKEN`, so open those links in a browser by hand.
4. New coordinates: take them from CAMRA WhatPub for pubs, or from the OSM Nominatim search for others. Keep to 1 request per second with a descriptive User-Agent, and spot-check the result by hand.

## Deploying to GitHub Pages

No build step and no secrets.

1. Push the repo to GitHub. A public repo gets Pages on any plan; Pages from a private repo needs GitHub Pro, Team or Enterprise.
2. **Settings → Pages → Build and deployment →** Source: *Deploy from a branch*, Branch: `main`, folder `/ (root)`.
3. The site appears at `https://<user>.github.io/<repo>/` within a minute or two.

To preview locally: `python3 -m http.server 8765`, then open http://localhost:8765.

## Known limitations

- Group policies (minimum spends, set menus for 8+, deposits) change often. `group_notes` are prompts to call the venue, not facts.
- Scores are editorial judgement (see `VERIFICATION.md`), not a published rating.
- Distances are straight-line. Real walks are about 25% longer, and the walking times shown allow for that.
- OSM tiles are fine at personal scale. For heavy traffic, switch to a commercial tile provider per the [OSM tile usage policy](https://operations.osmfoundation.org/policies/tiles/).
