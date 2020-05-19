# Remove the titles, newline characters
# I couldn't do ' \" ' around the links. So I did it manually.

import json, copy

with open('entities', 'r', encoding='utf8') as f:
    entities = json.load(f)
    f.close()

new_entities = []
for e in entities:
    c = e['content']

    modified_text = ""
    for line in c.splitlines():
        if len(line) >= 1 and line[0] not in [r"\\", "="]:
            l = r''
            modified_text = modified_text + line
    modified_text = modified_text.replace(r"\\", " ")    # Doesn't work!

    e['content'] = modified_text
    ed = copy.deepcopy(e)
    new_entities.append(ed)

with open('modified_entities', 'w', encoding='utf8') as f:
    json.dump(new_entities, f, ensure_ascii=False)
    f.close()