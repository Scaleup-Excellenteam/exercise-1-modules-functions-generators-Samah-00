import re


def find_secret_messages(generator):
    buffer = b""

    for chunk in generator:
        buffer += chunk

        while b"!" in buffer:
            match = re.search(b"[a-z]{5,}!", buffer)
            if match:
                message_start = match.start()
                message_end = match.end()
                message = buffer[message_start:message_end].decode("utf-8")
                yield message
                buffer = buffer[message_end:]
            else:
                buffer = buffer[-4:]
                break

    if len(buffer) >= 5 and b"!" not in buffer:
        message = buffer[-5:].decode("utf-8") + "!"
        yield message


def read_logo_file(filename, chunk_size=1024):
    with open(filename, "rb") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk


filename = "logo.jpg"
generator = read_logo_file(filename)
messages = find_secret_messages(generator)

for message in messages:
    print(message)

# this is the output that I received:
# python!
# isawesome!
# welldone!
# goodjob!
