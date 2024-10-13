# Voxelbot

Voxelbot is a versatile Discord bot designed for the FiftyOne Discord community, utilizing the [Hata](https://github.com/HuyaneMatsu/hata) framework. It offers a range of features for server management, user interaction, and community engagement.

## Features

Voxelbot’s functionality is modular, with each feature residing in its own plugin located under `voxelbot/plugins`. Below is an overview of the core plugins:

- **code_metrics.py**: Tracks and provides metrics related to the fiftyone repo. Useful for monitoring development activity within the Discord server.
- **faqs.py**: Manages a frequently asked questions (FAQ) system, allowing server members to easily find answers to common questions.
- **moderation_menu.py**: ability to softkick someone Bans a user, then unbans them, deleting their messages in the process.
- **easy_github_contribution.py**: Simplifies the verification of contributors to open-source projects.
- **logging.py**: Logs the activity on the discord to monitor any bad behaviour
- **misc.py**: Some easy simple commands

## Installation

```sh
git clone https://github.com/yourusername/voxelbot.git
cd voxelbot
```

Configure the bot: Set up your required vriables in the `.env` file inside voxelbot or export them in your shell.

### Running in docker

The simplest and most efficient way to run Voxelbot is through Docker. We've provided a `docker-run.sh` script that sets up and runs the bot inside a Docker container. This ensures that the bot runs in a consistent environment without needing to manually manage dependencies.

To run the bot using Docker:

```sh
./docker-run.sh
```

### Running natively

Install the dependencies:

```sh
python3 -m pip install .
```

Running the bot: You need to run the bot directly from the source directory

```sh
python3 -m voxelbot help
```
