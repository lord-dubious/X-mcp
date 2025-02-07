from typing import Any, Dict, List, Optional, Union
import time
import json
import logging
from fastmcp import FastMCP
from fastmcp.server import Context
import twikit
import os
from pathlib import Path
import logging
import time
import json

# Create an MCP server with proper metadata
mcp = FastMCP()

logger = logging.getLogger(__name__)
httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.WARNING)

USERNAME = os.getenv("TWITTER_USERNAME")
EMAIL = os.getenv("TWITTER_EMAIL")
PASSWORD = os.getenv("TWITTER_PASSWORD")
USER_AGENT = os.getenv("USER_AGENT")
CAPSOLVER_API_KEY = os.getenv("CAPSOLVER_API_KEY")
COOKIES_PATH = Path.home() / ".x-mcp" / "cookies.json"

# Rate limit tracking
RATE_LIMITS: Dict[str, List[float]] = {}
RATE_LIMIT_WINDOW = 15 * 60  # 15 minutes in seconds


def convert_tweets_to_markdown(tweets: Any) -> str:
    """Convert tweet objects to markdown format."""
    try:
        tweet_list = []
        for tweet in tweets:
            tweet_text = tweet.text.replace("\n", "\n> ")
            tweet_list.append(f"Tweet ID: {tweet.id}\n> {tweet_text}\n")
        return "\n".join(tweet_list)
    except Exception as e:
        logger.error(f"Failed to convert tweets to markdown: {e}")
        return str(tweets)


async def get_twitter_client() -> twikit.Client:
    """Initialize and return an authenticated Twitter client."""
    captcha_solver = None
    if CAPSOLVER_API_KEY:
        captcha_solver = twikit._captcha.capsolver.Capsolver(api_key=CAPSOLVER_API_KEY)
    client = twikit.Client(
        "en-US", user_agent=USER_AGENT, captcha_solver=captcha_solver
    )

    if COOKIES_PATH.exists():
        client.load_cookies(COOKIES_PATH)
    else:
        try:
            await client.login(
                auth_info_1=USERNAME, auth_info_2=EMAIL, password=PASSWORD
            )
        except Exception as e:
            logger.error(f"Failed to login: {e}")
            raise
        COOKIES_PATH.parent.mkdir(parents=True, exist_ok=True)
        client.save_cookies(COOKIES_PATH)

    return client


def check_rate_limit(endpoint: str) -> bool:
    """Check if we're within rate limits for a given endpoint."""
    now = time.time()
    if endpoint not in RATE_LIMITS:
        RATE_LIMITS[endpoint] = []

    # Remove old timestamps
    RATE_LIMITS[endpoint] = [
        t for t in RATE_LIMITS[endpoint] if now - t < RATE_LIMIT_WINDOW
    ]

    # Check limits based on endpoint
    limits = {
        "tweet": 300,  # 300 tweets per 15 minutes
        "dm": 1000,  # 1000 DMs per 15 minutes
        "follow": 400,  # 400 follows per 24 hours
        "like": 1000,  # 1000 likes per 24 hours
    }

    limit = limits.get(endpoint, 100)  # Default to 100 for unknown endpoints
    return len(RATE_LIMITS[endpoint]) < limit


@mcp.tool()
async def search_user(
    query: str, count: int = 20, cursor: Optional[str] = None
) -> str:
    """Searches for users based on the provided query."""
    try:
        client = await get_twitter_client()
        users = await client.search_user(query, count=count, cursor=cursor)
        return str(users)  # Assuming you want to return the raw result for now
    except Exception as e:
        logger.error(f"Failed to search users: {e}")
        return f"Failed to search users: {e}"


@mcp.tool(
    name="search_twitter",
    description="Search twitter with a query. Sort by 'Top' or 'Latest'"
)
async def search_twitter(ctx: Context, query: str, product: str = "Top", count: int = 20, cursor: Optional[str] = None) -> str:
    """Search twitter with a query. Sort by 'Top' or 'Latest'"""
    try:
        client = await get_twitter_client()
        tweets = await client.search_tweet(
            query, product=product, count=count, cursor=cursor
        )
        return convert_tweets_to_markdown(tweets)
    except Exception as e:
        logger.error(f"Failed to search tweets: {e}")
        return f"Failed to search tweets: {e}"


@mcp.tool(
    name="get_user_tweets",
    description="Get tweets from a specific user's timeline. Takes user_id, tweet_type (default: Tweets), count (default: 40), and cursor (optional)"
)
async def get_user_tweets(
    ctx: Context,
    user_id: str,
    tweet_type: str = "Tweets",
    count: int = 40,
    cursor: Optional[str] = None,
) -> str:
    """Get tweets from a specific user's timeline."""
    try:
        client = await get_twitter_client()
        tweets = await client.get_user_tweets(
            user_id=user_id, tweet_type=tweet_type, count=count, cursor=cursor
        )
        return convert_tweets_to_markdown(tweets)
    except Exception as e:
        logger.error(f"Failed to get user tweets: {e}")
        return f"Failed to get user tweets: {e}"


