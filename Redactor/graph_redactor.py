import command_generator


if __name__ == "__main__":
    cli = command_generator.get_command()
    while True:
        command = next(cli)
        print(command.__name__)
