"""Složí samostatný index.html (pro GitHub Pages) ze src/artifact.html."""
from pathlib import Path

root = Path(__file__).parent
s = (root / "src/artifact.html").read_text()
i = s.index('<header class="hdr">')
head, body = s[:i].rstrip(), s[i:].rstrip()
reset = (":root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);"
         "padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}"
         "img{max-width:100%}[hidden]{display:none!important}")
doc = f"""<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>{reset}</style>
{head}
</head>
<body>
{body}
</body>
</html>
"""
(root / "index.html").write_text(doc)
print("index.html sestaven")
