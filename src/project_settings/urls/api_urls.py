from django.urls import path, include


app_name = "api"

urlpatterns = [
    path("users/", include("users.urls", namespace="auth")),
    path("clients/", include("clients.urls", namespace="clients")),
    path("letters/", include("letters.urls", namespace="letters")),
    path("mailings/", include("mailings.urls", namespace="mailings")),
]
