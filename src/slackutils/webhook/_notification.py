from typing import Optional, Sequence
from slack_sdk.errors import SlackClientError
from slack_sdk.webhook import WebhookClient

from slackutils.data import Attachments


def send(
    webhook_url: str,
    header: Optional[str],
    message: Optional[str],
    fields: Sequence[str],
    footer: Optional[str],
    color: Optional[str],
) -> None:
    webhook = WebhookClient(url=webhook_url)
    attachments = Attachments(
        color, header, message, fields, footer,
    )
    response = webhook.send(attachments=attachments.to_dict())
    status_code, body = response.status_code, response.body
    if status_code != 200 or body != "ok":
        raise SlackClientError(
            f"Webhook request was failed - status: {status_code}, body: {body}"
        )
