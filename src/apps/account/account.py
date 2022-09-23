from django.urls import include, path

app_name = "account"

urlpatterns = [
    path(
        "",
        include(
            (
                "src.apps.account.urls.account",
                "src.apps.account.urls.account",
            ),
            namespace="account",
        ),
    ),
]
