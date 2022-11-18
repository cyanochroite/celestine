from .report import main as train


def report(page):
    with page.line("head") as line:
        line.label("title", "Page 0")
    label = train()
    for item in label:
        with page.line("body") as line:
            line.label(item, item)


def main(_):
    return [
        report,
    ]
