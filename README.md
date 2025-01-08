# X-mcp: Bridging Twitter and AI with the Model Context Protocol

This document provides a comprehensive guide to using the `x-mcp` server. This server acts as a bridge, enabling Large Language Models (LLMs) and AI applications to interact with Twitter using the Model Context Protocol (MCP) through the Twikit library.

## Understanding the Model Context Protocol (MCP)

The Model Context Protocol (MCP) is an open standard that allows AI applications to seamlessly connect with external data sources and tools. It provides a structured way for these applications to access, utilize, and even update information from various sources.

**Key Concepts of MCP:**

*   **MCP Hosts (Clients):** These are AI applications, such as Claude, that use LLMs and need to access external resources through MCP.
*   **MCP Servers:** These are programs that expose specific functionalities through the MCP protocol, allowing access to data sources and tools (like this `x-mcp` server).
*   **Resources:**  These represent file-like data that can be read by the LLM. Examples are API responses or file contents.
*   **Tools:** These are functions that the LLM can call (with user approval) to perform actions like searching data or posting tweets.
*   **Prompts:** These are pre-written templates that help users achieve specific tasks using the LLM.

In essence, MCP creates a standardized way for LLMs to interact with the world beyond their training data, addressing the challenge of information silos and fragmented integrations.

## Setup

1.  **Clone Repository:**
    ```bash
    git clone https://github.com/lord-dubious/x-mcp
    cd x-mcp
    ```
2.  **Configure MCP:** Add the following configuration to your MCP settings file. This tells your MCP host (e.g., Claude) how to find and use the `x-mcp` server:
    ```json
    {
        "mcpServer": {
            "command": "uvx",
            "args": ["--from", "git+https://github.com/lord-dubious/x-mcp", "x-mcp"],
            "env": {
                "TWITTER_USERNAME": "@your_username",
                "TWITTER_EMAIL": "your_email@example.com",
                "TWITTER_PASSWORD": "your_password",
                "USER_AGENT": "optional user agent",
                "CAPSOLVER_API_KEY": "optional capsolver api key"
            }
        }
    }
    ```
    *   **Credentials:** Replace `@your_username`, `your_email@example.com`, and `your_password` with your actual Twitter account credentials.
    *   **Optional Settings:**
        *   `USER_AGENT`:  You can set a custom user agent for API requests.
        *   `CAPSOLVER_API_KEY`: If required, add an API key for CAPTCHA solving.
    *   **Note:** The `uvx` command is used here to manage the server, which is typical for MCP setups.
3.  **Start Server:** Once configured, the MCP server will automatically start when your MCP host application is launched.

## Available Tools

This `x-mcp` server provides a set of tools for interacting with Twitter via the Twikit library. These tools can be used by an LLM (or AI application) that supports MCP. Parameters in `()` are optional.

### Timeline Tools

*   **`get_timeline`**: Get the tweets from your "For You" timeline.
    *   `count` (int): The number of tweets to retrieve (default: 20).
*   **`get_latest_timeline`**: Get the tweets from your "Following" timeline.
    *   `count` (int): The number of tweets to retrieve (default: 20).
*   **`get_timeline_with_cursor`**: Retrieves the "For You" timeline with cursor.
    *    `count` (int): The number of tweets to retrieve. Default is 20.
    *    `seen_tweet_ids` (list[str]): A list of tweet IDs that have been seen.
    *   `cursor` (str): A cursor for pagination.
*   **`get_latest_timeline_with_cursor`**: Retrieves the "Following" timeline with cursor.
    *   `count` (int): The number of tweets to retrieve. Default is 20.
    *   `seen_tweet_ids` (list[str]): A list of tweet IDs that have been seen.
    *   `cursor` (str): A cursor for pagination.

### User Tools

*   **`get_user_by_screen_name`**: Fetch user information using their screen name (Twitter handle).
    *   `screen_name` (str): The Twitter username.
*   **`get_user_by_id`**: Fetch user information using their user ID.
    *   `user_id` (str): The user ID.
*   **`get_user_tweets`**: Retrieve tweets from a specific user's timeline.
    *   `username` (str): The Twitter handle (without the `@`).
    *   `tweet_type` (str): The type of tweets to retrieve ('Tweets', 'Replies', 'Media', 'Likes') (default: 'Tweets').
    *   `count` (int): The number of tweets to retrieve (default: 10).
*   **`get_user_tweets_with_cursor`**: Fetches tweets from a specific user’s timeline with cursor.
    *  `user_id` (str): The ID of the Twitter user whose tweets to retrieve.
    *   `tweet_type` (str): The type of tweets to retrieve. Default is 'Tweets'.
    *    `count` (int): The number of tweets to retrieve. Default is 40.
    *   `cursor` (str): The cursor for fetching the next set of results.