@mcp.tool(
    name="get_timeline",
    description="Get tweets from your home timeline (For You). Takes count (default: 20), seen_tweet_ids (optional), and cursor (optional)"
)
async def get_timeline(
    ctx: Context,
    count: int = 20,
    seen_tweet_ids: Optional[List[str]] = None,
    cursor: Optional[str] = None,
) -> str:
    """Get tweets from your home timeline (For You)."""
    try:
        client = await get_twitter_client()
        tweets = await client.get_timeline(
            count=count, seen_tweet_ids=seen_tweet_ids, cursor=cursor
        )
        return convert_tweets_to_markdown(tweets)
    except Exception as e:
        logger.error(f"Failed to get timeline: {e}")
        return f"Failed to get timeline: {e}"


@mcp.tool(
    name="get_latest_timeline",
    description="Get tweets from your home timeline (Following). Takes count (default: 20), seen_tweet_ids (optional), and cursor (optional)"
)
async def get_latest_timeline(
    ctx: Context,
    count: int = 20,
    seen_tweet_ids: Optional[List[str]] = None,
    cursor: Optional[str] = None,
) -> str:
    """Get tweets from your home timeline (Following)."""
    try:
        client = await get_twitter_client()
        tweets = await client.get_latest_timeline(
            count=count, seen_tweet_ids=seen_tweet_ids, cursor=cursor
        )
        return convert_tweets_to_markdown(tweets)
    except Exception as e:
        logger.error(f"Failed to get latest timeline: {e}")
        return f"Failed to get latest timeline: {e}"


@mcp.tool()
async def post_tweet(
    text: str,
    media_paths: Optional[List[str]] = None,
    reply_to: Optional[str] = None,
    tags: Optional[List[str]] = None,
) -> str:
    """Post a tweet with optional media, reply, and tags."""
    try:
        if not check_rate_limit("tweet"):
            return "Rate limit exceeded for tweets. Please wait before posting again."

        client = await get_twitter_client()

        # Handle tags by converting to mentions
        if tags:
            mentions = " ".join(f"@{tag.lstrip('@')}" for tag in tags)
            text = f"{text}\n{mentions}"

        # Upload media if provided
        media_ids = []
        if media_paths:
            for path in media_paths:
                media_id = await client.upload_media(path, wait_for_completion=True)
                media_ids.append(media_id)

        # Create the tweet
        tweet = await client.create_tweet(
            text=text, media_ids=media_ids if media_ids else None, reply_to=reply_to
        )
        RATE_LIMITS["tweet"].append(time.time())
        return f"Successfully posted tweet: {tweet.id}"
    except Exception as e:
        logger.error(f"Failed to post tweet: {e}")
        return f"Failed to post tweet: {e}"


@mcp.tool()
async def delete_tweet(tweet_id: str) -> str:
    """Delete a tweet by its ID."""
    try:
        client = await get_twitter_client()
        await client.delete_tweet(tweet_id)
        return f"Successfully deleted tweet {tweet_id}"
    except Exception as e:
        logger.error(f"Failed to delete tweet: {e}")
        return f"Failed to delete tweet: {e}"


@mcp.tool()
async def send_dm(user_id: str, message: str, media_path: Optional[str] = None) -> str:
    """Send a direct message to a user."""
    try:
        if not check_rate_limit("dm"):
            return "Rate limit exceeded for DMs. Please wait before sending again."

        client = await get_twitter_client()

        media_id = None
        if media_path:
            media_id = await client.upload_media(media_path, wait_for_completion=True)

        await client.send_dm(user_id=user_id, text=message, media_id=media_id)
        RATE_LIMITS["dm"].append(time.time())
        return f"Successfully sent DM to user {user_id}"
    except Exception as e:
        logger.error(f"Failed to send DM: {e}")
        return f"Failed to send DM: {e}"


@mcp.tool()
async def delete_dm(message_id: str) -> str:
    """Delete a direct message by its ID."""
    try:
        client = await get_twitter_client()
        await client.delete_dm(message_id)
        return f"Successfully deleted DM {message_id}"
    except Exception as e:
        logger.error(f"Failed to delete DM: {e}")
        return f"Failed to delete DM: {e}"


@mcp.tool()
async def logout() -> str:
    """Logs out of the currently logged-in account."""
    try:
        client = await get_twitter_client()
        await client.logout()
        return "Successfully logged out"
    except Exception as e:
        logger.error(f"Failed to logout: {e}")
        return f"Failed to logout: {e}"


@mcp.tool()
async def unlock() -> str:
    """Unlocks the account using the provided CAPTCHA solver."""
    try:
        client = await get_twitter_client()
        await client.unlock()
        return "Successfully unlocked account"
    except Exception as e:
        logger.error(f"Failed to unlock account: {e}")
        return f"Failed to unlock account: {e}"


