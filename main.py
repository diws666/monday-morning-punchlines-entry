# Monday morning punchline entry — verified length: 107 characters.
LINE = "Monday morning: my alarm went off, my coffee filed a complaint, and my motivation is still on annual leave."

import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)