*   **`get_user_followers`**: Retrieves a list of followers for a given user.
    *   `user_id` (str): The ID of the user for whom to retrieve followers.
    *   `count` (int): The number of followers to retrieve. Default is 20.
    *   `cursor` (str): A string indicating the position of the cursor for pagination.
*   **`get_latest_followers`**: Retrieves the latest followers.
    *   `user_id` (str): The ID of the user for whom to return results.
    *    `screen_name` (str): The screen name of the user for whom to return results.
    *    `count` (int): The maximum number of IDs to retrieve. Default is 200.
    *   `cursor` (str): A string indicating the position of the cursor for pagination.
*   **`get_latest_friends`**: Retrieves the latest friends (following users).
    *    `user_id` (str): The ID of the user for whom to return results.
    *   `screen_name` (str): The screen name of the user for whom to return results.
    *   `count` (int): The maximum number of IDs to retrieve. Default is 200.
    *    `cursor` (str): A string indicating the position of the cursor for pagination.
*   **`get_user_verified_followers`**: Retrieves a list of verified followers for a given user.
    *   `user_id` (str): The ID of the user for whom to retrieve verified followers.
    *   `count` (int): The number of verified followers to retrieve. Default is 20.
    *    `cursor` (str): A string indicating the position of the cursor for pagination.
*   **`get_user_followers_you_know`**: Retrieves a list of common followers.
    *   `user_id` (str): The ID of the user for whom to retrieve followers you might know.
    *    `count` (int): The number of followers you might know to retrieve. Default is 20.
    *   `cursor` (str): A string indicating the position of the cursor for pagination.
*   **`get_user_following`**: Retrieves a list of users whom the given user is following.
    *   `user_id` (str): The ID of the user for whom to retrieve the following users.
    *   `count` (int): The number of following users to retrieve. Default is 20.
    *   `cursor` (str): A string indicating the position of the cursor for pagination.
*   **`get_user_subscriptions`**: Retrieves a list of users to which the specified user is subscribed.
    *   `user_id` (str): The ID of the user for whom to retrieve subscriptions.
    *   `count` (int): The number of subscriptions to retrieve. Default is 20.
    *   `cursor` (str): A string indicating the position of the cursor for pagination.
*   **`get_followers_ids`**: Fetches the IDs of the followers of a specified user.
    *   `user_id` (str): The ID of the user for whom to return results.
    *   `screen_name` (str): The screen name of the user for whom to return results.
    *   `count` (int): The maximum number of IDs to retrieve. Default is 5000.
    *    `cursor` (str): A string indicating the position of the cursor for pagination.
*   **`get_friends_ids`**: Fetches the IDs of the friends (following users) of a specified user.
    *   `user_id` (str): The ID of the user for whom to return results.
    *   `screen_name` (str): The screen name of the user for whom to return results.
    *   `count` (int): The maximum number of IDs to retrieve. Default is 5000.
    *   `cursor` (str): A string indicating the position of the cursor for pagination.
*   **`get_highlights_tweets`**: Retrieves highlighted tweets from a user’s timeline.
    *  `user_id` (str): The ID of the user for whom to retrieve highlighted tweets.
    *   `count` (int): The number of tweets to retrieve. Default is 20.
    *   `cursor` (str): A string indicating the position of the cursor for pagination.
*   **`get_user_id`**: Retrieves the user ID associated with the authenticated account.
*   **`get_user`**: Retrieve detailed information about the authenticated user.

### Tweet Tools

*   **`get_tweet_by_id`**: Fetches a tweet by tweet ID.
    *   `tweet_id` (str): The ID of the tweet.
    *   `cursor` (str): Token to retrieve more tweets.
*   **`get_scheduled_tweets`**: Retrieves scheduled tweets.
*   **`get_retweeters`**: Retrieve users who retweeted a specific tweet.
    *   `tweet_id` (str): The tweet ID.
    *   `count` (int): The maximum number of users to retrieve (default: 40).
    *   `cursor` (str): A string indicating the position of the cursor for pagination.
*   **`get_favoriters`**: Retrieve users who favorited a specific tweet.
    *   `tweet_id` (str): The tweet ID.
    *   `count` (int): The maximum number of users to retrieve (default: 40).
    *   `cursor` (str): A string indicating the position of the cursor for pagination.
*   **`get_community_note`**: Fetches a community note by ID.
    *   `note_id` (str): The community note ID.
*   **`post_tweet`**: Post a tweet with optional media, reply, and tags.
    *   `text` (str): The text content of the tweet.
    *   `media_paths` (list[str]): A list of file paths to media to attach to the tweet.
    *   `reply_to` (str): The ID of the tweet to reply to.
    *   `tags` (list[str]): A list of tags to include in the tweet (will be converted to mentions).
*   **`delete_tweet`**: Delete a tweet by its ID.
    *   `tweet_id` (str): The ID of the tweet to delete.
