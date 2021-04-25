from typing import NamedTuple

SUCCEEDED_COLOR = "#2EB886"
FAILED_COLOR = "#A30100"


class Attachments(NamedTuple):
    title: str
    workflow_id: str
    status: str
    message: str
    namespace: str
    serviceaccount: str
    url: str

    @property
    def color(self) -> str:
        if self.status == "Succeeded":
            return SUCCEEDED_COLOR
        if self.status == "Failed":
            return FAILED_COLOR
        return ""

    def to_payload(self) -> list:
        return [
            {
                "color": self.color,
                "blocks": [
                    {
                        "type": "header",
                        "text": {"type": "plain_text", "text": self.title},
                    },
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": self.message},
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*workflow id*:\n{self.workflow_id}",
                            },
                            {"type": "mrkdwn", "text": f"*status*:\n{self.status}"},
                            {
                                "type": "mrkdwn",
                                "text": f"*namespace*:\n{self.namespace}",
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*serviceaccount*:\n{self.serviceaccount}",
                            },
                        ],
                    },
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": f"*url*:\n{self.url}"},
                    },
                ],
            },
        ]
