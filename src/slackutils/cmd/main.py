import os

import click

import slackutils.webhook


@click.group()
def main():
    pass


@main.command()
@click.option("--title", required=True, type=str)
@click.option("--workflow-id", required=True, type=str)
@click.option("--status", required=True, type=str)
@click.option("--namespace", required=True, type=str)
@click.option("--serviceaccount", required=True, type=str)
@click.option("--url", required=True, type=str)
def webhook_send(
    title: str,
    workflow_id: str,
    status: str,
    namespace: str,
    serviceaccount: str,
    url: str,
):
    webhook_url = os.environ["WEBHOOK_URL"]
    slackutils.webhook.send(
        webhook_url=webhook_url,
        title=title,
        workflow_id=workflow_id,
        status=status,
        namespace=namespace,
        serviceaccount=serviceaccount,
        url=url,
    )


if __name__ == "__main__":
    main()
