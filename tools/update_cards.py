#!/usr/bin/env python3
# tools/update_cards.py
"""
Regenerate every place that lists our published datasets, from `datasets.yaml`.

Sources of truth
    datasets.yaml                      (this repo)

Targets
    README.md                          (this repo, GitHub)
    org-card/README.md                 (Hugging Face organization card,
                                        Space KeenForgeAI/README)

Generated regions are delimited by HTML-comment markers so they survive
hand-editing of the rest of the file:

    <!-- GEN:TABLE -->        ... <!-- GEN:TABLE_END -->
    <!-- GEN:LINKS -->        ... <!-- GEN:LINKS_END -->
    <!-- GEN:DETAILS -->      ... <!-- GEN:DETAILS_END -->
    <!-- GEN:CARD_TABLE -->   ... <!-- GEN:CARD_TABLE_END -->
    <!-- GEN:CARD_ZH -->      ... <!-- GEN:CARD_ZH_END -->

Usage
    python tools/update_cards.py            # regenerate the two files
    python tools/update_cards.py --check    # exit 1 if anything is out of date
    python tools/update_cards.py --push     # regenerate, push to GitHub and HF
"""
import os
import sys
import argparse
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
YAML_PATH = os.path.join(ROOT, "datasets.yaml")
README_PATH = os.path.join(ROOT, "README.md")
CARD_PATH = os.path.join(ROOT, "org-card", "README.md")

HF_CARD_REPO = "KeenForgeAI/README"          # the org-card Space
HF_ENDPOINT = "https://huggingface.co"       # force it: this machine sets hf-mirror.com
HF_PROXY = "http://127.0.0.1:10808"


# ---------------------------------------------------------------------------
# loading
# ---------------------------------------------------------------------------
def load():
    try:
        import yaml
    except ImportError:
        sys.exit("PyYAML is required:  pip install pyyaml")
    with open(YAML_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not data.get("datasets"):
        sys.exit("datasets.yaml contains no datasets")
    return data


def n(v):
    return "{:,}".format(int(v))


# ---------------------------------------------------------------------------
# block builders
# ---------------------------------------------------------------------------
def block_table(ds):
    out = ["| Dataset | Domain | Images | Boxes | Hugging Face | ModelScope |",
           "|---|---|---|---|---|---|"]
    for d in ds:
        out.append(
            "| **{id}** | {e} {dom} | {img} | {box} | "
            "[![HF](https://img.shields.io/badge/HF-dataset-yellow)]({hf}) | "
            "[ModelScope]({ms}) |".format(
                id=d["id"], e=d["emoji"], dom=d["domain_en"],
                img=n(d["images"]), box=n(d["boxes"]), hf=d["hf"], ms=d["ms"]))
    return "\n".join(out)


def block_links(ds):
    out = []
    for d in ds:
        s = "- **{id}** — [Hugging Face]({hf}) · [ModelScope]({ms})".format(**d)
        if d.get("doi"):
            s += " · [DOI](https://doi.org/{doi})".format(**d)
        out.append(s)
    return "\n".join(out)


def block_details(ds):
    parts = []
    for d in ds:
        parts.append("#### {e} {id} — {img} images · {box} boxes".format(
            e=d["emoji"], id=d["id"], img=n(d["images"]), box=n(d["boxes"])))
        if d.get("doi"):
            parts.append("")
            parts.append("DOI: [{doi}](https://doi.org/{doi})".format(**d))
        parts.append("")
        parts.append("{b} {s}".format(b=d["blurb_en"], s=d["summary_en"]))
        parts.append("")
    return "\n".join(parts).rstrip()


def block_card_table(ds):
    out = ["| Dataset | Domain | Size | Description |", "|---|---|---|---|"]
    for d in ds:
        out.append("| [`{id}`]({hf}) | {e} {dom} | {img} images · {box} boxes | {desc} |".format(
            id=d["id"], hf=d["hf"], e=d["emoji"], dom=d["domain_short"],
            img=n(d["images"]), box=n(d["boxes"]), desc=d["description_en"]))
    return "\n".join(out)


def block_card_zh(ds):
    parts = []
    for d in ds:
        parts.append("{e} [`{id}`]({hf})（{dom}，{img} 张 / {box} 框）".format(
            e=d["emoji"], id=d["id"], hf=d["hf"], dom=d["domain_zh"],
            img=n(d["images"]), box=n(d["boxes"])))
    return "**已发布数据集**：" + "、".join(parts)


# ---------------------------------------------------------------------------
# marker replacement
# ---------------------------------------------------------------------------
def replace_block(text, marker, body):
    start = "<!-- GEN:%s -->" % marker
    end = "<!-- GEN:%s_END -->" % marker
    i = text.find(start)
    j = text.find(end)
    if i < 0 or j < 0:
        raise SystemExit("marker pair not found: %s / %s" % (start, end))
    if j < i:
        raise SystemExit("marker order wrong for %s" % marker)
    return text[: i + len(start)] + "\n" + body + "\n" + text[j:]


def render(text, plan):
    for marker, body in plan:
        text = replace_block(text, marker, body)
    return text


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def write_if_changed(p, new):
    old = read(p)
    if old == new:
        return False
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(new)
    return True


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="do not write; exit 1 if any target is out of date")
    ap.add_argument("--push", action="store_true",
                    help="push README.md to GitHub and org-card/README.md to the HF Space")
    args = ap.parse_args()

    data = load()
    ds = data["datasets"]
    print("datasets.yaml: %d dataset(s) -> %s" % (len(ds), ", ".join(d["id"] for d in ds)))

    targets = [
        (README_PATH, [("TABLE", block_table(ds)),
                       ("LINKS", block_links(ds)),
                       ("DETAILS", block_details(ds))]),
        (CARD_PATH, [("CARD_TABLE", block_card_table(ds)),
                     ("CARD_ZH", block_card_zh(ds))]),
    ]

    changed = []
    for path, plan in targets:
        new = render(read(path), plan)
        rel = os.path.relpath(path, ROOT)
        if args.check:
            if new != read(path):
                print("  OUT OF DATE: %s" % rel)
                changed.append(rel)
            else:
                print("  up to date  : %s" % rel)
        else:
            if write_if_changed(path, new):
                print("  updated     : %s" % rel)
                changed.append(rel)
            else:
                print("  unchanged   : %s" % rel)

    if args.check:
        return 1 if changed else 0

    if not changed:
        print("nothing to do")

    if args.push:
        push_github()
        push_hf_card()
    return 0