@mcp.tool()
async def get_cookies() -> str:
    """Get the cookies."""
    try:
        client = await get_twitter_client()
        cookies = client.get_cookies()
        return str(cookies)
    except Exception as e:
        logger.error(f"Failed to get cookies: {e}")
        return f"Failed to get cookies: {e}"


@mcp.tool()
async def save_cookies(path: str) -> str:
    """Save cookies to file in json format."""
    try:
        client = await get_twitter_client()
        client.save_cookies(path)
        return f"Successfully saved cookies to {path}"
    except Exception as e:
        logger.error(f"Failed to save cookies: {e}")
        return f"Failed to save cookies: {e}"


@mcp.tool()
async def set_cookies(
    cookies: str, clear_cookies: bool = False
) -> str:
    """Sets cookies."""
    try:
        client = await get_twitter_client()
        import json

        client.set_cookies(json.loads(cookies), clear_cookies)
        return "Successfully set cookies"
    except Exception as e:
        logger.error(f"Failed to set cookies: {e}")
        return f"Failed to set cookies: {e}"


@mcp.tool()
async def load_cookies(path: str) -> str:
    """Loads cookies from a file."""
    try:
        client = await get_twitter_client()
        client.load_cookies(path)
        return f"Successfully loaded cookies from {path}"
    except Exception as e:
        logger.error(f"Failed to load cookies: {e}")
        return f"Failed to load cookies: {e}"


@mcp.tool()
async def set_delegate_account(user_id: str) -> str:
    """Sets the account to act as."""
    try:
        client = await get_twitter_client()
        client.set_delegate_account(user_id)
        return f"Successfully set delegate account to {user_id}"
    except Exception as e:
        logger.error(f"Failed to set delegate account: {e}")
        return f"Failed to set delegate account: {e}"


@mcp.tool()
async def get_user_id() -> str:
    """Retrieves the user ID associated with the authenticated account."""
    try:
        client = await get_twitter_client()
        user_id = await client.user_id()
        return user_id
    except Exception as e:
        logger.error(f"Failed to get user ID: {e}")
        return f"Failed to get user ID: {e}"


@mcp.tool()
async def get_user() -> str:
    """Retrieve detailed information about the authenticated user."""
    try:
        client = await get_twitter_client()
        user = await client.user()
        return str(user)
    except Exception as e:
        logger.error(f"Failed to get user: {e}")
        return f"Failed to get user: {e}"


@mcp.tool()
async def get_similar_tweets(tweet_id: str) -> str:
    """Retrieves tweets similar to the specified tweet (Twitter premium only)."""
    try:
        client = await get_twitter_client()
        tweets = await client.get_similar_tweets(tweet_id)
        return convert_tweets_to_markdown(tweets)
    except Exception as e:
        logger.error(f"Failed to get similar tweets: {e}")
        return f"Failed to get similar tweets: {e}"


@mcp.tool()
async def create_media_metadata(
    media_id: str,
    alt_text: Optional[str] = None,
    sensitive_warning: Optional[List[str]] = None,
) -> str:
    """Adds metadata to uploaded media."""
    try:
        client = await get_twitter_client()
        await client.create_media_metadata(media_id, alt_text, sensitive_warning)
        return f"Successfully created media metadata for {media_id}"
    except Exception as e:
        logger.error(f"Failed to create media metadata: {e}")
        return f"Failed to create media metadata: {e}"


@mcp.tool(
    name="create_poll_tweet",
    description="Create a tweet with a poll. Takes text content, list of choices, and optional duration in minutes."
)
async def create_poll_tweet(ctx: Context, text: str, choices: List[str], duration_minutes: int = 1440) -> str:
    """Create a tweet with a poll."""
    try:
        client = await get_twitter_client()
        
        # Create the poll
        card_uri = await client.create_poll(choices, duration_minutes)
        
        # Post the tweet with the poll
        tweet = await client.post_tweet(text, card_uri=card_uri)
        
        return f"Successfully created poll tweet: https://twitter.com/i/status/{tweet.id}"
    except Exception as e:
        logger.error(f"Failed to create poll tweet: {e}")
        return f"Failed to create poll tweet: {e}"


@mcp.tool()
async def vote(
    selected_choice: str,
    card_uri: str,
    tweet_id: str,
    card_name: str,
) -> str:
    """Vote on a poll with the selected choice."""
    try:
        client = await get_twitter_client()
        poll = await client.vote(selected_choice, card_uri, tweet_id, card_name)
        return f"Successfully voted on poll: {poll.id}"
    except Exception as e:
        logger.error(f"Failed to vote on poll: {e}")
        return f"Failed to vote on poll: {e}"


@mcp.tool()
async def create_scheduled_tweet(
    scheduled_at: int,
    text: str = "",
    media_paths: Optional[List[str]] = None,
) -> str:
    """Schedules a tweet to be posted at a specified timestamp."""
    try:
        client = await get_twitter_client()
        media_ids = []
        if media_paths:
            for path in media_paths:
                media_id = await client.upload_media(path, wait_for_completion=True)
                media_ids.append(media_id)
        tweet_id = await client.create_scheduled_tweet(scheduled_at, text, media_ids)
        return f"Successfully scheduled tweet with ID: {tweet_id}"
    except Exception as e:
        logger.error(f"Failed to schedule tweet: {e}")
        return f"Failed to schedule tweet: {e}"


