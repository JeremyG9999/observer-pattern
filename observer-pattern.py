class Subject:
    def __init__(self):
        self.observers = []
    def add(self, observer):
        self.observers.append(observer)
    def delete(self, observer):
        self.observers.remove(observer)
    def notify(self, message):
        for observer in self.observers:
            observer.notification(message)
    def retrieve(self):
        for observer in self.observers:
            print(observer.name)
    def update(self, old, new):
        for observer in self.observers:
            if observer.name == old:
                observer.name = new
class Observer:
    def __init__(self, name):
        self.name = name
    def notification(self, message):
        print(f"{self.name} message: {message}")
def main():
    subject = Subject()
    observer1 = Observer("Observer 1")
    observer2 = Observer("Observer 2")
    subject.add(observer1)
    subject.add(observer2)
    subject.notify("Hello World!")
    subject.update("Observer 1", "Observer 3")
    subject.delete(observer2)
    subject.retrieve()
main()