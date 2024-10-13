import sqlite3
import time


# Function to retrieve activity (either all users or a specific user)
def dump_activity(username=None):
    # Ensure you are using the correct path to the database
    with sqlite3.connect("../persist/voxelbot.db") as connection:
        c = connection.cursor()

        # SQL query for all users or a specific user
        if username:
            query = """
                SELECT content, username, timestamp, action
                FROM logging_messages
                WHERE username = ? AND content IS NOT NULL
                ORDER BY timestamp
            """
            params = (username,)
        else:
            query = """
                SELECT content, username, timestamp, action
                FROM logging_messages
                WHERE content IS NOT NULL
                ORDER BY timestamp
            """
            params = ()

        # Execute the query and fetch the results
        messages = c.execute(query, params).fetchall()

    # Write the activity log to messages.txt
    with open("server.log", "w") as f:
        for message in messages:
            content, username, timestamp, action = message

            # Convert the Unix timestamp to a human-readable format
            message_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

            # Replace newline characters in the message content with spaces
            content_cleaned = " ".join(content.split("\n"))

            # Check if the message action includes an update with old and new content
            if "updated" in action:
                # Parse the action to extract the old -> new structure
                action_parts = action.split(": ", 1)
                if len(action_parts) == 2:
                    old_new = action_parts[1]  # Extract the old -> new part
                    f.write(f"[{message_date}] {username} edited a message: {old_new}\n")
            # Handle message deletions (no content in this case)
            elif action == "delete":
                f.write(f"[{message_date}] {username} deleted a message\n")
            else:
                # Write the formatted message to the file (creation or normal message)
                f.write(f"[{message_date}] {username}: {content_cleaned}\n")


# Example usage:

# Dump all users' activity
dump_activity()

# Dump activity for a specific user (replace 'JohnDoe' with the actual username)
dump_activity("JohnDoe")