@mcp.tool()
async def get_user_by_screen_name(screen_name: str) -> str:
    """Fetches a user by screen name."""
    try:
        client = await get_twitter_client()
        user = await client.get_user_by_screen_name(screen_name)
        return str(user)
    except Exception as e:
        logger.error(f"Failed to get user by screen name: {e}")
        return f"Failed to get user by screen name: {e}"


@mcp.tool()
async def get_user_by_id(user_id: str) -> str:
    """Fetches a user by ID."""
    try:
        client = await get_twitter_client()
        user = await client.get_user_by_id(user_id)
        return str(user)
    except Exception as e:
        logger.error(f"Failed to get user by ID: {e}")
        return f"Failed to get user by ID: {e}"


@mcp.tool()
async def reverse_geocode(
    lat: float,
    long: float,
    accuracy: Optional[str] = None,
    granularity: Optional[str] = None,
    max_results: Optional[int] = None,
) -> str:
    """Given a latitude and a longitude, searches for up to 20 places."""
    try:
        client = await get_twitter_client()
        places = await client.reverse_geocode(
            lat, long, accuracy, granularity, max_results
        )
        return str(places)
    except Exception as e:
        logger.error(f"Failed to reverse geocode: {e}")
        return f"Failed to reverse geocode: {e}"


@mcp.tool()
async def search_geo(
    lat: Optional[float] = None,
    long: Optional[float] = None,
    query: Optional[str] = None,
    ip: Optional[str] = None,
    granularity: Optional[str] = None,
    max_results: Optional[int] = None,
) -> str:
    """Search for places that can be attached to a Tweet."""
    try:
        client = await get_twitter_client()
        places = await client.search_geo(lat, long, query, ip, granularity, max_results)
        return str(places)
    except Exception as e:
        logger.error(f"Failed to search geo: {e}")
        return f"Failed to search geo: {e}"


@mcp.tool()
async def get_place(place_id: str) -> str:
    """Retrieves a place by ID."""
    try:
        client = await get_twitter_client()
        place = await client.get_place(place_id)
        return str(place)
    except Exception as e:
        logger.error(f"Failed to get place: {e}")
        return f"Failed to get place: {e}"


@mcp.tool()
async def get_tweet_by_id(
    tweet_id: str, cursor: Optional[str] = None
) -> str:
    """Fetches a tweet by tweet ID."""
    try:
        client = await get_twitter_client()
        tweet = await client.get_tweet_by_id(tweet_id, cursor)
        return str(tweet)
    except Exception as e:
        logger.error(f"Failed to get tweet by ID: {e}")
        return f"Failed to get tweet by ID: {e}"


@mcp.tool()
async def get_scheduled_tweets() -> str:
    """Retrieves scheduled tweets."""
    try:
        client = await get_twitter_client()
        tweets = await client.get_scheduled_tweets()
        return str(tweets)
    except Exception as e:
        logger.error(f"Failed to get scheduled tweets: {e}")
        return f"Failed to get scheduled tweets: {e}"


@mcp.tool()
async def delete_scheduled_tweet(tweet_id: str) -> str:
    """Delete a scheduled tweet."""
    try:
        client = await get_twitter_client()
        await client.delete_scheduled_tweet(tweet_id)
        return f"Successfully deleted scheduled tweet {tweet_id}"
    except Exception as e:
        logger.error(f"Failed to delete scheduled tweet: {e}")
        return f"Failed to delete scheduled tweet: {e}"


@mcp.tool()
async def get_retweeters(
    tweet_id: str, count: int = 40, cursor: Optional[str] = None
) -> str:
    """Retrieve users who retweeted a specific tweet."""
    try:
        client = await get_twitter_client()
        retweeters = await client.get_retweeters(tweet_id, count, cursor)
        return convert_tweets_to_markdown(retweeters)
    except Exception as e:
        logger.error(f"Failed to get retweeters: {e}")
        return f"Failed to get retweeters: {e}"


@mcp.tool()
async def get_favoriters(
    tweet_id: str, count: int = 40, cursor: Optional[str] = None
) -> str:
    """Retrieve users who favorited a specific tweet."""
    try:
        client = await get_twitter_client()
        favoriters = await client.get_favoriters(tweet_id, count, cursor)
        return convert_tweets_to_markdown(favoriters)
    except Exception as e:
        logger.error(f"Failed to get favoriters: {e}")
        return f"Failed to get favoriters: {e}"


@mcp.tool()
async def get_community_note(note_id: str) -> str:
    """Fetches a community note by ID."""
    try:
        client = await get_twitter_client()
        note = await client.get_community_note(note_id)
        return str(note)
    except Exception as e:
        logger.error(f"Failed to get community note: {e}")
        return f"Failed to get community note: {e}"


