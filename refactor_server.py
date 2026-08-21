import re

with open('server.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace imports
content = content.replace(
    'from src.backend.wealthwise.dashboard import dashboard_snapshot, snapshot_summary\nfrom src.backend.wealthwise.privacy import redact',
    'from src.backend.wealthwise.dashboard import dashboard_snapshot, snapshot_summary\nfrom src.backend.wealthwise.ingest import CURRENCY_SYMBOLS, detect_currency, normalize, strip_preamble\nfrom src.backend.wealthwise.privacy import redact'
)

# 2. Remove the block from CURRENCY_SYMBOLS = to the end of _auto_categorize
pattern = r'CURRENCY_SYMBOLS = \{\"INR\".*?def _auto_categorize\(df: pd\.DataFrame\) -> list\[str\]:.*?return out\n'
content = re.sub(pattern, '', content, flags=re.DOTALL)

# 3. Replace usages
content = content.replace('_normalize(_strip_preamble(raw))', 'normalize(strip_preamble(raw))')
content = content.replace('_currency[sid] = _detect_currency(raw)', '_currency[sid] = detect_currency(raw)')

with open('server.py', 'w', encoding='utf-8') as f:
    f.write(content)
