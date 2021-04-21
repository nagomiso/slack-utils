from typing import NamedTuple


SUCCEEDED_COLOR = "#2EB886"
FAILED_COLOR = "#A30100"


class Attachments(NamedTuple):
    title: str
    workflow_id: str
    status: str
    namespace: str
    serviceaccount: str
    url: str

    @property
    def color(self) -> str:
        if self.status == "Succeeded":
            return SUCCEEDED_COLOR
        if self.status == "Failed":
            return FAILED_COLOR

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
                        "fields": [
                            {"type": "mrkdwn", "text": "*workflow id*"},
                            {"type": "mrkdwn", "text": "*status*"},
                        ],
                    },
                    {
                        "type": "section",
                        "fields": [
                            {"type": "mrkdwn", "text": self.workflow_id},
                            {"type": "mrkdwn", "text": self.status},
                        ],
                    },
                    {
                        "type": "section",
                        "fields": [
                            {"type": "mrkdwn", "text": "*namespace*"},
                            {"type": "mrkdwn", "text": "*serviceaccount*"},
                        ],
                    },
                    {
                        "type": "section",
                        "fields": [
                            {"type": "mrkdwn", "text": self.namespace},
                            {"type": "mrkdwn", "text": self.serviceaccount},
                        ],
                    },
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": "*url*"},
                    },
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": self.url},
                    },
                ],
            },
        ]
