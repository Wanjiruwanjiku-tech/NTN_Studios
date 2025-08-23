# Saint Rita - Daily tracker

- This is a simple daily tracker application for daily mental health checking inspired by Saint Rita.
- The application is built in three phases:

  1. __Phase 1__: This build path involves using pure HTML, CSS, and JS
  2. __Phase 2__: This build path will use React to build scalable, easy to extend components
  3. __Phase 3__: This phase will be built using Python

  ## Core MVP (Same for all stacks)

1. Daily Entry with fields from your worksheet: _date, affirmation, priority, actions.health, actions.voice, actions.growth, energy (high|medium|low), adjustment, nourish, challenge, release, weekNote_

2. Prayer: St. Rita short prayer on every page.

3. Persistence: save entries; load existing entries by date.

4. Export/Print: printer-friendly layout.

5. Extras you can add later: search, weekly overview, JSON export, login/sync.

### Phase 1 — HTML, CSS & JS (no framework)

- __Why?__
  - You want something simple, offline, and printable today.
  - You’re okay with local-only storage (later you can add sync).

- __Architecture__

  - index.html — form + list

  - styles.css — clean, print-friendly

  - app.js — state, validation, localStorage

  - manifest.json + service-worker.js — PWA (installable, offline)

- _Step-by-step_

  1. Scaffold files: index.html, styles.css, app.js, manifest.json, service-worker.js.

  2. Form first: get inputs working; bind “Save”.

  3. Local storage: localStorage["entries"] = JSON.stringify({...}).

  4. Load by date: on date change, fetch existing entry.

  5. Print styles: CSS @media print for a clean A4/Letter print.

  6. PWA: add manifest; register service worker; app works offline.