@mcp.tool()
async def favorite_tweet(tweet_id: str) -> str:
    """Favorites a tweet."""
    try:
        client = await get_twitter_client()
        await client.favorite_tweet(tweet_id)
        return f"Successfully favorited tweet {tweet_id}"
    except Exception as e:
        logger.error(f"Failed to favorite tweet: {e}")
        return f"Failed to favorite tweet: {e}"


@mcp.tool()
async def unfavorite_tweet(tweet_id: str) -> str:
    """Unfavorites a tweet."""
    try:
        client = await get_twitter_client()
        await client.unfavorite_tweet(tweet_id)
        return f"Successfully unfavorited tweet {tweet_id}"
    except Exception as e:
        logger.error(f"Failed to unfavorite tweet: {e}")
        return f"Failed to unfavorite tweet: {e}"


@mcp.tool()
async def retweet(tweet_id: str) -> str:
    """Retweets a tweet."""
    try:
        client = await get_twitter_client()
        await client.retweet(tweet_id)
        return f"Successfully retweeted tweet {tweet_id}"
    except Exception as e:
        logger.error(f"Failed to retweet: {e}")
        return f"Failed to retweet: {e}"


@mcp.tool()
async def delete_retweet(tweet_id: str) -> str:
    """Deletes the retweet."""
    try:
        client = await get_twitter_client()
        await client.delete_retweet(tweet_id)
        return f"Successfully deleted retweet of tweet {tweet_id}"
    except Exception as e:
        logger.error(f"Failed to delete retweet: {e}")
        return f"Failed to delete retweet: {e}"


@mcp.tool()
async def bookmark_tweet(
    tweet_id: str, folder_id: Optional[str] = None
) -> str:
    """Adds the tweet to bookmarks."""
    try:
        client = await get_twitter_client()
        await client.bookmark_tweet(tweet_id, folder_id)
        return f"Successfully bookmarked tweet {tweet_id}"
    except Exception as e:
        logger.error(f"Failed to bookmark tweet: {e}")
        return f"Failed to bookmark tweet: {e}"


@mcp.tool()
async def delete_bookmark(tweet_id: str) -> str:
    """Removes the tweet from bookmarks."""
    try:
        client = await get_twitter_client()
        await client.delete_bookmark(tweet_id)
        return f"Successfully deleted bookmark for tweet {tweet_id}"
    except Exception as e:
        logger.error(f"Failed to delete bookmark: {e}")
        return f"Failed to delete bookmark: {e}"


@mcp.tool()
async def get_bookmarks(
    count: int = 20,
    cursor: Optional[str] = None,
    folder_id: Optional[str] = None,
) -> str:
    """Retrieves bookmarks from the authenticated user’s Twitter account."""
    try:
        client = await get_twitter_client()
        bookmarks = await client.get_bookmarks(count, cursor, folder_id)
        return convert_tweets_to_markdown(bookmarks)
    except Exception as e:
        logger.error(f"Failed to get bookmarks: {e}")
        return f"Failed to get bookmarks: {e}"


@mcp.tool()
async def delete_all_bookmarks() -> str:
    """Deleted all bookmarks."""
    try:
        client = await get_twitter_client()
        await client.delete_all_bookmarks()
        return "Successfully deleted all bookmarks"
    except Exception as e:
        logger.error(f"Failed to delete all bookmarks: {e}")
        return f"Failed to delete all bookmarks: {e}"


@mcp.tool()
async def get_bookmark_folders(cursor: Optional[str] = None) -> str:
    """Retrieves bookmark folders."""
    try:
        client = await get_twitter_client()
        folders = await client.get_bookmark_folders(cursor)
        return str(folders)
    except Exception as e:
        logger.error(f"Failed to get bookmark folders: {e}")
        return f"Failed to get bookmark folders: {e}"


@mcp.tool()
async def edit_bookmark_folder(folder_id: str, name: str) -> str:
    """Edits a bookmark folder."""
    try:
        client = await get_twitter_client()
        folder = await client.edit_bookmark_folder(folder_id, name)
        return f"Successfully edited bookmark folder {folder.id}"
    except Exception as e:
        logger.error(f"Failed to edit bookmark folder: {e}")
        logger.error(f"Failed to delete bookmark folder: {e}")
        return f"Failed to delete bookmark folder: {e}"


@mcp.tool()
async def create_bookmark_folder(name: str) -> str:
    """Creates a bookmark folder."""
    try:
        client = await get_twitter_client()
        folder = await client.create_bookmark_folder(name)
        return f"Successfully created bookmark folder {folder.id}"
    except Exception as e:
        logger.error(f"Failed to create bookmark folder: {e}")
        return f"Failed to create bookmark folder: {e}"


@mcp.tool()
async def follow_user(user_id: str) -> str:
    """Follows a user."""
    try:
        client = await get_twitter_client()
        user = await client.follow_user(user_id)
        return f"Successfully followed user {user.id}"
    except Exception as e:
        logger.error(f"Failed to follow user: {e}")
        return f"Failed to follow user: {e}"


