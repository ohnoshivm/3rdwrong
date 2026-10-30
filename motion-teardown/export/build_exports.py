"""Build lightweight Substack and Medium Markdown copies from ARTICLE.md.

Run from the repository root: python3 motion-teardown/export/build_exports.py.
No HTML, embedded images or upload-kit copies are written.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = ROOT.parent
OUT = ROOT / "export"
REPO = "https://github.com/ohnoshivm/3rdwrong"
raw = (ROOT / "ARTICLE.md").read_text(encoding="utf-8")
frontmatter, src = raw.split("---", 2)[1:]
src = src.lstrip()
IMG = re.compile(r"^!\[(.*?)\]\((.+?)\)\n\*(.+)\*$", re.M)
images = [dict(n=n, alt=m[1], path=m[2], cap=m[3]) for n, m in enumerate(IMG.finditer(src), 1)]


def repo_url(link):
    path, _, frag = link.partition("#")
    target = (ROOT / path).resolve()
    relative = target.relative_to(REPO_ROOT).as_posix()
    kind = "tree" if target.is_dir() else "blob"
    return f"{REPO}/{kind}/main/{relative}" + (f"#{frag}" if frag else "")


def absolutise(text):
    return re.sub(r"(?<!!)\[([^\]]+)\]\((?!https?:|#|mailto:)([^)]+)\)",
                  lambda m: f"[{m[1]}]({repo_url(m[2])})", text)


def tables_to_lists(text):
    """Substack and Medium have no Markdown tables: turn each row into a bullet."""
    out, lines, i = [], text.split("\n"), 0
    in_code = False
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[-| :]+\|$", lines[i + 1]):
            head = [c.strip() for c in line.strip("|").split("|")]
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip("|").split("|")]
                first = cells[0] if cells[0].startswith("**") else f"**{cells[0]}**"
                rest = "; ".join(f"{h}: {c}" for h, c in zip(head[1:], cells[1:]) if c and c != "—")
                out.append(f"- {first}: {rest}" if rest else f"- {first}")
                i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out)



def platform_md(name):
    body = IMG.sub(lambda m: "[Image {:02d}: {} — {}]".format(
        next(im["n"] for im in images if im["path"] == m[2]), Path(m[2]).name, m[3]), src)
    note = f"<!-- {name} export of ARTICLE.md. Upload images directly from media/; no upload kit is stored. -->\n\n"
    return "---" + frontmatter + "---\n\n" + note + tables_to_lists(absolutise(body))


for name in ("Substack", "Medium"):
    (OUT / f"{name.lower()}.md").write_text(platform_md(name), encoding="utf-8")
print(f"{len(images)} image slots; wrote substack.md and medium.md only")
