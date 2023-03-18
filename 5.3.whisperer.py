import re


def find_secret_messages(generator):
    """
    iterate over a generator, in each iteration look for secret messages
    and yields them one by one.
    :param generator: a generator that contains chunks of a binary file.
    :return: strings containing "!" which represent the secret messages.
    """
    # initialize a byte object that will contain the chunks
    buffer = b""

    for chunk in generator:
        buffer += chunk

        while b"!" in buffer:
            # look for a secret message (a sequence of at least 5 lowercase letters followed by an "!")
            match = re.search(b"[a-z]{5,}!", buffer)
            # if a match is found, locate it in the buffer and decode it to utf-8 formate then yield it.
            if match:
                message_start = match.start()
                message_end = match.end()
                message = buffer[message_start:message_end].decode("utf-8")
                yield message
                buffer = buffer[message_end:]
            else:
                # if no match is found, retain the last 4 bytes of the buffer to use them in the next iteration
                buffer = buffer[-4:]
            break


def read_logo_file(filename, chunk_size=1024):
    """
    this generator opens a file in binary representation and reads it by chunks.
    :param filename: name of the file that we want to read.
    :param chunk_size: the size of the chunk that we want to read in each "iteration", default = 1024.
    :return: a chunk_size chunk of the file which name is received as a param.
    """
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
