import os
from typing import Optional, Sequence

import click

import slackutils.files
import slackutils.webhook


@click.group()
def main():
    pass


@main.command()
@click.option("--header", required=False, type=str, default=None)
@click.option("--message", "-m", required=False, type=str, default=None)
@click.option("--field", "-f", required=False, type=str, multiple=True, default=None)
@click.option("--footer", required=False, type=str, default=None)
@click.option(
    "--color",
    required=False,
    type=click.Choice(["good", "warning", "danger"], case_sensitive=False),
    default=None,
)
def webhook_send(
    header: Optional[str],
    message: Optional[str],
    field: Sequence[str],
    footer: Optional[str],
    color: Optional[str],
) -> None:
    webhook_url = os.environ["SLACK_WEBHOOK_URL"]
    slackutils.webhook.send(
        webhook_url=webhook_url,
        header=header,
        message=message,
        fields=field,
        footer=footer,
        color=color,
    )


@main.command()
@click.option("--channel", required=True, type=str)
@click.option("--filepath", required=True, type=str)
@click.option("--description", required=True, type=str)
def upload_image(
    channel: str,
    filepath: str,
    description: str,
) -> None:
    token = os.environ["TOKEN"]
    slackutils.files.upload_images(
        token=token,
        channel=channel,
        filepath=filepath,
        description=description,
    )


if __name__ == "__main__":
    main()