@mcp.tool()
async def unfollow_user(user_id: str) -> str:
    """Unfollows a user."""
    try:
        client = await get_twitter_client()
        user = await client.unfollow_user(user_id)
        return f"Successfully unfollowed user {user.id}"
    except Exception as e:
        logger.error(f"Failed to unfollow user: {e}")
        return f"Failed to unfollow user: {e}"


@mcp.tool()
async def block_user(user_id: str) -> str:
    """Blocks a user."""
    try:
        client = await get_twitter_client()
        user = await client.block_user(user_id)
        return f"Successfully blocked user {user.id}"
    except Exception as e:
        logger.error(f"Failed to block user: {e}")
        return f"Failed to block user: {e}"


@mcp.tool()
async def unblock_user(user_id: str) -> str:
    """Unblocks a user."""
    try:
        client = await get_twitter_client()
        user = await client.unblock_user(user_id)
        return f"Successfully unblocked user {user.id}"
    except Exception as e:
        logger.error(f"Failed to unblock user: {e}")
        return f"Failed to unblock user: {e}"


@mcp.tool()
async def mute_user(user_id: str) -> str:
    """Mutes a user."""
    try:
        client = await get_twitter_client()
        user = await client.mute_user(user_id)
        return f"Successfully muted user {user.id}"
    except Exception as e:
        logger.error(f"Failed to mute user: {e}")
        return f"Failed to mute user: {e}"


@mcp.tool(
    name="get_trends",
    description="Get trending topics on Twitter. Takes category (default: trending) and count (default: 20)"
)
async def get_trends(
    ctx: Context,
    category: str = "trending",
    count: int = 20,
    retry: bool = True,
    additional_request_params: Optional[dict] = None,
) -> str:
    """Get trending topics on Twitter."""
    try:
        client = await get_twitter_client()
        trends = await client.get_trends(
            category, count, retry, additional_request_params
        )
        return json.dumps([{
            "name": trend.name,
            "url": trend.url,
            "tweet_volume": trend.tweet_volume
        } for trend in trends], indent=2)
    except Exception as e:
        logger.error(f"Failed to get trends: {e}")
        return f"Failed to get trends: {e}"


@mcp.tool()
async def get_user_followers(
    user_id: str, count: int = 20, cursor: Optional[str] = None
) -> str:
    """Retrieves a list of followers for a given user."""
    try:
        client = await get_twitter_client()
        followers = await client.get_user_followers(user_id, count, cursor)
        return convert_tweets_to_markdown(followers)
    except Exception as e:
        logger.error(f"Failed to get user followers: {e}")
        return f"Failed to get user followers: {e}"


@mcp.tool()
async def get_latest_followers(
    user_id: Optional[str] = None,
    screen_name: Optional[str] = None,
    count: int = 200,
    cursor: Optional[str] = None,
) -> str:
    """Retrieves the latest followers."""
    try:
        client = await get_twitter_client()
        followers = await client.get_latest_followers(
            user_id, screen_name, count, cursor
        )
        return convert_tweets_to_markdown(followers)
    except Exception as e:
        logger.error(f"Failed to get latest followers: {e}")
        return f"Failed to get latest followers: {e}"


@mcp.tool()
async def get_latest_friends(
    user_id: Optional[str] = None,
    screen_name: Optional[str] = None,
    count: int = 200,
    cursor: Optional[str] = None,
) -> str:
    """Retrieves the latest friends (following users)."""
    try:
        client = await get_twitter_client()
        friends = await client.get_latest_friends(user_id, screen_name, count, cursor)
        return convert_tweets_to_markdown(friends)
    except Exception as e:
        logger.error(f"Failed to get latest friends: {e}")
        return f"Failed to get latest friends: {e}"


@mcp.tool()
async def get_user_verified_followers(
    user_id: str, count: int = 20, cursor: Optional[str] = None
) -> str:
    """Retrieves a list of verified followers for a given user."""
    try:
        client = await get_twitter_client()
        followers = await client.get_user_verified_followers(user_id, count, cursor)
        return convert_tweets_to_markdown(followers)
    except Exception as e:
        logger.error(f"Failed to get user verified followers: {e}")
        return f"Failed to get user verified followers: {e}"


@mcp.tool()
async def get_user_followers_you_know(
    user_id: str, count: int = 20, cursor: Optional[str] = None
) -> str:
    """Retrieves a list of common followers."""
    try:
        client = await get_twitter_client()
        followers = await client.get_user_followers_you_know(user_id, count, cursor)
        return convert_tweets_to_markdown(followers)
    except Exception as e:
        logger.error(f"Failed to get user followers you might know: {e}")
        return f"Failed to get user followers you might know: {e}"


@mcp.tool()
async def get_user_following(
    user_id: str, count: int = 20, cursor: Optional[str] = None
) -> str:
    """Retrieves a list of users whom the given user is following."""
    try:
        client = await get_twitter_client()
        following = await client.get_user_following(user_id, count, cursor)
        return convert_tweets_to_markdown(following)
    except Exception as e:
        logger.error(f"Failed to get user following: {e}")
        return f"Failed to get user following: {e}"


