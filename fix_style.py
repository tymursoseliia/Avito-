import sys

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the place where </head><body> is
bad_pattern = """    stroke: #8f8f8f !important;
    fill: #8f8f8f !important;
}
</head><body><div id="app">"""

good_pattern = """    stroke: #8f8f8f !important;
    fill: #8f8f8f !important;
}
</style>
</head><body><div id="app">"""

if bad_pattern in content:
    content = content.replace(bad_pattern, good_pattern)
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed unclosed style tag")
else:
    print("bad_pattern not found, let's try a regex")
    import re
    # Match the missing style tag area
    content, num_subs = re.subn(r'(\s*fill:\s*#8f8f8f\s*!important;\s*})\s*(</head><body>)', r'\1\n</style>\n\2', content)
    if num_subs > 0:
        with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed unclosed style tag using regex, {num_subs} substitutions")
    else:
        print("Could not find the target to replace")
