import os
import glob
import shutil

for path in glob.glob('BlockScript-GUI/build/*.html'):
    print(f'Patching HTML {path}')
    with open(path, 'r') as file:
        contents = file.read()
        contents = contents.replace('</head>', '<meta name="robots" content="noindex"></head>')
        contents = contents.replace('<link rel="manifest" href="manifest.webmanifest">', '')
    with open(path, 'w') as file:
        file.write(contents)

for path in glob.glob('BlockScript-GUI/build/js/*.js'):
    print(f'Patching JS {path}')
    with open(path, 'r') as file:
        contents = file.read()
        contents = contents.replace('https://trampoline.turbowarp.org', 'https://trampoline.turbowarp.xyz')
    with open(path, 'w') as file:
        file.write(contents)

os.remove('BlockScript-GUI/build/sw.js')
os.remove('BlockScript-GUI/build/manifest.webmanifest')
os.remove('BlockScript-GUI/build/fullscreen.html')
os.remove('BlockScript-GUI/build/embed.html')
os.remove('BlockScript-GUI/build/index.html')

shutil.copy('BlockScript-GUI/build/editor.html', 'BlockScript-GUI/build/index.html')
shutil.copy('robots.txt', 'BlockScript-GUI/build/robots.txt')