@mcp.tool()
async def get_user_subscriptions(
    user_id: str, count: int = 20, cursor: Optional[str] = None
) -> str:
    """Retrieves a list of users to which the specified user is subscribed."""
    try:
        client = await get_twitter_client()
        subscriptions = await client.get_user_subscriptions(user_id, count, cursor)
        return convert_tweets_to_markdown(subscriptions)
    except Exception as e:
        logger.error(f"Failed to get user subscriptions: {e}")
        return f"Failed to get user subscriptions: {e}"


@mcp.tool()
async def get_followers_ids(
    user_id: Optional[str] = None,
    screen_name: Optional[str] = None,
    count: int = 5000,
    cursor: Optional[str] = None,
) -> str:
    """Fetches the IDs of the followers of a specified user."""
    try:
        client = await get_twitter_client()
        ids = await client.get_followers_ids(user_id, screen_name, count, cursor)
        return str(ids)
    except Exception as e:
        logger.error(f"Failed to get followers ids: {e}")
        return f"Failed to get followers ids: {e}"


@mcp.tool()
async def get_friends_ids(
    user_id: Optional[str] = None,
    screen_name: Optional[str] = None,
    count: int = 5000,
    cursor: Optional[str] = None,
) -> str:
    """Fetches the IDs of the friends (following users) of a specified user."""
    try:
        client = await get_twitter_client()
        ids = await client.get_friends_ids(user_id, screen_name, count, cursor)
        return str(ids)
    except Exception as e:
        logger.error(f"Failed to get friends ids: {e}")
        return f"Failed to get friends ids: {e}"


@mcp.tool()
async def unmute_user(user_id: str) -> str:
    """Unmutes a user."""
    try:
        client = await get_twitter_client()
        user = await client.unmute_user(user_id)
        return f"Successfully unmuted user {user.id}"
    except Exception as e:
        logger.error(f"Failed to unmute user: {e}")
        return f"Failed to unmute user: {e}"


@mcp.tool()
async def get_highlights_tweets(
    user_id: str, count: int = 20, cursor: Optional[str] = None
) -> str:
    """Retrieves highlighted tweets from a user’s timeline."""
    try:
        client = await get_twitter_client()
        tweets = await client.get_user_highlights_tweets(user_id, count, cursor)
        return convert_tweets_to_markdown(tweets)
    except Exception as e:
        logger.error(f"Failed to get user highlights tweets: {e}")
        return f"Failed to get user highlights tweets: {e}"


@mcp.tool()
async def update_user() -> str:
    """Updates the user."""
    try:
        client = await get_twitter_client()
        user = await client.user()
        await user.update()
        return f"Successfully updated user {user.id}"
    except Exception as e:
        logger.error(f"Failed to update user: {e}")
        return f"Failed to update user: {e}"


@mcp.tool()
async def add_reaction_to_message(
    message_id: str, conversation_id: str, emoji: str
) -> str:
    """Adds a reaction emoji to a specific message in a conversation."""
    try:
        client = await get_twitter_client()
        await client.add_reaction_to_message(message_id, conversation_id, emoji)
        return f"Successfully added reaction to message {message_id}"
    except Exception as e:
        logger.error(f"Failed to add reaction to message: {e}")
        return f"Failed to add reaction to message: {e}"


@mcp.tool()
async def remove_reaction_from_message(
    message_id: str, conversation_id: str, emoji: str
) -> str:
    """Remove a reaction from a message."""
    try:
        client = await get_twitter_client()
        await client.remove_reaction_from_message(message_id, conversation_id, emoji)
        return f"Successfully removed reaction from message {message_id}"
    except Exception as e:
        logger.error(f"Failed to remove reaction from message: {e}")
        return f"Failed to remove reaction from message: {e}"


@mcp.tool()
async def get_dm_history(
    user_id: str, max_id: Optional[str] = None
) -> str:
    """Retrieves the DM conversation history with a specific user."""
    try:
        client = await get_twitter_client()
        messages = await client.get_dm_history(user_id, max_id)
        return str(messages)
    except Exception as e:
        logger.error(f"Failed to get DM history: {e}")
        return f"Failed to get DM history: {e}"


@mcp.tool()
async def send_dm_to_group(
    group_id: str,
    text: str,
    media_id: Optional[str] = None,
    reply_to: Optional[str] = None,
) -> str:
    """Sends a message to a group."""
    try:
        client = await get_twitter_client()
        message = await client.send_dm_to_group(group_id, text, media_id, reply_to)
        return f"Successfully sent DM to group {group_id}: {message.id}"
    except Exception as e:
        logger.error(f"Failed to send DM to group: {e}")
        return f"Failed to send DM to group: {e}"


@mcp.tool()
async def get_group_dm_history(
    group_id: str, max_id: Optional[str] = None
) -> str:
    """Retrieves the DM conversation history in a group."""
    try:
        client = await get_twitter_client()
        messages = await client.get_group_dm_history(group_id, max_id)
        return str(messages)
    except Exception as e:
        logger.error(f"Failed to get group DM history: {e}")
        return f"Failed to get group DM history: {e}"


