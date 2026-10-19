"""Shared welcome-video embed for the hub, Phase 1, Bridge and Sharpen heroes.

videos.json "welcome" values can be either:
- a site-relative MP4 path such as "video/launch.mp4" (hosted on GitHub Pages
  next to the pages); a "<name>.vtt" caption file and "<name>-poster.jpg" beside
  it are picked up automatically when present, or
- a YouTube URL (watch, youtu.be or embed form), rendered as an iframe.
Site mode renders a player; artifact mode renders a link-out button.
"""
import html, os, re

PAGES_BASE = "https://cg1262.github.io/gambill-data-engineer-track/site/"
YT_RE = re.compile(r"(?:youtu\.be/|youtube\.com/(?:watch\?v=|embed/))([A-Za-z0-9_-]{6,})")
_IFRAME_ALLOW = ("accelerometer; autoplay; clipboard-write; encrypted-media; "
                 "gyroscope; picture-in-picture; web-share")


def _is_local(url):
    return not re.match(r"^[a-z]+://", url, re.I)


def welcome_html(videos, key, mode, site_dir):
    url = (videos.get("welcome", {}).get(key, "") or "").strip()
    if not url:
        return ""
    e = html.escape
    if mode != "site":
        href = PAGES_BASE + url if _is_local(url) else url
        return f'<a class="welcome-btn" href="{e(href)}" target="_blank" rel="noopener">&#9654; Watch welcome</a>'
    if _is_local(url):
        stem = url[:-4] if url.lower().endswith(".mp4") else url
        poster = f"{stem}-poster.jpg"
        vtt = f"{stem}.vtt"
        poster_attr = f' poster="{e(poster)}"' if os.path.exists(os.path.join(site_dir, poster)) else ""
        track = (f'<track kind="captions" src="{e(vtt)}" srclang="en" label="English" default>'
                 if os.path.exists(os.path.join(site_dir, vtt)) else "")
        return (f'<div class="video-embed"><video controls preload="metadata" playsinline{poster_attr}>'
                f'<source src="{e(url)}" type="video/mp4">{track}'
                f'<a href="{e(url)}">Download the welcome video</a></video></div>')
    m = YT_RE.search(url)
    src = f"https://www.youtube.com/embed/{m.group(1)}" if m else url
    return (f'<div class="video-embed"><iframe src="{e(src)}" title="Welcome video" loading="lazy" '
            f'frameborder="0" allow="{_IFRAME_ALLOW}" allowfullscreen></iframe></div>')
