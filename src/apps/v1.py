from django.urls import include, path

urlpatterns = [
    path(
        "account/",
        include(
            (
                "src.apps.account.account",
                "src.apps.account.account",
            ),
            namespace="account",
        ),
    ),
  
]
