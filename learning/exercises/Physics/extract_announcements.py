import json
import re

path = r'C:\Users\borod\.gemini\antigravity\brain\da9eabd8-aced-40ce-b14a-a1a052db2d26\.system_generated\logs\transcript.jsonl'
seen = set()

with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        # Search for post texts that are not just names
        matches = re.findall(r'"text":"([^"]+)"', line)
        for m in matches:
            if len(m) > 20 and not re.match(r'^[А-Яа-яA-Za-z0-9\s]+$', m):
                if m not in seen and 'Реклама' not in m and 'Статистика' not in m:
                    seen.add(m)
                    print("POST:", m[:200])
