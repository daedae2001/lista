def une_csvs(li):
    todo = ""
    for arc in li:
        ar = arc.replace('.m3u8', '.csv').replace('.m3u', '.csv')
        f = open(ar, 'r', encoding="utf8")
        todo = todo+f.read()
        f.close()
    f = open('todo.csv', 'w', encoding="utf8")
    f.write(todo)
    f.close()
