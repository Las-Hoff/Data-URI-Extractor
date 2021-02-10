import re
import os
import sys
import mimetypes
import urllib.request

def load_file(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.readlines()
    return text

def pick_uris(text, pattern):
    uris = []
    for l in text:
        matches = re.findall(pattern, l)
        if matches != []:
            for i in matches:
                uris += [i[0]]
    return uris

def detect_ext(h):
    buf = re.sub(r'^(data:)', '', h)
    mime_t = re.sub(r'((;charset=[!#-/0-9:;=\?@A-Z\[\]_a-z~]+?)?(;base64)?)$', '', buf)
    dic = {'jpg':'.jpg', 'jpeg':'.jpeg', 'gif':'.gif', 'bmp':'.bmp', 'png':'.png', 'svg+xml':'.svg', 'tiff':'.tiff', 'tif':'.tif', 'webp':'.webp', 'apng':'.apng', 'icon':'.ico'}
    if mime_t == '':
        return '.txt'
    for i in dic:
        if i in mime_t:
            return dic[i]
    ext = mimetypes.guess_extension(mime_t)
    if ext != None:
        return ext
    return '.dat' 

def decode(uris, dirname):
    if uris == []:
        print('0 file saved')
        exit()
    digit = len(str(len(uris) - 1))
    for i, uri in enumerate(uris):
        header = uri.split(',', 1)[0]
        ext = detect_ext(header)
        i_z = str(i).zfill(digit)
        if ext == '.dat':
            with open(dirname + '/unknown_bin.txt', 'w', encoding = 'utf-8') as f:
                f.write(i_z + ' ' +header + '\n')
        filename = dirname + '/file_' + i_z + ext
        content = urllib.request.urlopen(uri).read()
        with open(filename, 'wb') as f:
            f.write(content)
    print(f'{len(uris)} files saved')

if len(sys.argv) != 2:
    print('usage: ' + sys.argv[0] + '<filename>')
filename = sys.argv[1]
t = load_file(filename)
regex = r'(data:([!#-/0-9:;=\?@A-Z\[\]_a-z~]+?/[!#-/0-9:;=\?@A-Z\[\]_a-z~]+?)?(;charset=[!#-/0-9:;=\?@A-Z\[\]_a-z~]+?)?(;base64)?,[!#-/0-9:;=\?@A-Z\[\]_a-z~]+)'
u = pick_uris(t, regex)
if '.' in filename:
    name = filename.rsplit('.', 1)[0]
else:
    name = filename
dirname = name + '_saved'
if os.path.exists(dirname):
    print('error: directory already exists')
    exit()
os.mkdir(dirname)
decode(u, dirname)