# X-mcp: Bridging Twitter and AI with the Model Context Protocol

This document provides a comprehensive guide to using the `x-mcp` server. This server acts as a bridge, enabling Large Language Models (LLMs) and AI applications to interact with Twitter using the Model Context Protocol (MCP) through the Twikit library.

## Twitter MCP Server

A FastMCP implementation for interacting with Twitter's API using the Twikit library. This server provides a comprehensive set of tools for managing Twitter accounts, posting tweets, managing direct messages, and more.

## Table of Contents

1. [Setup](#setup)
2. [Quick Start](#quick-start)
3. [Available Functions](#available-functions)
   - [Authentication & Account Management](#authentication-account-management)
   - [User Management](#user-management)
   - [Tweet Management](#tweet-management)
   - [Timeline & Search](#timeline-search)
   - [Direct Messages](#direct-messages)
   - [Analytics & Lists](#analytics-lists)
   - [Other Tools](#other-tools)
4. [Rate Limits](#rate-limits)
5. [Error Handling](#error-handling)
6. [Contributing](#contributing)
7. [License](#license)

## Setup

1. **Clone Repository:**

   ```bash
   git clone https://github.com/lord-dubious/x-mcp
   cd x-mcp
   ```

2. **Configure MCP:** Add the following configuration to your MCP settings file. This tells your MCP host (e.g., Claude) how to find and use the `x-mcp` server:

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

   - **Credentials:** Replace `@your_username`, `your_email@example.com`, and `your_password` with your actual Twitter account credentials.
   - **Optional Settings:**
     - `USER_AGENT`: You can set a custom user agent for API requests.
     - `CAPSOLVER_API_KEY`: If required, add an API key for CAPTCHA solving.
   - **Note:** The `uvx` command is used here to manage the server, which is typical for MCP setups.
3. **Start Server:** Once configured, the MCP server will automatically start when your MCP host application is launched.

## 🚀 Quick Start

No additional setup is required as the environment variables are set in the MCP configuration and dependencies are managed by `uvx`. Simply follow the setup instructions above to get started.

## 📚 Available Functions

### 🔑 Authentication & Account Management

| Function | Description | Parameters |
|----------|-------------|------------|
| `get_twitter_client` | Initialize and return an authenticated Twitter client | - |
| `unlock` | Unlocks the account using the provided CAPTCHA solver | - |
| `update_user` | Updates the user | - |

### 👤 User Management

| Function | Description | Parameters |
|----------|-------------|------------|
| `get_user_profile` | Get detailed profile information for a user | `user_id` |
| `get_user_by_screen_name` | Fetches a user by screen name | `screen_name` |
| `get_user_by_id` | Fetches a user by ID | `user_id` |
| `get_user_followers` | Retrieves a list of followers for a given user | `user_id`, `count?`, `cursor?` |
| `get_user_following` | Retrieves a list of users whom the given user is following | `user_id`, `count?`, `cursor?` |
| `get_user_followers_you_know` | Retrieves a list of common followers | `user_id`, `count?`, `cursor?` |
| `get_user_subscriptions` | Retrieves a list of users to which the specified user is subscribed | `user_id`, `count?`, `cursor?` |

### 📝 Tweet Management

| Function | Description | Parameters |
|----------|-------------|------------|
| `post_tweet` | Post a tweet with optional media, reply, and tags | `text`, `media_paths?`, `reply_to?`, `tags?` |
| `delete_tweet` | Delete a tweet by its ID | `tweet_id` |
| `get_tweet_details` | Get detailed information about a specific tweet | `tweet_id` |
| `create_poll_tweet` | Create a tweet with a poll | `text`, `choices`, `duration_minutes?` |
| `vote_on_poll` | Vote on a poll | `tweet_id`, `choice` |
| `favorite_tweet` | Favorites a tweet | `tweet_id` |
| `unfavorite_tweet` | Unfavorites a tweet | `tweet_id` |
| `bookmark_tweet` | Adds the tweet to bookmarks | `tweet_id`, `folder_id?` |
| `delete_bookmark` | Removes the tweet from bookmarks | `tweet_id` |
| `delete_all_bookmarks` | Deleted all bookmarks | - |

### 🔍 Timeline & Search

| Function | Description | Parameters |
|----------|-------------|------------|
| `get_timeline` | Get tweets from your home timeline (For You) | `count?`, `seen_tweet_ids?`, `cursor?` |
| `get_latest_timeline` | Get tweets from your home timeline (Following) | `count?` |
| `search_twitter` | Search twitter with a query. Sort by 'Top' or 'Latest' | `query`, `product?`, `count?`, `cursor?` |
| `get_trends` | Retrieves trending topics on Twitter | `category?`, `count?` |
| `get_highlights_tweets` | Retrieves highlighted tweets from a user’s timeline | `user_id`, `count?`, `cursor?` |
| `get_user_mentions` | Get tweets mentioning a specific user | `user_id`, `count?`, `cursor?` |

### 💬 Direct Messages

| Function | Description | Parameters |
|----------|-------------|------------|
| `send_dm` | Send a direct message to a user | `user_id`, `message`, `media_path?` |
| `delete_dm` | Delete a direct message by its ID | `message_id` |
| `get_dm_history` | Retrieves the DM conversation history with a specific user | `user_id`, `max_id?` |
| `send_dm_to_group` | Sends a message to a group | `group_id`, `text`, `media_id?`, `reply_to?` |
| `add_reaction_to_message` | Adds a reaction emoji to a specific message in a conversation | `message_id`, `conversation_id`, `emoji` |
| `remove_reaction_from_message` | Remove a reaction from a message | `message_id`, `conversation_id`, `emoji` |

### 📊 Analytics & Lists

| Function | Description | Parameters |
|----------|-------------|------------|
| `get_retweeters` | Retrieve users who retweeted a specific tweet | `tweet_id`, `count?`, `cursor?` |
| `get_favoriters` | Retrieve users who favorited a specific tweet | `tweet_id`, `count?`, `cursor?` |
| `get_followers_ids` | Fetches the IDs of the followers of a specified user | `user_id?`, `screen_name?`, `count?`, `cursor?` |
| `get_friends_ids` | Fetches the IDs of the friends (following users) of a specified user | `user_id?`, `screen_name?`, `count?`, `cursor?` |

### 🛠️ Other Tools

| Function | Description | Parameters |
|----------|-------------|------------|
| `get_place` | Retrieves a place by ID | `place_id` |
| `search_geo` | Search for places that can be attached to a Tweet | `lat?`, `long?`, `query?`, `ip?`, `granularity?`, `max_results?` |

## ⚡ Rate Limits

The server implements rate limiting to comply with Twitter's API restrictions:

| Action Type | Limit | Time Window |
|-------------|-------|-------------|
| Tweet actions | 300 | 15 minutes |
| DM actions | 1000 | 15 minutes |
| Follow actions | 400 | 24 hours |
| Like actions | 1000 | 24 hours |

## 🔧 Error Handling

All API responses follow this standardized format:

```python
{
    "success": bool,
    "data": dict,    # Present on success
    "error": str,    # Present on failure
    "error_type": str  # Present on failure
}
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