def _run(args, cwd=None):
    print("  $", " ".join(args))
    p = subprocess.run(args, cwd=cwd or ROOT, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    if p.stdout and p.stdout.strip():
        print("   ", p.stdout.strip()[:600])
    if p.stderr and p.stderr.strip():
        print("    err:", p.stderr.strip()[:600])
    return p.returncode


def push_github():
    """Stage everything, commit if anything changed, then push."""
    print("pushing to GitHub ...")
    _run(["git", "add", "-A"])
    staged = subprocess.run(["git", "diff", "--cached", "--quiet"],
                            cwd=ROOT).returncode != 0
    if not staged:
        print("  nothing staged - nothing to commit")
        return
    _run(["git", "-c", "user.name=KeenForgeAI",
          "-c", "user.email=lucygan113@gmail.com",
          "commit", "-m", "Update dataset index from datasets.yaml"])
    _run(["git", "push", "origin", "HEAD"])


def push_hf_card():
    print("uploading org card to Hugging Face (%s) ..." % HF_CARD_REPO)
    os.environ["HF_ENDPOINT"] = HF_ENDPOINT
    os.environ["HTTP_PROXY"] = HF_PROXY
    os.environ["HTTPS_PROXY"] = HF_PROXY
    os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
    try:
        from huggingface_hub import HfApi
    except ImportError:
        print("  huggingface_hub not installed - skipped")
        return
    tok_path = os.path.expanduser("~/.cache/huggingface/token")
    token = open(tok_path).read().strip() if os.path.exists(tok_path) else None
    api = HfApi(token=token, endpoint=HF_ENDPOINT)
    api.upload_file(path_or_fileobj=CARD_PATH, path_in_repo="README.md",
                    repo_id=HF_CARD_REPO, repo_type="space",
                    commit_message="Update org card from datasets.yaml")
    print("  uploaded org-card/README.md -> %s" % HF_CARD_REPO)


if __name__ == "__main__":
    sys.exit(main())
