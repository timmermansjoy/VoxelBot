__all__ = ()

from hata.env import EnvGetter
from hata import Role, Guild


with EnvGetter() as env:
    VOXELBOT_TOKEN = env.get_str("VOXELBOT_TOKEN", raise_if_missing_or_empty=True)  # Discord bot token
    GITHUB_TOKEN = env.get_str("GITHUB_TOKEN", raise_if_missing_or_empty=True)  # GitHub token
    GUILD_ID = Guild.precreate(env.get_str("GUILD_ID"))  # The ID of the server
    ADMIN_ROLE = Role.precreate(env.get_int("ADMIN_ROLE_ID"))  # The ID of the admin role
    DEFAULT_ROLE = Role.precreate(env.get_int("DEFAULT_ROLE_ID"))  # The ID of the default role
    CONTRIBUTOR_ROLE = Role.precreate(env.get_int("CONTRIBUTOR_ROLE_ID"))  # The ID of the contributor role
    CONTRIBUTION_CHANNEL = env.get_int("CONTRIBUTION_CHANNEL_ID")  # Chanel to use for contribution check