*   **`create_media_metadata`**: Adds metadata to uploaded media.
    *   `media_id` (str): The media id for which to create metadata.
    *   `alt_text` (str): Alternative text for the media.
    *   `sensitive_warning` (list[str]): A list of sensitive content warnings for the media.
*   **`create_poll`**: Creates a poll and returns card-uri.
    *   `choices` (list[str]): A list of choices for the poll. Maximum of 4 choices.
    *   `duration_minutes` (int): The duration of the poll in minutes.
*   **`vote`**: Vote on a poll with the selected choice.
    *   `selected_choice` (str): The label of the selected choice for the vote.
    *   `card_uri` (str): The URI of the poll card.
    *   `tweet_id` (str): The ID of the original tweet containing the poll.
    *   `card_name` (str): The name of the poll card.
*   **`create_scheduled_tweet`**: Schedules a tweet to be posted at a specified timestamp.
    *   `scheduled_at` (int): The timestamp when the tweet should be scheduled for posting.
    *   `text` (str): The text content of the tweet.
    *   `media_paths` (list[str]): A list of media IDs to be attached to the tweet.
*   **`delete_scheduled_tweet`**: Delete a scheduled tweet.
    *   `tweet_id` (str): The ID of the scheduled tweet to delete.
*   **`bookmark_tweet`**: Adds the tweet to bookmarks.
    *   `tweet_id` (str): The ID of the tweet to be bookmarked.
    *   `folder_id` (str): The ID of the folder to add the bookmark to.
*   **`delete_bookmark`**: Removes the tweet from bookmarks.
    *   `tweet_id` (str): The ID of the tweet to be removed from bookmarks.
*   **`delete_all_bookmarks`**: Deleted all bookmarks.

### DM Tools

*   **`send_dm`**: Send a direct message to a user.
    *   `user_id` (str): The ID of the user to send the DM to.
    *   `message` (str): The text content of the DM.
    *   `media_path` (str): The file path to media to attach to the DM.
*   **`delete_dm`**: Delete a direct message by its ID.
    *   `message_id` (str): The ID of the DM to delete.
*   **`get_dm_history`**: Retrieves the DM conversation history with a specific user.
    *   `user_id` (str): The ID of the user with whom the DM conversation history will be retrieved.
    *   `max_id` (str): If specified, retrieves messages older than the specified max_id.
*   **`send_dm_to_group`**: Sends a message to a group.
    *   `group_id` (str): The ID of the group in which the direct message will be sent.
    *   `text` (str): The text content of the direct message.
    *   `media_id` (str): The media ID associated with any media content to be included in the message.
    *   `reply_to` (str): Message ID to reply to.
*   **`get_group_dm_history`**: Retrieves the DM conversation history in a group.
    *   `group_id` (str): The ID of the group in which the DM conversation history will be retrieved.
    *   `max_id` (str): If specified, retrieves messages older than the specified max_id.
*   **`get_group`**: Fetches a group by ID.
    *   `group_id` (str): The ID of the group to retrieve information for.
*   **`add_members_to_group`**: Adds members to a group.
    *   `group_id` (str): ID of the group to which the member is to be added.
    *   `user_ids` (list[str]): List of IDs of users to be added.
*   **`change_group_name`**: Changes group name.
    *   `group_id` (str): ID of the group to be renamed.
    *   `name` (str): New name.
*   **`add_reaction_to_message`**: Adds a reaction emoji to a specific message in a conversation.
    *   `message_id` (str): The ID of the message to which the reaction emoji will be added.
    *   `conversation_id` (str): The ID of the conversation containing the message.
    *   `emoji` (str): The emoji to be added as a reaction.
*   **`remove_reaction_from_message`**: Remove a reaction from a message.
    *   `message_id` (str): The ID of the message from which to remove the reaction.
    *   `conversation_id` (str): The ID of the conversation where the message is located.
    *   `emoji` (str): The emoji to remove as a reaction.

### Other Tools

*   **`update_user`**: Updates the user.
*   **`logout`**: Logs out of the currently logged-in account.
*   **`unlock`**: Unlocks the account using the provided CAPTCHA solver.
*   **`get_cookies`**: Get the cookies.
*   **`save_cookies`**: Save cookies to file in json format.
    *   `path` (str): The path to the file where the cookie will be stored.
*   **`set_cookies`**: Sets cookies.
    *   `cookies` (str): The cookies to be set as key value pair.
    *   `clear_cookies` (bool): Whether to clear existing cookies. Default is False.
*   **`load_cookies`**: Loads cookies from a file.
    *   `path` (str): Path to the file where the cookie is stored.

## Key Takeaways

*   This server utilizes the Model Context Protocol (MCP) to enable communication between LLMs and the Twitter API.
*   It exposes a variety of tools for both reading and writing data on Twitter.
*   The server runs using `uvx`, which helps manage the server's dependencies and execution.
*   Remember to use your actual Twitter credentials to configure the server.