@mcp.tool()
async def get_group(group_id: str) -> str:
    """Fetches a group by ID."""
    try:
        client = await get_twitter_client()
        group = await client.get_group(group_id)
        return str(group)
    except Exception as e:
        logger.error(f"Failed to get group: {e}")
        return f"Failed to get group: {e}"


@mcp.tool()
async def add_members_to_group(
    group_id: str, user_ids: List[str]
) -> str:
    """Adds members to a group."""
    try:
        client = await get_twitter_client()
        await client.add_members_to_group(group_id, user_ids)
        return f"Successfully added members to group {group_id}"
    except Exception as e:
        logger.error(f"Failed to add members to group: {e}")
        return f"Failed to add members to group: {e}"


@mcp.tool()
async def change_group_name(group_id: str, name: str) -> str:
    """Changes group name."""
    try:
        client = await get_twitter_client()
        await client.change_group_name(group_id, name)
        return f"Successfully changed group name for group {group_id}"
    except Exception as e:
        logger.error(f"Failed to change group name: {e}")
        return f"Failed to change group name: {e}"


@mcp.tool(
    name="get_user_profile",
    description="Get detailed profile information for a user"
)
async def get_user_profile(ctx: Context, user_id: str) -> Dict[str, Any]:
    """Get detailed profile information for a user."""
    try:
        client = await get_twitter_client()
        user = await client.get_user_by_id(user_id)
        
        return {
            "id": user.id,
            "name": user.name,
            "screen_name": user.screen_name,
            "description": user.description,
            "followers_count": user.followers_count,
            "friends_count": user.friends_count,
            "statuses_count": user.statuses_count,
            "created_at": str(user.created_at),
            "verified": user.verified,
            "protected": user.protected,
            "location": user.location,
            "url": user.url,
            "profile_image_url": user.profile_image_url,
        }
    except Exception as e:
        logger.error(f"Failed to get user profile: {e}")
        return {"error": str(e)}


@mcp.tool()
async def get_tweet_details(tweet_id: str) -> Dict[str, Any]:
    """Get detailed information about a specific tweet."""
    try:
        client = await get_twitter_client()
        tweet = await client.get_tweet_by_id(tweet_id)
        
        return {
            "success": True,
            "data": {
                "id": tweet.id,
                "text": tweet.text,
                "created_at": str(tweet.created_at),
                "author_id": tweet.author_id,
                "retweet_count": tweet.retweet_count,
                "favorite_count": tweet.favorite_count,
                "reply_count": tweet.reply_count,
                "quote_count": tweet.quote_count,
                "lang": tweet.lang
            }
        }
    except Exception as e:
        logger.error(f"Failed to get tweet details: {e}")
        return {
            "success": False,
            "error": str(e),
            "error_type": "TwitterAPIError"
        }


@mcp.tool()
async def vote_on_poll(tweet_id: str, choice: str) -> str:
    """Vote on a poll."""
    try:
        client = await get_twitter_client()
        tweet = await client.get_tweet_by_id(tweet_id)
        if not hasattr(tweet, "card"):
            return "This tweet does not contain a poll"

        await client.vote(
            selected_choice=choice,
            card_uri=tweet.card.url,
            tweet_id=tweet_id,
            card_name=tweet.card.name,
        )
        return f"Successfully voted for '{choice}' on tweet {tweet_id}"
    except Exception as e:
        logger.error(f"Failed to vote on poll: {e}")
        return f"Failed to vote on poll: {e}"


@mcp.tool()
async def get_user_mentions(
    user_id: str, count: int = 20, cursor: Optional[str] = None
) -> str:
    """Get tweets mentioning a specific user."""
    try:
        client = await get_twitter_client()
        query = f"@{user_id}"
        tweets = await client.search_tweet(
            query, product="Latest", count=count, cursor=cursor
        )
        return convert_tweets_to_markdown(tweets)
    except Exception as e:
        logger.error(f"Failed to get user mentions: {e}")
        return f"Failed to get user mentions: {e}"


@mcp.tool()
async def get_conversation_thread(tweet_id: str) -> str:
    """Get the full conversation thread for a tweet."""
    try:
        client = await get_twitter_client()
        tweet = await client.get_tweet_by_id(tweet_id)
        conversation = []

        # Get parent tweets if this is a reply
        current_tweet = tweet
        while hasattr(current_tweet, "in_reply_to_status_id"):
            parent_id = current_tweet.in_reply_to_status_id
            if parent_id:
                current_tweet = await client.get_tweet_by_id(parent_id)
                conversation.insert(0, current_tweet)
            else:
                break

        # Add the main tweet
        conversation.append(tweet)

        return convert_tweets_to_markdown(conversation)
    except Exception as e:
        logger.error(f"Failed to get conversation thread: {e}")
        return f"Failed to get conversation thread: {e}"
