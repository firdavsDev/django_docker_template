import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Sentry config
sentry_sdk.init(
    dsn=os.environ["SENTRY_DSN"],
    integrations=[
        DjangoIntegration(),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
