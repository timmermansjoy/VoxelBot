import os
from hata import ClientWrapper, Embed
from hata.ext.slash import abort
from github import Github

ALL = ClientWrapper()

# Initialize the GitHub client with your access token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise EnvironmentError("Please set the GITHUB_TOKEN environment variable.")
github_client = Github(GITHUB_TOKEN)

REPO_NAME = "voxel51/fiftyone"

# Define the available metrics
METRICS = {
    "overview": "Overview of key metrics",
    "pull_requests": "Recent Pull Requests",
}


def get_repository(repo_name):
    """Fetches the repository object."""
    try:
        return github_client.get_repo(repo_name)
    except Exception as e:
        abort(f"Repository '{repo_name}' not found or an error occurred: {e}")


def get_overview(repo):
    """Returns an overview of key metrics."""
    stars = repo.stargazers_count
    forks = repo.forks_count
    watchers = repo.watchers_count
    issues = repo.open_issues_count
    prs = repo.get_pulls(state="open").totalCount
    description = repo.description or "No description."
    url = repo.html_url
    contributors = repo.get_contributors().totalCount
    latest_release = repo.get_latest_release().tag_name
    size_mb = round(repo.size * 1e-6, 2)
    license = repo.get_license().license

    embed = Embed(title=repo.full_name, url=url)
    description = (
        f"**Description:** {description}\n"
        f"**Stars:** {stars}\n"
        f"**Forks:** {forks}\n"
        f"**Watchers:** {watchers}\n"
        f"**Open Issues:** {issues}\n"
        f"**Open Pull Requests:** {prs}\n"
        f"**Number of Contributors:** {contributors}\n"
        f"**Latest Release:** {latest_release}\n"
        f"**Repository Size:** {size_mb} MB\n"
        f"**License:** {license.name}"
    )
    embed.description = description
    return embed


def get_recent_pull_requests(repo, limit=5):
    """Returns the 5 most recent open pull requests."""
    pulls = repo.get_pulls(state="open")[:limit]
    pull_list = "\n".join([f"- [{pr.title}]({pr.html_url})" for pr in pulls])
    return f"**Recent Pull Requests:**\n{pull_list}"


@ALL.interactions(is_global=True, wait_for_acknowledgement=True)
async def repo_metrics(metric: ("str", "Metric to retrieve")):  # type: ignore # noqa: F722
    """Provides specific metric(s) for the voxel51/fiftyone repository."""
    repo = get_repository(REPO_NAME)

    if metric == "overview":
        response = get_overview(repo)
    elif metric == "pull_requests":
        response = get_recent_pull_requests(repo)
    else:
        abort("Invalid metric.")

    return response


@repo_metrics.autocomplete("metric")
async def metric_autocomplete(value):
    if not value:
        return list(METRICS.keys())
    value_lower = value.lower()
    return [metric for metric in METRICS.keys() if metric.startswith(value_lower)]
