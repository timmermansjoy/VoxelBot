__all__ = ("Voxy",)

from hata import Client
from hata.ext.slash import setup_ext_slash

from ..constants import VOXELBOT_TOKEN


Voxy = Client(
    VOXELBOT_TOKEN,
)


slash = setup_ext_slash(Voxy, use_default_exception_handler=False)


@slash.error
async def slash_error(client: Client, event, *_):
    try:
        await client.interaction_response_message_create(
            event,
            "Something went wrong! Ping <@141320943459893249>",
            show_for_invoking_user_only=True,
        )
    except:
        pass
    return False
