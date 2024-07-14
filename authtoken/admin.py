from django.contrib import admin, messages

from .models import APIKey
from .extensions import generate_token


@admin.action(description="Revoke selected API keys")
def revoke_key(modeladmin, request, queryset):
    queryset.update(revoked=True)


@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "created_at",
    ]
    readonly_fields = ["token", "created_at"]


    def save_model(self, request, obj: APIKey, form, change):
        if not obj.token:  # New API key
            key = generate_token()
            obj.token = key

            if request:
                messages.add_message(
                    request,
                    messages.WARNING,
                    f"The API key for {obj} is '{obj.token}'."
                    "You should store it somewhere safe: "
                    "you will not be able to see the key again.",
                )

        obj.save()
        return obj
