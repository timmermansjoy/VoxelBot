import pathlib

from hata.ext.slash import abort


from hata import ClientWrapper


ALL = ClientWrapper()


# load all tags from the tags folder
TAGS = {}
for file in (pathlib.Path(__file__).parent.parent.parent / "assets/faqs/").iterdir():
    TAGS[file.stem] = file.read_text()
TAG_NAMES = list(TAGS)


@ALL.interactions(is_global=True, wait_for_acknowledgement=True)
async def faq(tag: ("str", "Tag to send")):  # type: ignore # noqa: F722
    """Sends a short snippet of information."""
    if tag not in TAGS:
        abort(f"Tag `{tag}` not found.")
    return TAGS[tag]


@faq.autocomplete("tag")
async def tags_autocomplete(value):
    if value is None:
        return TAG_NAMES[:25]
    return [tag for tag in TAG_NAMES if tag.startswith(value.casefold())]
