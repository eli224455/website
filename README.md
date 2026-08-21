# Elizabeth Tesfaye Law Office — website

A static, SEO-optimised website for a law office in Addis Ababa, Ethiopia.
No database, no server-side code, no build step required to host it — plain HTML,
CSS and a small amount of JavaScript. It will run on GitHub Pages or Cloudflare
Pages for free.

---

## Contents

1. [What's in the box](#whats-in-the-box)
2. [Publish on Cloudflare Pages](#publish-on-cloudflare-pages-recommended)
3. [Publish on GitHub Pages](#publish-on-github-pages)
4. [Connect your domain](#connect-your-domain)
5. [Editing content](#editing-content)
6. [Making the contact form actually send email](#making-the-contact-form-actually-send-email)
7. [SEO: what's already done, what you must do](#seo-whats-already-done-what-you-must-do)
8. [Adding an Amharic version later](#adding-an-amharic-version-later)

---

## What's in the box

**16 pages**, all written and populated:

| Page | URL |
|---|---|
| Home | `/` |
| About the firm | `/about/` |
| Practice areas (overview) | `/practice-areas/` |
| Family Law | `/family-law-addis-ababa/` |
| Civil Litigation | `/civil-litigation-ethiopia/` |
| Succession & Inheritance | `/succession-inheritance-ethiopia/` |
| Business & Corporate Law | `/business-corporate-law-addis-ababa/` |
| Criminal Law | `/criminal-defense-lawyer-addis-ababa/` |
| Legal Consultation | `/legal-consultation-ethiopia/` |
| FAQ (20 questions) | `/faq/` |
| Contact + map | `/contact/` |
| Legal Insights | `/insights/` |
| 3 starter articles | `/insights/…/` |
| Not-found page | `/404.html` |

Plus `sitemap.xml`, `robots.txt`, an Open Graph share image, and an SVG logo.

**Folder layout**

```
/                     ← the built website (this is what gets served)
  index.html
  about/index.html
  …
  assets/css/style.css
  assets/js/main.js
  assets/img/          logo, favicon, share image
  sitemap.xml
  robots.txt
  _headers             Cloudflare Pages: security + caching headers
  _redirects           Cloudflare Pages: short URLs like /divorce
  .nojekyll            GitHub Pages: serve files as-is

tools/                ← the source the pages are generated from
  config.py            ⭐ phone, email, address, hours, practice areas
  content_practice.py  ⭐ the six practice-area articles
  content_pages.py     ⭐ FAQ questions and blog articles
  template.py          header, footer, structured data
  build.py             regenerates every page — `python3 tools/build.py`
```

You can edit the `.html` files directly for a quick fix. For anything you want to
change **everywhere at once** (phone number, address, a nav link), edit the file
in `tools/` and re-run the build — otherwise the next build will overwrite your
hand edits.

---

## Publish on Cloudflare Pages (recommended)

Cloudflare is the better choice here: its network has points of presence closer
to Ethiopian visitors than GitHub's, it supports the `_headers` and `_redirects`
files included in this project, and it gives you free analytics.

1. Push this folder to a GitHub repository (see the GitHub section below for the
   commands).
2. Go to **dash.cloudflare.com** → **Workers & Pages** → **Create** →
   **Pages** → **Connect to Git**.
3. Authorise Cloudflare and pick your repository.
4. On the build settings screen:
   - **Framework preset:** `None`
   - **Build command:** *leave empty*
   - **Build output directory:** `/`
5. Click **Save and Deploy**.

You'll get a URL like `elizabeth-tesfaye-law.pages.dev` within about a minute.
Every future `git push` redeploys automatically.

> **Optional:** if you'd rather Cloudflare rebuild the HTML from `tools/` on each
> deploy, set the build command to `python3 tools/build.py` and leave the output
> directory as `/`.

---

## Publish on GitHub Pages

```bash
cd path/to/this/folder
git init
git add .
git commit -m "Initial website"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

Then in the repository on github.com: **Settings → Pages → Build and deployment**

- **Source:** `Deploy from a branch`
- **Branch:** `main`, folder `/ (root)`
- **Save**

The site appears at `https://YOUR-USERNAME.github.io/YOUR-REPO/` after a minute
or two.

A GitHub Actions workflow is also included at `.github/workflows/deploy.yml`. If
you prefer that route, set **Source** to `GitHub Actions` instead — it rebuilds
the HTML from `tools/` on every push and warns you if any placeholder text is
still on the site.

> ⚠️ **A caveat about GitHub Pages:** it serves the site from a subfolder unless
> you attach a custom domain. Because every link in this site starts with `/`,
> the site will only work correctly on GitHub Pages once your domain is
> connected (or if you name the repository `YOUR-USERNAME.github.io`). Cloudflare
> Pages has no such issue. **If you're not connecting a domain right away, use
> Cloudflare.**

---

## Connect your domain

The site is configured for **`https://etlawoffice.com`** — matching your email
address. If you use a different domain, change `SITE_URL` at the top of
`tools/config.py` and re-run `python3 tools/build.py`, otherwise your canonical
tags and sitemap will point at the wrong place.

**On Cloudflare Pages:** your project → **Custom domains** → **Set up a domain**.
If the domain is already on Cloudflare, DNS is configured for you. Otherwise
Cloudflare shows you the two records to add at your registrar.

**On GitHub Pages:** **Settings → Pages → Custom domain**, enter the domain, save
(this creates a `CNAME` file automatically — don't create one by hand), then at
your registrar add:

```
A     @      185.199.108.153
A     @      185.199.109.153
A     @      185.199.110.153
A     @      185.199.111.153
CNAME www    YOUR-USERNAME.github.io
```

Tick **Enforce HTTPS** once the certificate is issued (usually under an hour).

---

## Editing content

### Change the phone number, email, address or opening hours

Open `tools/config.py`, edit the value, then run:

```bash
python3 tools/build.py
```

This updates every page — including the footer, the structured data Google
reads, and the `tel:` links — in one pass.

### Change the wording of a practice-area page

Open `tools/content_practice.py`. Each of the six pages is a block of ordinary
HTML. Edit the text between the tags, then rebuild.

### Add or change an FAQ question

Open `tools/content_pages.py` and edit `FAQ_GROUPS`. Questions are grouped by
topic. New questions are added to the page **and** to the FAQ structured data
automatically.

### Add a new article

In `tools/content_pages.py`, copy one of the entries in the `INSIGHTS` list and
change `slug`, `title`, `seo_title`, `description`, `date`, `date_display`,
`category`, `related` and `body`. Rebuild, and the article appears on the blog
index, the home page, the sitemap and the other articles' "continue reading"
sections.

### Add client testimonials

There's a commented-out testimonial block near the bottom of `tools/build.py`
inside `build_home()`. Uncomment it and add **real** quotes from clients who have
given you written permission to publish them. Please don't publish invented or
composite testimonials — beyond the professional-conduct problem, fabricated
reviews are the kind of thing that damages a law practice badly if noticed.

### Replace the logo

`assets/img/logo.svg`, `assets/img/logo-mark.svg` and `assets/img/favicon.svg`
are **recreations** of your ET monogram drawn as vector art, because the original
image file wasn't available when the site was built. They match the design and
colours closely, and being vectors they stay sharp at any size.

If you want to use your original file instead: save it as
`assets/img/logo.svg` (or `.png`), and replace the `MARK_SVG` constant at the top
of `tools/template.py` with an `<img src="/assets/img/logo.svg" alt="">` tag.
Then rebuild.

---

## Making the contact form actually send email

Right now, submitting the contact form opens the visitor's own email program with
the message pre-filled. That works, but a meaningful share of visitors —
especially on phones without a mail app configured — will drop off.

To receive submissions directly, pick a free form service and change two things:

**Using [Formspree](https://formspree.io) (simplest):**

1. Sign up, create a form, copy your endpoint (`https://formspree.io/f/XXXXXX`).
2. In `tools/build.py`, find `<form id="consultation-form"` and change:
   ```html
   data-mode="mailto" data-email="..." method="post" action="#"
   ```
   to:
   ```html
   method="post" action="https://formspree.io/f/XXXXXX"
   ```
3. Rebuild.

**Using Cloudflare Pages Functions** (no third party, if you're hosting on
Cloudflare): add a `functions/api/contact.js` handler and point the form's
`action` at `/api/contact`. Cloudflare's docs cover this under "Pages Functions".

Whichever you choose, test it by submitting the form yourself and confirming the
message arrives.

---

## SEO: what's already done, what you must do

### Already built in

- Unique `<title>` (≤ 62 chars) and meta description (≤ 155 chars) on every page
- One `<h1>` per page containing that page's target keyword, with a logical
  `<h2>`/`<h3>` structure beneath it
- Descriptive URLs (`/family-law-addis-ababa/`, not `/page3/`)
- **JSON-LD structured data:** `LegalService` with full address, geo coordinates,
  opening hours and a service catalogue; `Attorney`; `FAQPage` on the FAQ;
  `BreadcrumbList` sitewide; `Service` on each practice page; `Article` on each
  post
- Consistent NAP (name, address, phone) in the footer of every page — this is the
  single biggest local-SEO signal
- Canonical tags, Open Graph and Twitter Card tags with a custom share image
- `sitemap.xml` and `robots.txt`
- Internal links between every related practice page
- Fast by design: one CSS file, one small JS file, inline SVG (no icon fonts), no
  tracking scripts, no jQuery, fonts loaded without blocking rendering
- Accessibility: semantic landmarks, skip link, keyboard-navigable menu, visible
  focus outlines, WCAG AA contrast, `prefers-reduced-motion` respected

### What only you can do

1. **Create a Google Business Profile** — go to
   business.google.com, add "Elizabeth Tesfaye Law Office", category *Law Firm*
   or *Attorney*, and enter the address **exactly** as it appears in the footer
   of this site. Verify it. For a local law office this will drive more enquiries
   than everything else on this list combined.
2. **Submit the sitemap** — Google Search Console → add
   `etlawoffice.com` → verify ownership → **Sitemaps** → submit `sitemap.xml`.
   Do the same at Bing Webmaster Tools.
3. **Check the map pin.** The coordinates in `tools/config.py` are approximate
   for Summit. Open Google Maps, right-click your building, copy the exact
   latitude/longitude, and paste them into `LATITUDE` and `LONGITUDE`.
4. **List the firm in Ethiopian directories** with the identical name, address
   and phone number. Inconsistent listings actively hurt local ranking.
5. **Publish new articles.** Three are included to establish the section. One
   genuinely useful article a month, answering a question clients actually ask,
   compounds over time. This is the highest-return ongoing SEO work available to
   a law firm.

---

## Adding an Amharic version later

The site is structured for it. When you're ready:

1. Translate the content files into `tools/content_practice_am.py` and
   `tools/content_pages_am.py`.
2. Set `AMHARIC_READY = True` in `tools/config.py`. This switches on the
   `hreflang` alternate tags in every page's `<head>` and turns the greyed-out
   **አማርኛ** button in the header into a working link to `/am/`.
3. Generate the Amharic pages under `/am/`.

The `hreflang` markup tells Google the two versions are translations of one
another rather than duplicate content — which matters, because getting this wrong
is a common way to lose ranking on a bilingual site.

---

## Before you go live

See **PUBLISH-CHECKLIST.md** — there are a small number of facts about you and
your practice that the site cannot invent, and they're marked in yellow on the
About page until you fill them in.

---

*Built as a static site: no CMS to update, no plugins to patch, no monthly
hosting bill.*
