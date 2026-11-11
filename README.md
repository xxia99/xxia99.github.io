# xxia99.github.io

Personal academic website of Xin Xia. Plain HTML and CSS with a tiny vanilla-JS lightbox; no build step, no framework.

## Files

- `index.html` - the page (bio, news, publications, patents, experience)
- `assets/site.css` - all styles
- `images/avatar.jpg` - headshot
- `images/thumbs/`, `images/fulls/` - work previews (thumbnail + lightbox image)
- `data/XinXia-CV.pdf` - CV (compiled from `xin_xia_academic_cv.tex`)

## Publish on GitHub Pages

1. Create a public repository named exactly `xxia99.github.io` on GitHub.
2. In this folder:
   ```bash
   git add -A
   git commit -m "Initial academic website"
   git branch -M main
   git remote add origin git@github.com:xxia99/xxia99.github.io.git
   git push -u origin main
   ```
3. On GitHub: Settings > Pages > Source: "Deploy from a branch", branch `main`, folder `/ (root)`.
4. The site appears at https://xxia99.github.io/ within a minute or two.

## Update

Edit `index.html` directly (each paper is one `<article class="pub">` block under its year heading; add a 740x435 thumb and a full image), replace
`data/XinXia-CV.pdf` after recompiling the CV, then commit and push.
