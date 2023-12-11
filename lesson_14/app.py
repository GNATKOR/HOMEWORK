from lesson_14.interfaces import FileWorker


def app():
    fw = FileWorker('tested.txt')
    print(f'Initial file contents: {fw.read()}')
    fw.append('obj1')
    fw.append('obj2')
    print(f'Final file contents: {fw.read()}')
    fw.close()


app()
