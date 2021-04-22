from slack_sdk.errors import SlackClientError
from slack_sdk.webhook import WebhookClient

from slackutils.data import Attachments


def send(
    webhook_url: str,
    title: str,
    workflow_id: str,
    status: str,
    message: str,
    namespace: str,
    serviceaccount: str,
    url: str,
) -> None:
    webhook = WebhookClient(url=webhook_url)
    attachments = Attachments(
        title=title,
        workflow_id=workflow_id,
        status=status,
        message=message,
        namespace=namespace,
        serviceaccount=serviceaccount,
        url=url,
    )
    response = webhook.send(attachments=attachments.to_payload())
    status_code, body = response.status_code, response.body
    if status_code != 200 or body != "ok":
        raise SlackClientError(
            f"Webhook request was failed - status: {status_code}, body: {body}"
        )
