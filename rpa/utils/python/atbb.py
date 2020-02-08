def read_id_pass():
    f = open('id_pass.txt')
    txt = f.read()
    f.close()
    lines = txt.split('\n')
    id, pw = lines[0], lines[1]
    return id, pw