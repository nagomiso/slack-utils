from slack_sdk.webhook import WebhookClient

from slackutils.data import Attachments


def send(
    webhook_url: str,
    title: str,
    workflow_id: str,
    status: str,
    namespace: str,
    serviceaccount: str,
    url: str,
) -> None:
    webhook = WebhookClient(url=webhook_url)
    attachments = Attachments(
        title=title,
        workflow_id=workflow_id,
        status=status,
        namespace=namespace,
        serviceaccount=serviceaccount,
        url=url,
    )
    response = webhook.send(attachments=attachments.to_payload())
    if response.status_code != 200:
        raise
    if response.body != "ok":
        raise
