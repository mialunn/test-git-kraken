from portscanner import *
import fire

class Main:

    def start(self):
        target = Target("localhost", 0, 25565)

        target.print_information()

if __name__ == '__main__':
    fire.Fire(Main)