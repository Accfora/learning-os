import json

path = r'C:\Users\borod\.gemini\antigravity\brain\da9eabd8-aced-40ce-b14a-a1a052db2d26\.system_generated\logs\transcript.jsonl'
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        if '1340' in line:
            pos = line.find('1340')
            print("Found 1340 snippet:", line[max(0, pos-50):pos+250])
            break
