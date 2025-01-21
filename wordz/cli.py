import click

from wordz.libwordz import compte_mots


@click.command()
@click.argument("inpt")
@click.argument("word", required=False)
@click.option(
    "-n", default=32, help="How many words to display", show_default=True, type=int
)
def main(inpt: str, n: int, word: str | None):
    with open(inpt) as in_stream:
        count = compte_mots(in_stream)

    if word is not None:
        print(f"{word}: {count[word]}")
    else:
        for w, c in count.most_common(n):
            print(f"{w}: {c}")


if __name__ == "__main__":
    main()
