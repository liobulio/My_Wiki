"""Minimal YAML-frontmatter reader (stdlib only) for the subset this wiki uses:
scalars, quoted strings, inline lists [a, b], block lists (- item), one level of nesting.
Falls back to PyYAML when installed."""
import pathlib, re

try:  # optional
    import yaml  # type: ignore
except Exception:  # noqa: BLE001
    yaml = None

_FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)


def _scalar(v: str):
    v = v.strip()
    if v == "" or v in ("null", "~"):
        return ""
    if (v[0] == v[-1]) and v[0] in "\"'" and len(v) >= 2:
        return v[1:-1]
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [] if not inner else [_scalar(x) for x in _split_inline(inner)]
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    if re.fullmatch(r"-?\d+\.\d*", v):
        return float(v)
    return v


def _split_inline(s: str):
    out, cur, depth, q = [], "", 0, None
    for ch in s:
        if q:
            cur += ch
            if ch == q:
                q = None
            continue
        if ch in "\"'":
            q = ch; cur += ch; continue
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur); cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return out


def parse_yaml_subset(text: str) -> dict:
    data, key, indent_of_key = {}, None, 0
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.split(" #")[0].rstrip() if not raw.strip().startswith("#") else ""
        if not line.strip():
            i += 1; continue
        ind = len(raw) - len(raw.lstrip(" "))
        st = line.strip()
        if ind == 0 and ":" in st and not st.startswith("- "):
            k, _, v = st.partition(":")
            key = k.strip()
            if v.strip():
                data[key] = _scalar(v)
            else:
                data[key] = None  # to be filled by block below
        elif st.startswith("- ") and key is not None:
            item = st[2:].strip()
            if data.get(key) is None:
                data[key] = []
            if isinstance(data[key], list):
                if ":" in item and not item.startswith(("[", "\"", "'")):
                    k2, _, v2 = item.partition(":")
                    d = {k2.strip(): _scalar(v2)}
                    # nested keys of this list item
                    j = i + 1
                    while j < len(lines) and lines[j].strip() and (len(lines[j]) - len(lines[j].lstrip(" "))) > ind and not lines[j].strip().startswith("- "):
                        k3, _, v3 = lines[j].strip().partition(":")
                        d[k3.strip()] = _scalar(v3); j += 1
                    data[key].append(d); i = j; continue
                data[key].append(_scalar(item))
        elif ind > 0 and key is not None and ":" in st:
            if data.get(key) is None:
                data[key] = {}
            if isinstance(data[key], dict):
                k2, _, v2 = st.partition(":")
                data[key][k2.strip()] = _scalar(v2)
        i += 1
    for k, v in list(data.items()):
        if v is None:
            data[k] = ""
    return data


def split_frontmatter(text: str):
    m = _FM.match(text)
    if not m:
        return {}, text
    block = m.group(1)
    meta = None
    if yaml is not None:
        try:
            meta = yaml.safe_load(block) or {}
        except Exception:  # noqa: BLE001
            meta = None
    if meta is None:
        meta = parse_yaml_subset(block)
    return meta, text[m.end():]


def load_frontmatter(path):
    return split_frontmatter(pathlib.Path(path).read_text(encoding="utf-8"))
