- [Home](index.html)
- twikit package
- [View page source](_sources/twikit.rst.txt)

---

# twikit package [](#module-twikit "Link to this heading")

## Twikit Twitter API Wrapper [](#twikit-twitter-api-wrapper "Link to this heading")

[https://github.com/d60/twikit](https://github.com/d60/twikit)
A Python library for interacting with the Twitter API.

## Client [](#client "Link to this heading")

_class_ twikit.client.client.Client( _language:str\|None=None_, _proxy:str\|None=None_, _captcha_solver:[Capsolver](#twikit._captcha.capsolver.Capsolver "twikit._captcha.capsolver.Capsolver") \|None=None_, _user_agent:str\|None=None_, _\*\*kwargs_) [\[source\]](_modules/twikit/client/client.html#Client) [](#twikit.client.client.Client "Link to this definition")

A client for interacting with the Twitter API.
Since this class is for asynchronous use,
methods must be executed using await.

Parameters:

- **language** ( `str` \| None, default=None) – The language code to use in API requests.

- **proxy** ( `str` \| None, default=None) – The proxy server URL to use for request
  (e.g., ‘ [http://0.0.0.0:0000](http://0.0.0.0:0000)’).

- **captcha_solver** ( [`Capsolver`](#twikit._captcha.capsolver.Capsolver "twikit._captcha.capsolver.Capsolver") \| None, default=None) – See [`Capsolver`](#twikit._captcha.capsolver.Capsolver "twikit._captcha.capsolver.Capsolver").

Examples

```
>>> client = Client(language='en-US')

```

```
>>> await client.login(
...     auth_info_1='example_user',
...     auth_info_2='email@example.com',
...     password='00000000'
... )

```

_async_ login( _\*_, _auth_info_1:str_, _auth_info_2:str\|None=None_, _password:str_, _totp_secret:str\|None=None_)→dict [\[source\]](_modules/twikit/client/client.html#Client.login) [](#twikit.client.client.Client.login "Link to this definition")

Logs into the account using the specified login information.
auth_info_1 and password are required parameters.
auth_info_2 is optional and can be omitted, but it is
recommended to provide if available.
The order in which you specify authentication information
(auth_info_1 and auth_info_2) is flexible.

Parameters:

- **auth_info_1** ( `str`) – The first piece of authentication information,
  which can be a username, email address, or phone number.

- **auth_info_2** ( `str`, default=None) – The second piece of authentication information,
  which is optional but recommended to provide.
  It can be a username, email address, or phone number.

- **password** ( `str`) – The password associated with the account.

- **totp_secret** ( `str`) – The TOTP (Time-Based One-Time Password) secret key used for
  two-factor authentication (2FA).

Examples

```
>>> await client.login(
...     auth_info_1='example_user',
...     auth_info_2='email@example.com',
...     password='00000000'
... )

```

_async_ logout()→Response [\[source\]](_modules/twikit/client/client.html#Client.logout) [](#twikit.client.client.Client.logout "Link to this definition")

Logs out of the currently logged-in account.

_async_ unlock()→None [\[source\]](_modules/twikit/client/client.html#Client.unlock) [](#twikit.client.client.Client.unlock "Link to this definition")

Unlocks the account using the provided CAPTCHA solver.

See also

`capsolver`

get_cookies()→dict [\[source\]](_modules/twikit/client/client.html#Client.get_cookies) [](#twikit.client.client.Client.get_cookies "Link to this definition")

Get the cookies.
You can skip the login procedure by loading the saved cookies
using the [`set_cookies()`](#twikit.client.client.Client.set_cookies "twikit.client.client.Client.set_cookies") method.

Examples

```
>>> client.get_cookies()

```

See also

[`set_cookies`](#twikit.client.client.Client.set_cookies "twikit.client.client.Client.set_cookies"), [`load_cookies`](#twikit.client.client.Client.load_cookies "twikit.client.client.Client.load_cookies"), [`save_cookies`](#twikit.client.client.Client.save_cookies "twikit.client.client.Client.save_cookies")

save_cookies( _path:str_)→None [\[source\]](_modules/twikit/client/client.html#Client.save_cookies) [](#twikit.client.client.Client.save_cookies "Link to this definition")

Save cookies to file in json format.
You can skip the login procedure by loading the saved cookies
using the [`load_cookies()`](#twikit.client.client.Client.load_cookies "twikit.client.client.Client.load_cookies") method.

Parameters:

**path** ( `str`) – The path to the file where the cookie will be stored.

Examples

```
>>> client.save_cookies('cookies.json')

```

See also

[`load_cookies`](#twikit.client.client.Client.load_cookies "twikit.client.client.Client.load_cookies"), [`get_cookies`](#twikit.client.client.Client.get_cookies "twikit.client.client.Client.get_cookies"), [`set_cookies`](#twikit.client.client.Client.set_cookies "twikit.client.client.Client.set_cookies")

set_cookies( _cookies:dict_, _clear_cookies:bool=False_)→None [\[source\]](_modules/twikit/client/client.html#Client.set_cookies) [](#twikit.client.client.Client.set_cookies "Link to this definition")

Sets cookies.
You can skip the login procedure by loading a saved cookies.

Parameters:

**cookies** ( `dict`) – The cookies to be set as key value pair.

Examples

```
>>> with open('cookies.json', 'r', encoding='utf-8') as f:
...     client.set_cookies(json.load(f))

```

See also

[`get_cookies`](#twikit.client.client.Client.get_cookies "twikit.client.client.Client.get_cookies"), [`load_cookies`](#twikit.client.client.Client.load_cookies "twikit.client.client.Client.load_cookies"), [`save_cookies`](#twikit.client.client.Client.save_cookies "twikit.client.client.Client.save_cookies")

load_cookies( _path:str_)→None [\[source\]](_modules/twikit/client/client.html#Client.load_cookies) [](#twikit.client.client.Client.load_cookies "Link to this definition")

Loads cookies from a file.
You can skip the login procedure by loading a saved cookies.

Parameters:

**path** ( `str`) – Path to the file where the cookie is stored.

Examples

```
>>> client.load_cookies('cookies.json')

```

See also

[`get_cookies`](#twikit.client.client.Client.get_cookies "twikit.client.client.Client.get_cookies"), [`save_cookies`](#twikit.client.client.Client.save_cookies "twikit.client.client.Client.save_cookies"), [`set_cookies`](#twikit.client.client.Client.set_cookies "twikit.client.client.Client.set_cookies")

set_delegate_account( _user_id:str\|None_)→None [\[source\]](_modules/twikit/client/client.html#Client.set_delegate_account) [](#twikit.client.client.Client.set_delegate_account "Link to this definition")

Sets the account to act as.

Parameters:

**user_id** ( `str` \| None) – The user ID of the account to act as.
Set to None to clear the delegated account.

_async_ user_id()→str [\[source\]](_modules/twikit/client/client.html#Client.user_id) [](#twikit.client.client.Client.user_id "Link to this definition")

Retrieves the user ID associated with the authenticated account.

_async_ user()→[User](#twikit.user.User "twikit.user.User") [\[source\]](_modules/twikit/client/client.html#Client.user) [](#twikit.client.client.Client.user "Link to this definition")

Retrieve detailed information about the authenticated user.

_async_ search_tweet( _query:str_, _product:Literal\['Top','Latest','Media'\]_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/client/client.html#Client.search_tweet) [](#twikit.client.client.Client.search_tweet "Link to this definition")

Searches for tweets based on the specified query and
product type.

Parameters:

- **query** ( `str`) – The search query.

- **product** ( _{'Top'_ _,_ _'Latest'_ _,_ _'Media'}_) – The type of tweets to retrieve.

- **count** ( `int`, default=20) – The number of tweets to retrieve, between 1 and 20.

- **cursor** ( `str`, default=20) – Token to retrieve more tweets.

Returns:

An instance of the Result class containing the
search results.

Return type:

Result\[ `Tweet`\]

Examples

```
>>> tweets = await client.search_tweet('query', 'Top')
>>> for tweet in tweets:
...    print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

```
>>> more_tweets = await tweets.next()  # Retrieve more tweets
>>> for tweet in more_tweets:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

```
>>> # Retrieve previous tweets
>>> previous_tweets = await tweets.previous()

```

_async_ search_user( _query:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/client/client.html#Client.search_user) [](#twikit.client.client.Client.search_user "Link to this definition")

Searches for users based on the provided query.

Parameters:

- **query** ( `str`) – The search query for finding users.

- **count** ( `int`, default=20) – The number of users to retrieve in each request.

- **cursor** ( `str`, default=None) – Token to retrieve more users.

Returns:

An instance of the Result class containing the
search results.

Return type:

Result\[ `User`\]

Examples

```
>>> result = await client.search_user('query')
>>> for user in result:
...     print(user)
<User id="...">
<User id="...">
...
...

```

```
>>> more_results = await result.next()  # Retrieve more search results
>>> for user in more_results:
...     print(user)
<User id="...">
<User id="...">
...
...

```

_async_ get_similar_tweets( _tweet_id:str_)→list\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/client/client.html#Client.get_similar_tweets) [](#twikit.client.client.Client.get_similar_tweets "Link to this definition")

Retrieves tweets similar to the specified tweet (Twitter premium only).

Parameters:

**tweet_id** ( `str`) – The ID of the tweet for which similar tweets are to be retrieved.

Returns:

A list of Tweet objects representing tweets
similar to the specified tweet.

Return type:

list\[ `Tweet`\]

_async_ get_user_highlights_tweets( _user_id:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/client/client.html#Client.get_user_highlights_tweets) [](#twikit.client.client.Client.get_user_highlights_tweets "Link to this definition")

Retrieves highlighted tweets from a user’s timeline.

Parameters:

- **user_id** ( `str`) – The user ID

- **count** ( `int`, default=20) – The number of tweets to retrieve.

Returns:

An instance of the Result class containing the highlighted tweets.

Return type:

Result\[ `Tweet`\]

Examples

```
>>> result = await client.get_user_highlights_tweets('123456789')
>>> for tweet in result:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

```
>>> more_results = await result.next()  # Retrieve more highlighted tweets
>>> for tweet in more_results:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

_async_ upload_media( _source:str\|bytes_, _wait_for_completion:bool=False_, _status_check_interval:float\|None=None_, _media_type:str\|None=None_, _media_category:str\|None=None_, _is_long_video:bool=False_)→str [\[source\]](_modules/twikit/client/client.html#Client.upload_media) [](#twikit.client.client.Client.upload_media "Link to this definition")

Uploads media to twitter.

Parameters:

- **source** ( `str` \| `bytes`) – The source of the media to be uploaded.
  It can be either a file path or bytes of the media content.

- **wait_for_completion** ( `bool`, default=False) – Whether to wait for the completion of the media upload process.

- **status_check_interval** ( `float`, default=1.0) – The interval (in seconds) to check the status of the
  media upload process.

- **media_type** ( `str`, default=None) – The MIME type of the media.
  If not specified, it will be guessed from the source.

- **media_category** ( `str`, default=None) – The media category.

- **is_long_video** ( `bool`, default=False) – If this is True, videos longer than 2:20 can be uploaded.
  (Twitter Premium only)

Returns:

The media ID of the uploaded media.

Return type:

`str`

Examples

Videos, images and gifs can be uploaded.

```
>>> media_id_1 = await client.upload_media(
...     'media1.jpg',
... )

```

```
>>> media_id_2 = await client.upload_media(
...     'media2.mp4',
...     wait_for_completion=True
... )

```

```
>>> media_id_3 = await client.upload_media(
...     'media3.gif',
...     wait_for_completion=True,
...     media_category='tweet_gif'  # media_category must be specified
... )

```

_async_ check_media_status( _media_id:str_, _is_long_video:bool=False_)→dict [\[source\]](_modules/twikit/client/client.html#Client.check_media_status) [](#twikit.client.client.Client.check_media_status "Link to this definition")

Check the status of uploaded media.

Parameters:

**media_id** ( `str`) – The media ID of the uploaded media.

Returns:

A dictionary containing information about the status of
the uploaded media.

Return type:

dict

_async_ create_media_metadata( _media_id:str_, _alt_text:str\|None=None_, _sensitive_warning:list\[Literal\['adult_content','graphic_violence','other'\]\]=None_)→Response [\[source\]](_modules/twikit/client/client.html#Client.create_media_metadata) [](#twikit.client.client.Client.create_media_metadata "Link to this definition")

Adds metadata to uploaded media.

Parameters:

- **media_id** ( `str`) – The media id for which to create metadata.

- **alt_text** ( `str` \| None, default=None) – Alternative text for the media.

- **sensitive_warning** ( _list{'adult_content'_ _,_ _'graphic_violence'_ _,_ _'other'}_) – A list of sensitive content warnings for the media.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> media_id = await client.upload_media('media.jpg')
>>> await client.create_media_metadata(
...     media_id,
...     alt_text='This is a sample media',
...     sensitive_warning=['other']
... )
>>> await client.create_tweet(media_ids=[media_id])

```

_async_ create_poll( _choices:list\[str\]_, _duration_minutes:int_)→str [\[source\]](_modules/twikit/client/client.html#Client.create_poll) [](#twikit.client.client.Client.create_poll "Link to this definition")

Creates a poll and returns card-uri.

Parameters:

- **choices** (list\[ `str`\]) – A list of choices for the poll. Maximum of 4 choices.

- **duration_minutes** ( `int`) – The duration of the poll in minutes.

Returns:

The URI of the created poll card.

Return type:

`str`

Examples

Create a poll with three choices lasting for 60 minutes:

```
>>> choices = ['Option A', 'Option B', 'Option C']
>>> duration_minutes = 60
>>> card_uri = await client.create_poll(choices, duration_minutes)
>>> print(card_uri)
'card://0000000000000000000'

```

_async_ vote( _selected_choice:str_, _card_uri:str_, _tweet_id:str_, _card_name:str_)→[Poll](#twikit.tweet.Poll "twikit.tweet.Poll") [\[source\]](_modules/twikit/client/client.html#Client.vote) [](#twikit.client.client.Client.vote "Link to this definition")

Vote on a poll with the selected choice.
:param selected_choice: The label of the selected choice for the vote.
:type selected_choice: `str`
:param card_uri: The URI of the poll card.
:type card_uri: `str`
:param tweet_id: The ID of the original tweet containing the poll.
:type tweet_id: `str`
:param card_name: The name of the poll card.
:type card_name: `str`

Returns:

The Poll object representing the updated poll after voting.

Return type:

`Poll`

_async_ create_tweet( _text:str=''_, _media_ids:list\[str\]\|None=None_, _poll_uri:str\|None=None_, _reply_to:str\|None=None_, _conversation_control:Literal\['followers','verified','mentioned'\]\|None=None_, _attachment_url:str\|None=None_, _community_id:str\|None=None_, _share_with_followers:bool=False_, _is_note_tweet:bool=False_, _richtext_options:list\[dict\]=None_, _edit_tweet_id:str\|None=None_)→[Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet") [\[source\]](_modules/twikit/client/client.html#Client.create_tweet) [](#twikit.client.client.Client.create_tweet "Link to this definition")

Creates a new tweet on Twitter with the specified
text, media, and poll.

Parameters:

- **text** ( `str`, default=’’) – The text content of the tweet.

- **media_ids** (list\[ `str`\], default=None) – A list of media IDs or URIs to attach to the tweet.
  media IDs can be obtained by using the upload_media method.

- **poll_uri** ( `str`, default=None) – The URI of a Twitter poll card to attach to the tweet.
  Poll URIs can be obtained by using the create_poll method.

- **reply_to** ( `str`, default=None) – The ID of the tweet to which this tweet is a reply.

- **conversation_control** ( _{'followers'_ _,_ _'verified'_ _,_ _'mentioned'}_) – The type of conversation control for the tweet:
  \- ‘followers’: Limits replies to followers only.
  \- ‘verified’: Limits replies to verified accounts only.
  \- ‘mentioned’: Limits replies to mentioned accounts only.

- **attachment_url** ( `str`) – URL of the tweet to be quoted.

- **is_note_tweet** ( `bool`, default=False) – If this option is set to True, tweets longer than 280 characters
  can be posted (Twitter Premium only).

- **richtext_options** (list\[ `dict`\], default=None) – Options for decorating text (Twitter Premium only).

- **edit_tweet_id** ( `str` \| None, default=None) – ID of the tweet to edit (Twitter Premium only).

Raises:

[**DuplicateTweet**](#twikit.errors.DuplicateTweet "twikit.errors.DuplicateTweet") –

Returns:

The Created Tweet.

Return type:

`Tweet`

Examples

Create a tweet with media:

```
>>> tweet_text = 'Example text'
>>> media_ids = [\
...     await client.upload_media('image1.png'),\
...     await client.upload_media('image2.png')\
... ]
>>> await client.create_tweet(
...     tweet_text,
...     media_ids=media_ids
... )

```

Create a tweet with a poll:

```
>>> tweet_text = 'Example text'
>>> poll_choices = ['Option A', 'Option B', 'Option C']
>>> duration_minutes = 60
>>> poll_uri = await client.create_poll(poll_choices, duration_minutes)
>>> await client.create_tweet(
...     tweet_text,
...     poll_uri=poll_uri
... )

```

See also

[`upload_media`](#twikit.client.client.Client.upload_media "twikit.client.client.Client.upload_media"), [`create_poll`](#twikit.client.client.Client.create_poll "twikit.client.client.Client.create_poll")

_async_ create_scheduled_tweet( _scheduled_at:int_, _text:str=''_, _media_ids:list\[str\]\|None=None_)→str [\[source\]](_modules/twikit/client/client.html#Client.create_scheduled_tweet) [](#twikit.client.client.Client.create_scheduled_tweet "Link to this definition")

Schedules a tweet to be posted at a specified timestamp.

Parameters:

- **scheduled_at** ( `int`) – The timestamp when the tweet should be scheduled for posting.

- **text** ( `str`, default=’’) – The text content of the tweet, by default an empty string.

- **media_ids** (list\[ `str`\], default=None) – A list of media IDs to be attached to the tweet, by default None.

Returns:

The ID of the scheduled tweet.

Return type:

`str`

Examples

Create a tweet with media:

```
>>> scheduled_time = int(time.time()) + 3600  # One hour from now
>>> tweet_text = 'Example text'
>>> media_ids = [\
...     await client.upload_media('image1.png'),\
...     await client.upload_media('image2.png')\
... ]
>>> await client.create_scheduled_tweet(
...     scheduled_time
...     tweet_text,
...     media_ids=media_ids
... )

```

_async_ delete_tweet( _tweet_id:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.delete_tweet) [](#twikit.client.client.Client.delete_tweet "Link to this definition")

Deletes a tweet.

Parameters:

**tweet_id** ( `str`) – ID of the tweet to be deleted.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> tweet_id = '0000000000'
>>> await delete_tweet(tweet_id)

```

_async_ get_user_by_screen_name( _screen_name:str_)→[User](#twikit.user.User "twikit.user.User") [\[source\]](_modules/twikit/client/client.html#Client.get_user_by_screen_name) [](#twikit.client.client.Client.get_user_by_screen_name "Link to this definition")

Fetches a user by screen name.

### Parameter [](#parameter "Link to this heading")

screen_name`str`

The screen name of the Twitter user.

returns:

An instance of the User class representing the
Twitter user.

rtype:

`User`

Examples

```
>>> target_screen_name = 'example_user'
>>> user = await client.get_user_by_name(target_screen_name)
>>> print(user)
<User id="...">

```

_async_ get_user_by_id( _user_id:str_)→[User](#twikit.user.User "twikit.user.User") [\[source\]](_modules/twikit/client/client.html#Client.get_user_by_id) [](#twikit.client.client.Client.get_user_by_id "Link to this definition")

Fetches a user by ID

### Parameter [](#id1 "Link to this heading")

user_id`str`

The ID of the Twitter user.

returns:

An instance of the User class representing the
Twitter user.

rtype:

`User`

Examples

```
>>> target_screen_name = '000000000'
>>> user = await client.get_user_by_id(target_screen_name)
>>> print(user)
<User id="000000000">

```

_async_ reverse_geocode( _lat:float_, _long:float_, _accuracy:str\|float\|None=None_, _granularity:str\|None=None_, _max_results:int\|None=None_)→list\[ [Place](#twikit.geo.Place "twikit.geo.Place")\] [\[source\]](_modules/twikit/client/client.html#Client.reverse_geocode) [](#twikit.client.client.Client.reverse_geocode "Link to this definition")

Given a latitude and a longitude, searches for up to 20 places that

Parameters:

- **lat** ( `float`) – The latitude to search around.

- **long** ( `float`) – The longitude to search around.

- **accuracy** ( `str` \| `float` None, default=None) – A hint on the “region” in which to search.

- **granularity** ( `str` \| None, default=None) – This is the minimal granularity of place types to return and must
  be one of: neighborhood, city, admin or country.

- **max_results** ( `int` \| None, default=None) – A hint as to the number of results to return.

Return type:

list\[ [`Place`](#twikit.geo.Place "twikit.geo.Place")\]

_async_ search_geo( _lat:float\|None=None_, _long:float\|None=None_, _query:str\|None=None_, _ip:str\|None=None_, _granularity:str\|None=None_, _max_results:int\|None=None_)→list\[ [Place](#twikit.geo.Place "twikit.geo.Place")\] [\[source\]](_modules/twikit/client/client.html#Client.search_geo) [](#twikit.client.client.Client.search_geo "Link to this definition")

Search for places that can be attached to a Tweet via POST
statuses/update.

Parameters:

- **lat** ( `float` \| None) – The latitude to search around.

- **long** ( `float` \| None) – The longitude to search around.

- **query** ( `str` \| None) – Free-form text to match against while executing a geo-based query,
  best suited for finding nearby locations by name.
  Remember to URL encode the query.

- **ip** ( `str` \| None) – An IP address. Used when attempting to
  fix geolocation based off of the user’s IP address.

- **granularity** ( `str` \| None) – This is the minimal granularity of place types to return and must
  be one of: neighborhood, city, admin or country.

- **max_results** ( `int` \| None) – A hint as to the number of results to return.

Return type:

list\[ [`Place`](#twikit.geo.Place "twikit.geo.Place")\]

_async_ get_place( _id:str_)→[Place](#twikit.geo.Place "twikit.geo.Place") [\[source\]](_modules/twikit/client/client.html#Client.get_place) [](#twikit.client.client.Client.get_place "Link to this definition")Parameters:

**id** ( `str`) – The ID of the place.

Return type:

[`Place`](#twikit.geo.Place "twikit.geo.Place")

_async_ get_tweet_by_id( _tweet_id:str_, _cursor:str\|None=None_)→[Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet") [\[source\]](_modules/twikit/client/client.html#Client.get_tweet_by_id) [](#twikit.client.client.Client.get_tweet_by_id "Link to this definition")

Fetches a tweet by tweet ID.

Parameters:

**tweet_id** ( `str`) – The ID of the tweet.

Returns:

A Tweet object representing the fetched tweet.

Return type:

`Tweet`

Examples

```
>>> target_tweet_id = '...'
>>> tweet = client.get_tweet_by_id(target_tweet_id)
>>> print(tweet)
<Tweet id="...">

```

_async_ get_scheduled_tweets()→list\[ScheduledTweet\] [\[source\]](_modules/twikit/client/client.html#Client.get_scheduled_tweets) [](#twikit.client.client.Client.get_scheduled_tweets "Link to this definition")

Retrieves scheduled tweets.

Returns:

List of ScheduledTweet objects representing the scheduled tweets.

Return type:

list\[ `ScheduledTweet`\]

_async_ delete_scheduled_tweet( _tweet_id:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.delete_scheduled_tweet) [](#twikit.client.client.Client.delete_scheduled_tweet "Link to this definition")

Delete a scheduled tweet.

Parameters:

**tweet_id** ( `str`) – The ID of the scheduled tweet to delete.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

_async_ get_retweeters( _tweet_id:str_, _count:int=40_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/client/client.html#Client.get_retweeters) [](#twikit.client.client.Client.get_retweeters "Link to this definition")

Retrieve users who retweeted a specific tweet.

Parameters:

- **tweet_id** ( `str`) – The ID of the tweet.

- **count** ( `int`, default=40) – The maximum number of users to retrieve.

- **cursor** ( `str`, default=None) – A string indicating the position of the cursor for pagination.

Returns:

A list of users who retweeted the tweet.

Return type:

Result\[ `User`\]

Examples

```
>>> tweet_id = '...'
>>> retweeters = client.get_retweeters(tweet_id)
>>> print(retweeters)
[<User id="...">, <User id="...">, ..., <User id="...">]

```

```
>>> more_retweeters = retweeters.next()  # Retrieve more retweeters.
>>> print(more_retweeters)
[<User id="...">, <User id="...">, ..., <User id="...">]

```

_async_ get_favoriters( _tweet_id:str_, _count:int=40_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/client/client.html#Client.get_favoriters) [](#twikit.client.client.Client.get_favoriters "Link to this definition")

Retrieve users who favorited a specific tweet.

Parameters:

- **tweet_id** ( `str`) – The ID of the tweet.

- **count** ( _int_ _,_ _default=40_) – The maximum number of users to retrieve.

- **cursor** ( `str`, default=None) – A string indicating the position of the cursor for pagination.

Returns:

A list of users who favorited the tweet.

Return type:

Result\[ `User`\]

Examples

```
>>> tweet_id = '...'
>>> favoriters = await client.get_favoriters(tweet_id)
>>> print(favoriters)
[<User id="...">, <User id="...">, ..., <User id="...">]

```

```
>>> # Retrieve more favoriters.
>>> more_favoriters = await favoriters.next()
>>> print(more_favoriters)
[<User id="...">, <User id="...">, ..., <User id="...">]

```

_async_ get_community_note( _note_id:str_)→[CommunityNote](#twikit.tweet.CommunityNote "twikit.tweet.CommunityNote") [\[source\]](_modules/twikit/client/client.html#Client.get_community_note) [](#twikit.client.client.Client.get_community_note "Link to this definition")

Fetches a community note by ID.

Parameters:

**note_id** ( `str`) – The ID of the community note.

Returns:

A CommunityNote object representing the fetched community note.

Return type:

`CommunityNote`

Raises:

[**TwitterException**](#twikit.errors.TwitterException "twikit.errors.TwitterException") – Invalid note ID.

Examples

```
>>> note_id = '...'
>>> note = client.get_community_note(note_id)
>>> print(note)
<CommunityNote id="...">

```

_async_ get_user_tweets( _user_id:str_, _tweet_type:Literal\['Tweets','Replies','Media','Likes'\]_, _count:int=40_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/client/client.html#Client.get_user_tweets) [](#twikit.client.client.Client.get_user_tweets "Link to this definition")

Fetches tweets from a specific user’s timeline.

Parameters:

- **user_id** ( `str`) – The ID of the Twitter user whose tweets to retrieve.
  To get the user id from the screen name, you can use
  get_user_by_screen_name method.

- **tweet_type** ( _{'Tweets'_ _,_ _'Replies'_ _,_ _'Media'_ _,_ _'Likes'}_) – The type of tweets to retrieve.

- **count** ( `int`, default=40) – The number of tweets to retrieve.

- **cursor** ( `str`, default=None) – The cursor for fetching the next set of results.

Returns:

A Result object containing a list of Tweet objects.

Return type:

Result\[ `Tweet`\]

Examples

```
>>> user_id = '...'

```

If you only have the screen name, you can get the user id as follows:

```
>>> screen_name = 'example_user'
>>> user = client.get_user_by_screen_name(screen_name)
>>> user_id = user.id

```

```
>>> tweets = await client.get_user_tweets(user_id, 'Tweets', count=20)
>>> for tweet in tweets:
...    print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

```
>>> more_tweets = await tweets.next()  # Retrieve more tweets
>>> for tweet in more_tweets:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

```
>>> # Retrieve previous tweets
>>> previous_tweets = await tweets.previous()

```

See also

[`get_user_by_screen_name`](#twikit.client.client.Client.get_user_by_screen_name "twikit.client.client.Client.get_user_by_screen_name")

_async_ get_timeline( _count:int=20_, _seen_tweet_ids:list\[str\]\|None=None_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/client/client.html#Client.get_timeline) [](#twikit.client.client.Client.get_timeline "Link to this definition")

Retrieves the timeline.
Retrieves tweets from Home -> For You.

Parameters:

- **count** ( `int`, default=20) – The number of tweets to retrieve.

- **seen_tweet_ids** (list\[ `str`\], default=None) – A list of tweet IDs that have been seen.

- **cursor** ( `str`, default=None) – A cursor for pagination.

Returns:

A Result object containing a list of Tweet objects.

Return type:

Result\[ `Tweet`\]

Example

```
>>> tweets = await client.get_timeline()
>>> for tweet in tweets:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...
>>> more_tweets = await tweets.next() # Retrieve more tweets
>>> for tweet in more_tweets:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

_async_ get_latest_timeline( _count:int=20_, _seen_tweet_ids:list\[str\]\|None=None_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/client/client.html#Client.get_latest_timeline) [](#twikit.client.client.Client.get_latest_timeline "Link to this definition")

Retrieves the timeline.
Retrieves tweets from Home -> Following.

Parameters:

- **count** ( `int`, default=20) – The number of tweets to retrieve.

- **seen_tweet_ids** (list\[ `str`\], default=None) – A list of tweet IDs that have been seen.

- **cursor** ( `str`, default=None) – A cursor for pagination.

Returns:

A Result object containing a list of Tweet objects.

Return type:

Result\[ `Tweet`\]

Example

```
>>> tweets = await client.get_latest_timeline()
>>> for tweet in tweets:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...
>>> more_tweets = await tweets.next() # Retrieve more tweets
>>> for tweet in more_tweets:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

_async_ favorite_tweet( _tweet_id:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.favorite_tweet) [](#twikit.client.client.Client.favorite_tweet "Link to this definition")

Favorites a tweet.

Parameters:

**tweet_id** ( `str`) – The ID of the tweet to be liked.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> tweet_id = '...'
>>> await client.favorite_tweet(tweet_id)

```

See also

[`unfavorite_tweet`](#twikit.client.client.Client.unfavorite_tweet "twikit.client.client.Client.unfavorite_tweet")

_async_ unfavorite_tweet( _tweet_id:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.unfavorite_tweet) [](#twikit.client.client.Client.unfavorite_tweet "Link to this definition")

Unfavorites a tweet.

Parameters:

**tweet_id** ( `str`) – The ID of the tweet to be unliked.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> tweet_id = '...'
>>> await client.unfavorite_tweet(tweet_id)

```

See also

[`favorite_tweet`](#twikit.client.client.Client.favorite_tweet "twikit.client.client.Client.favorite_tweet")

_async_ retweet( _tweet_id:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.retweet) [](#twikit.client.client.Client.retweet "Link to this definition")

Retweets a tweet.

Parameters:

**tweet_id** ( `str`) – The ID of the tweet to be retweeted.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> tweet_id = '...'
>>> await client.retweet(tweet_id)

```

See also

[`delete_retweet`](#twikit.client.client.Client.delete_retweet "twikit.client.client.Client.delete_retweet")

_async_ delete_retweet( _tweet_id:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.delete_retweet) [](#twikit.client.client.Client.delete_retweet "Link to this definition")

Deletes the retweet.

Parameters:

**tweet_id** ( `str`) – The ID of the retweeted tweet to be unretweeted.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> tweet_id = '...'
>>> await client.delete_retweet(tweet_id)

```

See also

[`retweet`](#twikit.client.client.Client.retweet "twikit.client.client.Client.retweet")

_async_ bookmark_tweet( _tweet_id:str_, _folder_id:str\|None=None_)→Response [\[source\]](_modules/twikit/client/client.html#Client.bookmark_tweet) [](#twikit.client.client.Client.bookmark_tweet "Link to this definition")

Adds the tweet to bookmarks.

Parameters:

- **tweet_id** ( `str`) – The ID of the tweet to be bookmarked.

- **folder_id** ( `str` \| None, default=None) – The ID of the folder to add the bookmark to.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> tweet_id = '...'
>>> await client.bookmark_tweet(tweet_id)

```

_async_ delete_bookmark( _tweet_id:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.delete_bookmark) [](#twikit.client.client.Client.delete_bookmark "Link to this definition")

Removes the tweet from bookmarks.

Parameters:

**tweet_id** ( `str`) – The ID of the tweet to be removed from bookmarks.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> tweet_id = '...'
>>> await client.delete_bookmark(tweet_id)

```

See also

[`bookmark_tweet`](#twikit.client.client.Client.bookmark_tweet "twikit.client.client.Client.bookmark_tweet")

_async_ get_bookmarks( _count:int=20_, _cursor:str\|None=None_, _folder_id:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/client/client.html#Client.get_bookmarks) [](#twikit.client.client.Client.get_bookmarks "Link to this definition")

Retrieves bookmarks from the authenticated user’s Twitter account.

Parameters:

- **count** ( `int`, default=20) – The number of bookmarks to retrieve.

- **folder_id** ( `str` \| None, default=None) – Folder to retrieve bookmarks.

Returns:

A Result object containing a list of Tweet objects
representing bookmarks.

Return type:

Result\[ `Tweet`\]

Example

```
>>> bookmarks = await client.get_bookmarks()
>>> for bookmark in bookmarks:
...     print(bookmark)
<Tweet id="...">
<Tweet id="...">

```

```
>>> # # To retrieve more bookmarks
>>> more_bookmarks = await bookmarks.next()
>>> for bookmark in more_bookmarks:
...     print(bookmark)
<Tweet id="...">
<Tweet id="...">

```

_async_ delete_all_bookmarks()→Response [\[source\]](_modules/twikit/client/client.html#Client.delete_all_bookmarks) [](#twikit.client.client.Client.delete_all_bookmarks "Link to this definition")

Deleted all bookmarks.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> await client.delete_all_bookmarks()

```

_async_ get_bookmark_folders( _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[BookmarkFolder\] [\[source\]](_modules/twikit/client/client.html#Client.get_bookmark_folders) [](#twikit.client.client.Client.get_bookmark_folders "Link to this definition")

Retrieves bookmark folders.

Returns:

Result object containing a list of bookmark folders.

Return type:

Result\[ `BookmarkFolder`\]

Examples

```
>>> folders = await client.get_bookmark_folders()
>>> print(folders)
[<BookmarkFolder id="...">, ..., <BookmarkFolder id="...">]
>>> more_folders = await folders.next()  # Retrieve more folders

```

_async_ edit_bookmark_folder( _folder_id:str_, _name:str_)→BookmarkFolder [\[source\]](_modules/twikit/client/client.html#Client.edit_bookmark_folder) [](#twikit.client.client.Client.edit_bookmark_folder "Link to this definition")

Edits a bookmark folder.

Parameters:

- **folder_id** ( `str`) – ID of the folder to edit.

- **name** ( `str`) – New name for the folder.

Returns:

Updated bookmark folder.

Return type:

`BookmarkFolder`

Examples

```
>>> await client.edit_bookmark_folder('123456789', 'MyFolder')

```

_async_ delete_bookmark_folder( _folder_id:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.delete_bookmark_folder) [](#twikit.client.client.Client.delete_bookmark_folder "Link to this definition")

Deletes a bookmark folder.

Parameters:

**folder_id** ( `str`) – ID of the folder to delete.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

_async_ create_bookmark_folder( _name:str_)→BookmarkFolder [\[source\]](_modules/twikit/client/client.html#Client.create_bookmark_folder) [](#twikit.client.client.Client.create_bookmark_folder "Link to this definition")

Creates a bookmark folder.

Parameters:

**name** ( `str`) – Name of the folder.

Returns:

Newly created bookmark folder.

Return type:

`BookmarkFolder`

_async_ follow_user( _user_id:str_)→[User](#twikit.user.User "twikit.user.User") [\[source\]](_modules/twikit/client/client.html#Client.follow_user) [](#twikit.client.client.Client.follow_user "Link to this definition")

Follows a user.

Parameters:

**user_id** ( `str`) – The ID of the user to follow.

Returns:

The followed user.

Return type:

`User`

Examples

```
>>> user_id = '...'
>>> await client.follow_user(user_id)

```

See also

[`unfollow_user`](#twikit.client.client.Client.unfollow_user "twikit.client.client.Client.unfollow_user")

_async_ unfollow_user( _user_id:str_)→[User](#twikit.user.User "twikit.user.User") [\[source\]](_modules/twikit/client/client.html#Client.unfollow_user) [](#twikit.client.client.Client.unfollow_user "Link to this definition")

Unfollows a user.

Parameters:

**user_id** ( `str`) – The ID of the user to unfollow.

Returns:

The unfollowed user.

Return type:

`User`

Examples

```
>>> user_id = '...'
>>> await client.unfollow_user(user_id)

```

See also

[`follow_user`](#twikit.client.client.Client.follow_user "twikit.client.client.Client.follow_user")

_async_ block_user( _user_id:str_)→[User](#twikit.user.User "twikit.user.User") [\[source\]](_modules/twikit/client/client.html#Client.block_user) [](#twikit.client.client.Client.block_user "Link to this definition")

Blocks a user.

Parameters:

**user_id** ( `str`) – The ID of the user to block.

Returns:

The blocked user.

Return type:

`User`

See also

[`unblock_user`](#twikit.client.client.Client.unblock_user "twikit.client.client.Client.unblock_user")

_async_ unblock_user( _user_id:str_)→[User](#twikit.user.User "twikit.user.User") [\[source\]](_modules/twikit/client/client.html#Client.unblock_user) [](#twikit.client.client.Client.unblock_user "Link to this definition")

Unblocks a user.

Parameters:

**user_id** ( `str`) – The ID of the user to unblock.

Returns:

The unblocked user.

Return type:

`User`

See also

[`block_user`](#twikit.client.client.Client.block_user "twikit.client.client.Client.block_user")

_async_ mute_user( _user_id:str_)→[User](#twikit.user.User "twikit.user.User") [\[source\]](_modules/twikit/client/client.html#Client.mute_user) [](#twikit.client.client.Client.mute_user "Link to this definition")

Mutes a user.

Parameters:

**user_id** ( `str`) – The ID of the user to mute.

Returns:

The muted user.

Return type:

`User`

See also

[`unmute_user`](#twikit.client.client.Client.unmute_user "twikit.client.client.Client.unmute_user")

_async_ unmute_user( _user_id:str_)→[User](#twikit.user.User "twikit.user.User") [\[source\]](_modules/twikit/client/client.html#Client.unmute_user) [](#twikit.client.client.Client.unmute_user "Link to this definition")

Unmutes a user.

Parameters:

**user_id** ( `str`) – The ID of the user to unmute.

Returns:

The unmuted user.

Return type:

`User`

See also

[`mute_user`](#twikit.client.client.Client.mute_user "twikit.client.client.Client.mute_user")

_async_ get_trends( _category:Literal\['trending','for-you','news','sports','entertainment'\]_, _count:int=20_, _retry:bool=True_, _additional_request_params:dict\|None=None_)→list\[ [Trend](#twikit.trend.Trend "twikit.trend.Trend")\] [\[source\]](_modules/twikit/client/client.html#Client.get_trends) [](#twikit.client.client.Client.get_trends "Link to this definition")

Retrieves trending topics on Twitter.

Parameters:

- **category** ( _{'trending'_ _,_ _'for-you'_ _,_ _'news'_ _,_ _'sports'_ _,_ _'entertainment'}_) – The category of trends to retrieve. Valid options include:
  \- ‘trending’: General trending topics.
  \- ‘for-you’: Trends personalized for the user.
  \- ‘news’: News-related trends.
  \- ‘sports’: Sports-related trends.
  \- ‘entertainment’: Entertainment-related trends.

- **count** ( `int`, default=20) – The number of trends to retrieve.

- **retry** ( `bool`, default=True) – If no trends are fetched continuously retry to fetch trends.

- **additional_request_params** ( `dict`, default=None) – Parameters to be added on top of the existing trends API
  parameters. Typically, it is used as additional_request_params =
  {‘candidate_source’: ‘trends’} when this function doesn’t work
  otherwise.

Returns:

A list of Trend objects representing the retrieved trends.

Return type:

list\[ `Trend`\]

Examples

```
>>> trends = await client.get_trends('trending')
>>> for trend in trends:
...     print(trend)
<Trend name="...">
<Trend name="...">
...

```

_async_ get_available_locations()→list\[ [Location](#twikit.trend.Location "twikit.trend.Location")\] [\[source\]](_modules/twikit/client/client.html#Client.get_available_locations) [](#twikit.client.client.Client.get_available_locations "Link to this definition")

Retrieves locations where trends can be retrieved.

Return type:

list\[ [`Location`](#twikit.trend.Location "twikit.trend.Location")\]

_async_ get_place_trends( _woeid:int_)→[PlaceTrends](#twikit.trend.PlaceTrends "twikit.trend.PlaceTrends") [\[source\]](_modules/twikit/client/client.html#Client.get_place_trends) [](#twikit.client.client.Client.get_place_trends "Link to this definition")

Retrieves the top 50 trending topics for a specific id.
You can get available woeid using
[`Client.get_available_locations`](#twikit.client.client.Client.get_available_locations "twikit.client.client.Client.get_available_locations").

_async_ get_user_followers( _user_id:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/client/client.html#Client.get_user_followers) [](#twikit.client.client.Client.get_user_followers "Link to this definition")

Retrieves a list of followers for a given user.

Parameters:

- **user_id** ( `str`) – The ID of the user for whom to retrieve followers.

- **count** ( _int_ _,_ _default=20_) – The number of followers to retrieve.

Returns:

A list of User objects representing the followers.

Return type:

Result\[ `User`\]

_async_ get_latest_followers( _user_id:str\|None=None_, _screen_name:str\|None=None_, _count:int=200_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/client/client.html#Client.get_latest_followers) [](#twikit.client.client.Client.get_latest_followers "Link to this definition")

Retrieves the latest followers.
Max count : 200

_async_ get_latest_friends( _user_id:str\|None=None_, _screen_name:str\|None=None_, _count:int=200_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/client/client.html#Client.get_latest_friends) [](#twikit.client.client.Client.get_latest_friends "Link to this definition")

Retrieves the latest friends (following users).
Max count : 200

_async_ get_user_verified_followers( _user_id:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/client/client.html#Client.get_user_verified_followers) [](#twikit.client.client.Client.get_user_verified_followers "Link to this definition")

Retrieves a list of verified followers for a given user.

Parameters:

- **user_id** ( `str`) – The ID of the user for whom to retrieve verified followers.

- **count** ( `int`, default=20) – The number of verified followers to retrieve.

Returns:

A list of User objects representing the verified followers.

Return type:

Result\[ `User`\]

_async_ get_user_followers_you_know( _user_id:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/client/client.html#Client.get_user_followers_you_know) [](#twikit.client.client.Client.get_user_followers_you_know "Link to this definition")

Retrieves a list of common followers.

Parameters:

- **user_id** ( `str`) – The ID of the user for whom to retrieve followers you might know.

- **count** ( `int`, default=20) – The number of followers you might know to retrieve.

Returns:

A list of User objects representing the followers you might know.

Return type:

Result\[ `User`\]

_async_ get_user_following( _user_id:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/client/client.html#Client.get_user_following) [](#twikit.client.client.Client.get_user_following "Link to this definition")

Retrieves a list of users whom the given user is following.

Parameters:

- **user_id** ( `str`) – The ID of the user for whom to retrieve the following users.

- **count** ( `int`, default=20) – The number of following users to retrieve.

Returns:

A list of User objects representing the users being followed.

Return type:

Result\[ `User`\]

_async_ get_user_subscriptions( _user_id:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/client/client.html#Client.get_user_subscriptions) [](#twikit.client.client.Client.get_user_subscriptions "Link to this definition")

Retrieves a list of users to which the specified user is subscribed.

Parameters:

- **user_id** ( `str`) – The ID of the user for whom to retrieve subscriptions.

- **count** ( `int`, default=20) – The number of subscriptions to retrieve.

Returns:

A list of User objects representing the subscribed users.

Return type:

Result\[ `User`\]

_async_ get_followers_ids( _user_id:str\|None=None_, _screen_name:str\|None=None_, _count:int=5000_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[int\] [\[source\]](_modules/twikit/client/client.html#Client.get_followers_ids) [](#twikit.client.client.Client.get_followers_ids "Link to this definition")

Fetches the IDs of the followers of a specified user.

Parameters:

- **user_id** ( `str` \| None, default=None) – The ID of the user for whom to return results.

- **screen_name** ( `str` \| None, default=None) – The screen name of the user for whom to return results.

- **count** ( `int`, default=5000) – The maximum number of IDs to retrieve.

Returns:

A Result object containing the IDs of the followers.

Return type:

`` Result`[:class:`int ``\]

_async_ get_friends_ids( _user_id:str\|None=None_, _screen_name:str\|None=None_, _count:int=5000_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[int\] [\[source\]](_modules/twikit/client/client.html#Client.get_friends_ids) [](#twikit.client.client.Client.get_friends_ids "Link to this definition")

Fetches the IDs of the friends (following users) of a specified user.

Parameters:

- **user_id** ( `str` \| None, default=None) – The ID of the user for whom to return results.

- **screen_name** ( `str` \| None, default=None) – The screen name of the user for whom to return results.

- **count** ( `int`, default=5000) – The maximum number of IDs to retrieve.

Returns:

A Result object containing the IDs of the friends.

Return type:

`` Result`[:class:`int ``\]

_async_ send_dm( _user_id:str_, _text:str_, _media_id:str\|None=None_, _reply_to:str\|None=None_)→[Message](#twikit.message.Message "twikit.message.Message") [\[source\]](_modules/twikit/client/client.html#Client.send_dm) [](#twikit.client.client.Client.send_dm "Link to this definition")

Send a direct message to a user.

Parameters:

- **user_id** ( `str`) – The ID of the user to whom the direct message will be sent.

- **text** ( `str`) – The text content of the direct message.

- **media_id** ( `str`, default=None) – The media ID associated with any media content
  to be included in the message.
  Media ID can be received by using the `upload_media()` method.

- **reply_to** ( `str`, default=None) – Message ID to reply to.

Returns:

Message object containing information about the message sent.

Return type:

`Message`

Examples

```
>>> # send DM with media
>>> user_id = '000000000'
>>> media_id = await client.upload_media('image.png')
>>> message = await client.send_dm(user_id, 'text', media_id)
>>> print(message)
<Message id='...'>

```

See also

[`upload_media`](#twikit.client.client.Client.upload_media "twikit.client.client.Client.upload_media"), [`delete_dm`](#twikit.client.client.Client.delete_dm "twikit.client.client.Client.delete_dm")

_async_ add_reaction_to_message( _message_id:str_, _conversation_id:str_, _emoji:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.add_reaction_to_message) [](#twikit.client.client.Client.add_reaction_to_message "Link to this definition")

Adds a reaction emoji to a specific message in a conversation.

Parameters:

- **message_id** ( `str`) – The ID of the message to which the reaction emoji will be added.
  Group ID (‘00000000’) or partner_ID-your_ID (‘00000000-00000001’)

- **conversation_id** ( `str`) – The ID of the conversation containing the message.

- **emoji** ( `str`) – The emoji to be added as a reaction.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> message_id = '00000000'
>>> conversation_id = f'00000001-{await client.user_id()}'
>>> await client.add_reaction_to_message(
...    message_id, conversation_id, 'Emoji here'
... )

```

_async_ remove_reaction_from_message( _message_id:str_, _conversation_id:str_, _emoji:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.remove_reaction_from_message) [](#twikit.client.client.Client.remove_reaction_from_message "Link to this definition")

Remove a reaction from a message.

Parameters:

- **message_id** ( `str`) – The ID of the message from which to remove the reaction.

- **conversation_id** ( `str`) – The ID of the conversation where the message is located.
  Group ID (‘00000000’) or partner_ID-your_ID (‘00000000-00000001’)

- **emoji** ( `str`) – The emoji to remove as a reaction.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> message_id = '00000000'
>>> conversation_id = f'00000001-{await client.user_id()}'
>>> await client.remove_reaction_from_message(
...    message_id, conversation_id, 'Emoji here'
... )

```

_async_ delete_dm( _message_id:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.delete_dm) [](#twikit.client.client.Client.delete_dm "Link to this definition")

Deletes a direct message with the specified message ID.

Parameters:

**message_id** ( `str`) – The ID of the direct message to be deleted.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> await client.delete_dm('0000000000')

```

_async_ get_dm_history( _user_id:str_, _max_id:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Message](#twikit.message.Message "twikit.message.Message")\] [\[source\]](_modules/twikit/client/client.html#Client.get_dm_history) [](#twikit.client.client.Client.get_dm_history "Link to this definition")

Retrieves the DM conversation history with a specific user.

Parameters:

- **user_id** ( `str`) – The ID of the user with whom the DM conversation
  history will be retrieved.

- **max_id** ( `str`, default=None) – If specified, retrieves messages older than the specified max_id.

Returns:

A Result object containing a list of Message objects representing
the DM conversation history.

Return type:

Result\[ `Message`\]

Examples

```
>>> messages = await client.get_dm_history('0000000000')
>>> for message in messages:
>>>     print(message)
<Message id="...">
<Message id="...">
...
...

```

```
>>> more_messages = await messages.next()  # Retrieve more messages
>>> for message in more_messages:
>>>     print(message)
<Message id="...">
<Message id="...">
...
...

```

_async_ send_dm_to_group( _group_id:str_, _text:str_, _media_id:str\|None=None_, _reply_to:str\|None=None_)→GroupMessage [\[source\]](_modules/twikit/client/client.html#Client.send_dm_to_group) [](#twikit.client.client.Client.send_dm_to_group "Link to this definition")

Sends a message to a group.

Parameters:

- **group_id** ( `str`) – The ID of the group in which the direct message will be sent.

- **text** ( `str`) – The text content of the direct message.

- **media_id** ( `str`, default=None) – The media ID associated with any media content
  to be included in the message.
  Media ID can be received by using the `upload_media()` method.

- **reply_to** ( `str`, default=None) – Message ID to reply to.

Returns:

GroupMessage object containing information about
the message sent.

Return type:

`GroupMessage`

Examples

```
>>> # send DM with media
>>> group_id = '000000000'
>>> media_id = await client.upload_media('image.png')
>>> message = await client.send_dm_to_group(group_id, 'text', media_id)
>>> print(message)
<GroupMessage id='...'>

```

See also

[`upload_media`](#twikit.client.client.Client.upload_media "twikit.client.client.Client.upload_media"), [`delete_dm`](#twikit.client.client.Client.delete_dm "twikit.client.client.Client.delete_dm")

_async_ get_group_dm_history( _group_id:str_, _max_id:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[GroupMessage\] [\[source\]](_modules/twikit/client/client.html#Client.get_group_dm_history) [](#twikit.client.client.Client.get_group_dm_history "Link to this definition")

Retrieves the DM conversation history in a group.

Parameters:

- **group_id** ( `str`) – The ID of the group in which the DM conversation
  history will be retrieved.

- **max_id** ( `str`, default=None) – If specified, retrieves messages older than the specified max_id.

Returns:

A Result object containing a list of GroupMessage objects
representing the DM conversation history.

Return type:

Result\[ `GroupMessage`\]

Examples

```
>>> messages = await client.get_group_dm_history('0000000000')
>>> for message in messages:
>>>     print(message)
<GroupMessage id="...">
<GroupMessage id="...">
...
...

```

```
>>> more_messages = await messages.next()  # Retrieve more messages
>>> for message in more_messages:
>>>     print(message)
<GroupMessage id="...">
<GroupMessage id="...">
...
...

```

_async_ get_group( _group_id:str_)→Group [\[source\]](_modules/twikit/client/client.html#Client.get_group) [](#twikit.client.client.Client.get_group "Link to this definition")

Fetches a guild by ID.

Parameters:

**group_id** ( `str`) – The ID of the group to retrieve information for.

Returns:

An object representing the retrieved group.

Return type:

`Group`

_async_ add_members_to_group( _group_id:str_, _user_ids:list\[str\]_)→Response [\[source\]](_modules/twikit/client/client.html#Client.add_members_to_group) [](#twikit.client.client.Client.add_members_to_group "Link to this definition")

Adds members to a group.

Parameters:

- **group_id** ( `str`) – ID of the group to which the member is to be added.

- **user_ids** (list\[ `str`\]) – List of IDs of users to be added.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> group_id = '...'
>>> members = ['...']
>>> await client.add_members_to_group(group_id, members)

```

_async_ change_group_name( _group_id:str_, _name:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.change_group_name) [](#twikit.client.client.Client.change_group_name "Link to this definition")

Changes group name

Parameters:

- **group_id** ( `str`) – ID of the group to be renamed.

- **name** ( `str`) – New name.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

_async_ create_list( _name:str_, _description:str=''_, _is_private:bool=False_)→[List](#twikit.list.List "twikit.list.List") [\[source\]](_modules/twikit/client/client.html#Client.create_list) [](#twikit.client.client.Client.create_list "Link to this definition")

Creates a list.

Parameters:

- **name** ( `str`) – The name of the list.

- **description** ( `str`, default=’’) – The description of the list.

- **is_private** ( `bool`, default=False) – Indicates whether the list is private (True) or public (False).

Returns:

The created list.

Return type:

`List`

Examples

```
>>> list = await client.create_list(
...     'list name',
...     'list description',
...     is_private=True
... )
>>> print(list)
<List id="...">

```

_async_ edit_list_banner( _list_id:str_, _media_id:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.edit_list_banner) [](#twikit.client.client.Client.edit_list_banner "Link to this definition")

Edit the banner image of a list.

Parameters:

- **list_id** ( `str`) – The ID of the list.

- **media_id** ( `str`) – The ID of the media to use as the new banner image.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> list_id = '...'
>>> media_id = await client.upload_media('image.png')
>>> await client.edit_list_banner(list_id, media_id)

```

_async_ delete_list_banner( _list_id:str_)→Response [\[source\]](_modules/twikit/client/client.html#Client.delete_list_banner) [](#twikit.client.client.Client.delete_list_banner "Link to this definition")

Deletes list banner.

Parameters:

**list_id** ( `str`) – ID of the list from which the banner is to be removed.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

_async_ edit_list( _list_id:str_, _name:str\|None=None_, _description:str\|None=None_, _is_private:bool\|None=None_)→[List](#twikit.list.List "twikit.list.List") [\[source\]](_modules/twikit/client/client.html#Client.edit_list) [](#twikit.client.client.Client.edit_list "Link to this definition")

Edits list information.

Parameters:

- **list_id** ( `str`) – The ID of the list to edit.

- **name** ( `str`, default=None) – The new name for the list.

- **description** ( `str`, default=None) – The new description for the list.

- **is_private** ( `bool`, default=None) – Indicates whether the list should be private
  (True) or public (False).

Returns:

The updated Twitter list.

Return type:

`List`

Examples

```
>>> await client.edit_list(
...     'new name', 'new description', True
... )

```

_async_ add_list_member( _list_id:str_, _user_id:str_)→[List](#twikit.list.List "twikit.list.List") [\[source\]](_modules/twikit/client/client.html#Client.add_list_member) [](#twikit.client.client.Client.add_list_member "Link to this definition")

Adds a user to a list.

Parameters:

- **list_id** ( `str`) – The ID of the list.

- **user_id** ( `str`) – The ID of the user to add to the list.

Returns:

The updated Twitter list.

Return type:

`List`

Examples

```
>>> await client.add_list_member('list id', 'user id')

```

_async_ remove_list_member( _list_id:str_, _user_id:str_)→[List](#twikit.list.List "twikit.list.List") [\[source\]](_modules/twikit/client/client.html#Client.remove_list_member) [](#twikit.client.client.Client.remove_list_member "Link to this definition")

Removes a user from a list.

Parameters:

- **list_id** ( `str`) – The ID of the list.

- **user_id** ( `str`) – The ID of the user to remove from the list.

Returns:

The updated Twitter list.

Return type:

`List`

Examples

```
>>> await client.remove_list_member('list id', 'user id')

```

_async_ get_lists( _count:int=100_, _cursor:str=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [List](#twikit.list.List "twikit.list.List")\] [\[source\]](_modules/twikit/client/client.html#Client.get_lists) [](#twikit.client.client.Client.get_lists "Link to this definition")

Retrieves a list of user lists.

Parameters:

**count** ( `int`) – The number of lists to retrieve.

Returns:

Retrieved lists.

Return type:

Result\[ `List`\]

Examples

```
>>> lists = client.get_lists()
>>> for list_ in lists:
...     print(list_)
<List id="...">
<List id="...">
...
...
>>> more_lists = lists.next()  # Retrieve more lists

```

_async_ get_list( _list_id:str_)→[List](#twikit.list.List "twikit.list.List") [\[source\]](_modules/twikit/client/client.html#Client.get_list) [](#twikit.client.client.Client.get_list "Link to this definition")

Retrieve list by ID.

Parameters:

**list_id** ( `str`) – The ID of the list to retrieve.

Returns:

List object.

Return type:

`List`

_async_ get_list_tweets( _list_id:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/client/client.html#Client.get_list_tweets) [](#twikit.client.client.Client.get_list_tweets "Link to this definition")

Retrieves tweets from a list.

Parameters:

- **list_id** ( `str`) – The ID of the list to retrieve tweets from.

- **count** ( `int`, default=20) – The number of tweets to retrieve.

- **cursor** ( `str`, default=None) – The cursor for pagination.

Returns:

A Result object containing the retrieved tweets.

Return type:

Result\[ `Tweet`\]

Examples

```
>>> tweets = await client.get_list_tweets('list id')
>>> for tweet in tweets:
...    print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

```
>>> more_tweets = await tweets.next()  # Retrieve more tweets
>>> for tweet in more_tweets:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

_async_ get_list_members( _list_id:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/client/client.html#Client.get_list_members) [](#twikit.client.client.Client.get_list_members "Link to this definition")

Retrieves members of a list.

Parameters:

- **list_id** ( `str`) – List ID.

- **count** ( _int_ _,_ _default=20_) – Number of members to retrieve.

Returns:

Members of a list

Return type:

Result\[ `User`\]

Examples

```
>>> members = client.get_list_members(123456789)
>>> for member in members:
...     print(member)
<User id="...">
<User id="...">
...
...
>>> more_members = members.next()  # Retrieve more members

```

_async_ get_list_subscribers( _list_id:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/client/client.html#Client.get_list_subscribers) [](#twikit.client.client.Client.get_list_subscribers "Link to this definition")

Retrieves subscribers of a list.

Parameters:

- **list_id** ( `str`) – List ID.

- **count** ( `int`, default=20) – Number of subscribers to retrieve.

Returns:

Subscribers of a list

Return type:

Result\[ `User`\]

Examples

```
>>> members = client.get_list_subscribers(123456789)
>>> for subscriber in subscribers:
...     print(subscriber)
<User id="...">
<User id="...">
...
...
>>> more_subscribers = members.next()  # Retrieve more subscribers

```

_async_ search_list( _query:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [List](#twikit.list.List "twikit.list.List")\] [\[source\]](_modules/twikit/client/client.html#Client.search_list) [](#twikit.client.client.Client.search_list "Link to this definition")

Search for lists based on the provided query.

Parameters:

- **query** ( `str`) – The search query.

- **count** ( `int`, default=20) – The number of lists to retrieve.

Returns:

An instance of the Result class containing the
search results.

Return type:

Result\[ `List`\]

Examples

```
>>> lists = await client.search_list('query')
>>> for list in lists:
...     print(list)
<List id="...">
<List id="...">
...

```

```
>>> more_lists = await lists.next()  # Retrieve more lists

```

_async_ get_notifications( _type:Literal\['All','Verified','Mentions'\]_, _count:int=40_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Notification](#twikit.notification.Notification "twikit.notification.Notification")\] [\[source\]](_modules/twikit/client/client.html#Client.get_notifications) [](#twikit.client.client.Client.get_notifications "Link to this definition")

Retrieve notifications based on the provided type.

Parameters:

- **type** ( _{'All'_ _,_ _'Verified'_ _,_ _'Mentions'}_) – Type of notifications to retrieve.
  All: All notifications
  Verified: Notifications relating to authenticated users
  Mentions: Notifications with mentions

- **count** ( `int`, default=40) – Number of notifications to retrieve.

Returns:

List of retrieved notifications.

Return type:

Result\[ `Notification`\]

Examples

```
>>> notifications = await client.get_notifications('All')
>>> for notification in notifications:
...     print(notification)
<Notification id="...">
<Notification id="...">
...
...

```

```
>>> # Retrieve more notifications
>>> more_notifications = await notifications.next()

```

_async_ search_community( _query:str_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Community](#twikit.community.Community "twikit.community.Community")\] [\[source\]](_modules/twikit/client/client.html#Client.search_community) [](#twikit.client.client.Client.search_community "Link to this definition")

Searchs communities based on the specified query.

Parameters:

**query** ( `str`) – The search query.

Returns:

List of retrieved communities.

Return type:

Result\[ `Community`\]

Examples

```
>>> communities = await client.search_communities('query')
>>> for community in communities:
...     print(community)
<Community id="...">
<Community id="...">
...

```

```
>>> # Retrieve more communities
>>> more_communities = await communities.next()

```

_async_ get_community( _community_id:str_)→[Community](#twikit.community.Community "twikit.community.Community") [\[source\]](_modules/twikit/client/client.html#Client.get_community) [](#twikit.client.client.Client.get_community "Link to this definition")

Retrieves community by ID.

Parameters:

**list_id** ( `str`) – The ID of the community to retrieve.

Returns:

Community object.

Return type:

`Community`

_async_ get_community_tweets( _community_id:str_, _tweet_type:Literal\['Top','Latest','Media'\]_, _count:int=40_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/client/client.html#Client.get_community_tweets) [](#twikit.client.client.Client.get_community_tweets "Link to this definition")

Retrieves tweets from a community.

Parameters:

- **community_id** ( `str`) – The ID of the community.

- **tweet_type** ( _{'Top'_ _,_ _'Latest'_ _,_ _'Media'}_) – The type of tweets to retrieve.

- **count** ( `int`, default=40) – The number of tweets to retrieve.

Returns:

List of retrieved tweets.

Return type:

Result\[ `Tweet`\]

Examples

```
>>> community_id = '...'
>>> tweets = await client.get_community_tweets(community_id, 'Latest')
>>> for tweet in tweets:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
>>> more_tweets = await tweets.next()  # Retrieve more tweets

```

_async_ get_communities_timeline( _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/client/client.html#Client.get_communities_timeline) [](#twikit.client.client.Client.get_communities_timeline "Link to this definition")

Retrieves tweets from communities timeline.

Parameters:

**count** ( `int`, default=20) – The number of tweets to retrieve.

Returns:

List of retrieved tweets.

Return type:

Result\[ `Tweet`\]

Examples

```
>>> tweets = await client.get_communities_timeline()
>>> for tweet in tweets:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
>>> more_tweets = await tweets.next()  # Retrieve more tweets

```

_async_ join_community( _community_id:str_)→[Community](#twikit.community.Community "twikit.community.Community") [\[source\]](_modules/twikit/client/client.html#Client.join_community) [](#twikit.client.client.Client.join_community "Link to this definition")

Join a community.

Parameters:

**community_id** ( `str`) – The ID of the community to join.

Returns:

The joined community.

Return type:

`Community`

_async_ leave_community( _community_id:str_)→[Community](#twikit.community.Community "twikit.community.Community") [\[source\]](_modules/twikit/client/client.html#Client.leave_community) [](#twikit.client.client.Client.leave_community "Link to this definition")

Leave a community.

Parameters:

**community_id** ( `str`) – The ID of the community to leave.

Returns:

The left community.

Return type:

`Community`

_async_ request_to_join_community( _community_id:str_, _answer:str\|None=None_)→[Community](#twikit.community.Community "twikit.community.Community") [\[source\]](_modules/twikit/client/client.html#Client.request_to_join_community) [](#twikit.client.client.Client.request_to_join_community "Link to this definition")

Request to join a community.

Parameters:

- **community_id** ( `str`) – The ID of the community to request to join.

- **answer** ( `str`, default=None) – The answer to the join request.

Returns:

The requested community.

Return type:

`Community`

_async_ get_community_members( _community_id:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [CommunityMember](#twikit.community.CommunityMember "twikit.community.CommunityMember")\] [\[source\]](_modules/twikit/client/client.html#Client.get_community_members) [](#twikit.client.client.Client.get_community_members "Link to this definition")

Retrieves members of a community.

Parameters:

- **community_id** ( `str`) – The ID of the community.

- **count** ( `int`, default=20) – The number of members to retrieve.

Returns:

List of retrieved members.

Return type:

Result\[ `CommunityMember`\]

_async_ get_community_moderators( _community_id:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [CommunityMember](#twikit.community.CommunityMember "twikit.community.CommunityMember")\] [\[source\]](_modules/twikit/client/client.html#Client.get_community_moderators) [](#twikit.client.client.Client.get_community_moderators "Link to this definition")

Retrieves moderators of a community.

Parameters:

- **community_id** ( `str`) – The ID of the community.

- **count** ( `int`, default=20) – The number of moderators to retrieve.

Returns:

List of retrieved moderators.

Return type:

Result\[ `CommunityMember`\]

_async_ search_community_tweet( _community_id:str_, _query:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/client/client.html#Client.search_community_tweet) [](#twikit.client.client.Client.search_community_tweet "Link to this definition")

Searchs tweets in a community.

Parameters:

- **community_id** ( `str`) – The ID of the community.

- **query** ( `str`) – The search query.

- **count** ( `int`, default=20) – The number of tweets to retrieve.

Returns:

List of retrieved tweets.

Return type:

Result\[ `Tweet`\]

_async_ get_streaming_session( _topics:set\[str\]_, _auto_reconnect:bool=True_)→[StreamingSession](#twikit.streaming.StreamingSession "twikit.streaming.StreamingSession") [\[source\]](_modules/twikit/client/client.html#Client.get_streaming_session) [](#twikit.client.client.Client.get_streaming_session "Link to this definition")

Returns a session for interacting with the streaming API.

Parameters:

- **topics** (set\[ `str`\]) – The set of topics to stream.
  Topics can be generated using [`Topic`](#twikit.streaming.Topic "twikit.streaming.Topic").

- **auto_reconnect** ( `bool`, default=True) – Whether to automatically reconnect when disconnected.

Returns:

A stream session instance.

Return type:

[`StreamingSession`](#twikit.streaming.StreamingSession "twikit.streaming.StreamingSession")

Examples

```
>>> from twikit.streaming import Topic
>>>
>>> topics = {
...     Topic.tweet_engagement('1739617652'), # Stream tweet engagement
...     Topic.dm_update('17544932482-174455537996'), # Stream DM update
...     Topic.dm_typing('17544932482-174455537996') # Stream DM typing
... }
>>> session = await client.get_streaming_session(topics)
>>>
>>> async for topic, payload in session:
...     if payload.dm_update:
...         conversation_id = payload.dm_update.conversation_id
...         user_id = payload.dm_update.user_id
...         print(f'{conversation_id}: {user_id} sent a message')
>>>
>>>     if payload.dm_typing:
...         conversation_id = payload.dm_typing.conversation_id
...         user_id = payload.dm_typing.user_id
...         print(f'{conversation_id}: {user_id} is typing')
>>>
>>>     if payload.tweet_engagement:
...         like = payload.tweet_engagement.like_count
...         retweet = payload.tweet_engagement.retweet_count
...         view = payload.tweet_engagement.view_count
...         print('Tweet engagement updated:'
...               f'likes: {like} retweets: {retweet} views: {view}')

```

Topics to stream can be added or deleted using
[`StreamingSession.update_subscriptions`](#twikit.streaming.StreamingSession.update_subscriptions "twikit.streaming.StreamingSession.update_subscriptions") method.

```
>>> subscribe_topics = {
...     Topic.tweet_engagement('1749528513'),
...     Topic.tweet_engagement('1765829534')
... }
>>> unsubscribe_topics = {
...     Topic.tweet_engagement('1739617652'),
...     Topic.dm_update('17544932482-174455537996'),
...     Topic.dm_update('17544932482-174455537996')
... }
>>> await session.update_subscriptions(
...     subscribe_topics, unsubscribe_topics
... )

```

See also

[`StreamingSession`](#twikit.streaming.StreamingSession "twikit.streaming.StreamingSession"), [`StreamingSession.update_subscriptions`](#twikit.streaming.StreamingSession.update_subscriptions "twikit.streaming.StreamingSession.update_subscriptions"), [`Payload`](#twikit.streaming.Payload "twikit.streaming.Payload"), [`Topic`](#twikit.streaming.Topic "twikit.streaming.Topic")

## Tweet [](#module-twikit.tweet "Link to this heading")

_class_ twikit.tweet.Tweet( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _data:dict_, _user:[User](#twikit.user.User "twikit.user.User")=None_) [\[source\]](_modules/twikit/tweet.html#Tweet) [](#twikit.tweet.Tweet "Link to this definition")id [](#twikit.tweet.Tweet.id "Link to this definition")

The unique identifier of the tweet.

Type:

`str`

created_at [](#twikit.tweet.Tweet.created_at "Link to this definition")

The date and time when the tweet was created.

Type:

`str`

created_at_datetime [](#twikit.tweet.Tweet.created_at_datetime "Link to this definition")

The created_at converted to datetime.

Type:

`datetime`

user [](#twikit.tweet.Tweet.user "Link to this definition")

Author of the tweet.

Type:

`User`

text [](#twikit.tweet.Tweet.text "Link to this definition")

The full text of the tweet.

Type:

`str`

lang [](#twikit.tweet.Tweet.lang "Link to this definition")

The language of the tweet.

Type:

`str`

in_reply_to [](#twikit.tweet.Tweet.in_reply_to "Link to this definition")

The tweet ID this tweet is in reply to, if any

Type:

`str`

is_quote_status [](#twikit.tweet.Tweet.is_quote_status "Link to this definition")

Indicates if the tweet is a quote status.

Type:

`bool`

quote [](#twikit.tweet.Tweet.quote "Link to this definition")

The Tweet being quoted (if any)

Type:

[`Tweet`](#twikit.tweet.Tweet "twikit.tweet.Tweet") \| None

retweeted_tweet [](#twikit.tweet.Tweet.retweeted_tweet "Link to this definition")

The Tweet being retweeted (if any)

Type:

[`Tweet`](#twikit.tweet.Tweet "twikit.tweet.Tweet") \| None

possibly_sensitive [](#twikit.tweet.Tweet.possibly_sensitive "Link to this definition")

Indicates if the tweet content may be sensitive.

Type:

`bool`

possibly_sensitive_editable [](#twikit.tweet.Tweet.possibly_sensitive_editable "Link to this definition")

Indicates if the tweet’s sensitivity can be edited.

Type:

`bool`

quote_count [](#twikit.tweet.Tweet.quote_count "Link to this definition")

The count of quotes for the tweet.

Type:

`int`

media [](#twikit.tweet.Tweet.media "Link to this definition")

A list of media entities associated with the tweet.

Type:

`list`

reply_count [](#twikit.tweet.Tweet.reply_count "Link to this definition")

The count of replies to the tweet.

Type:

`int`

favorite_count [](#twikit.tweet.Tweet.favorite_count "Link to this definition")

The count of favorites or likes for the tweet.

Type:

`int`

favorited [](#twikit.tweet.Tweet.favorited "Link to this definition")

Indicates if the tweet is favorited.

Type:

`bool`

view_count [](#twikit.tweet.Tweet.view_count "Link to this definition")

The count of views.

Type:

`int` \| None

view_count_state [](#twikit.tweet.Tweet.view_count_state "Link to this definition")

The state of the tweet views.

Type:

`str` \| None

retweet_count [](#twikit.tweet.Tweet.retweet_count "Link to this definition")

The count of retweets for the tweet.

Type:

`int`

place [](#twikit.tweet.Tweet.place "Link to this definition")

The location associated with the tweet.

Type:

[`Place`](#twikit.geo.Place "twikit.geo.Place") \| None

editable_until_msecs [](#twikit.tweet.Tweet.editable_until_msecs "Link to this definition")

The timestamp until which the tweet is editable.

Type:

`int`

is_translatable [](#twikit.tweet.Tweet.is_translatable "Link to this definition")

Indicates if the tweet is translatable.

Type:

`bool`

is_edit_eligible [](#twikit.tweet.Tweet.is_edit_eligible "Link to this definition")

Indicates if the tweet is eligible for editing.

Type:

`bool`

edits_remaining [](#twikit.tweet.Tweet.edits_remaining "Link to this definition")

The remaining number of edits allowed for the tweet.

Type:

`int`

replies [](#twikit.tweet.Tweet.replies "Link to this definition")

Replies to the tweet.

Type:

Result\[ [`Tweet`](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] \| None

reply_to [](#twikit.tweet.Tweet.reply_to "Link to this definition")

A list of Tweet objects representing the tweets to which to reply.

Type:

list\[ [`Tweet`](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] \| None

related_tweets [](#twikit.tweet.Tweet.related_tweets "Link to this definition")

Related tweets.

Type:

list\[ [`Tweet`](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] \| None

hashtags [](#twikit.tweet.Tweet.hashtags "Link to this definition")

Hashtags included in the tweet text.

Type:

list\[ `str`\]

has_card [](#twikit.tweet.Tweet.has_card "Link to this definition")

Indicates if the tweet contains a card.

Type:

`bool`

thumbnail_title [](#twikit.tweet.Tweet.thumbnail_title "Link to this definition")

The title of the webpage displayed inside tweet’s card.

Type:

`str` \| None

thumbnail_url [](#twikit.tweet.Tweet.thumbnail_url "Link to this definition")

Link to the image displayed in the tweet’s card.

Type:

`str` \| None

urls [](#twikit.tweet.Tweet.urls "Link to this definition")

Information about URLs contained in the tweet.

Type:

`list`

full_text [](#twikit.tweet.Tweet.full_text "Link to this definition")

The full text of the tweet.

Type:

`str` \| None

_async_ delete()→Response [\[source\]](_modules/twikit/tweet.html#Tweet.delete) [](#twikit.tweet.Tweet.delete "Link to this definition")

Deletes the tweet.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> await tweet.delete()

```

_async_ favorite()→Response [\[source\]](_modules/twikit/tweet.html#Tweet.favorite) [](#twikit.tweet.Tweet.favorite "Link to this definition")

Favorites the tweet.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

See also

`Client.favorite_tweet`

_async_ unfavorite()→Response [\[source\]](_modules/twikit/tweet.html#Tweet.unfavorite) [](#twikit.tweet.Tweet.unfavorite "Link to this definition")

Favorites the tweet.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

See also

`Client.unfavorite_tweet`

_async_ retweet()→Response [\[source\]](_modules/twikit/tweet.html#Tweet.retweet) [](#twikit.tweet.Tweet.retweet "Link to this definition")

Retweets the tweet.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

See also

`Client.retweet`

_async_ delete_retweet()→Response [\[source\]](_modules/twikit/tweet.html#Tweet.delete_retweet) [](#twikit.tweet.Tweet.delete_retweet "Link to this definition")

Deletes the retweet.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

See also

`Client.delete_retweet`

_async_ bookmark()→Response [\[source\]](_modules/twikit/tweet.html#Tweet.bookmark) [](#twikit.tweet.Tweet.bookmark "Link to this definition")

Adds the tweet to bookmarks.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

See also

`Client.bookmark_tweet`

_async_ delete_bookmark()→Response [\[source\]](_modules/twikit/tweet.html#Tweet.delete_bookmark) [](#twikit.tweet.Tweet.delete_bookmark "Link to this definition")

Removes the tweet from bookmarks.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

See also

`Client.delete_bookmark`

_async_ reply( _text:str=''_, _media_ids:list\[str\]\|None=None_, _\*\*kwargs_)→[Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet") [\[source\]](_modules/twikit/tweet.html#Tweet.reply) [](#twikit.tweet.Tweet.reply "Link to this definition")

Replies to the tweet.

Parameters:

- **text** ( `str`, default=’’) – The text content of the reply.

- **media_ids** (list\[ `str`\], default=None) – A list of media IDs or URIs to attach to the reply.
  Media IDs can be obtained by using the upload_media method.

Returns:

The created tweet.

Return type:

[`Tweet`](#twikit.tweet.Tweet "twikit.tweet.Tweet")

Examples

```
>>> tweet_text = 'Example text'
>>> media_ids = [\
...     client.upload_media('image1.png'),\
...     client.upload_media('image2.png')\
... ]
>>> await tweet.reply(
...     tweet_text,
...     media_ids=media_ids
... )

```

See also

`None`

_async_ get_retweeters( _count:str=40_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/tweet.html#Tweet.get_retweeters) [](#twikit.tweet.Tweet.get_retweeters "Link to this definition")

Retrieve users who retweeted the tweet.

Parameters:

- **count** ( `int`, default=40) – The maximum number of users to retrieve.

- **cursor** ( `str`, default=None) – A string indicating the position of the cursor for pagination.

Returns:

A list of users who retweeted the tweet.

Return type:

Result\[ `User`\]

Examples

```
>>> tweet_id = '...'
>>> retweeters = tweet.get_retweeters()
>>> print(retweeters)
[<User id="...">, <User id="...">, ..., <User id="...">]

```

```
>>> more_retweeters = retweeters.next()  # Retrieve more retweeters.
>>> print(more_retweeters)
[<User id="...">, <User id="...">, ..., <User id="...">]

```

_async_ get_favoriters( _count:str=40_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/tweet.html#Tweet.get_favoriters) [](#twikit.tweet.Tweet.get_favoriters "Link to this definition")

Retrieve users who favorited a specific tweet.

Parameters:

- **tweet_id** ( `str`) – The ID of the tweet.

- **count** ( `int`, default=40) – The maximum number of users to retrieve.

- **cursor** ( `str`, default=None) – A string indicating the position of the cursor for pagination.

Returns:

A list of users who favorited the tweet.

Return type:

Result\[ `User`\]

Examples

```
>>> tweet_id = '...'
>>> favoriters = tweet.get_favoriters()
>>> print(favoriters)
[<User id="...">, <User id="...">, ..., <User id="...">]

```

```
>>> more_favoriters = favoriters.next()  # Retrieve more favoriters.
>>> print(more_favoriters)
[<User id="...">, <User id="...">, ..., <User id="...">]

```

_async_ get_similar_tweets()→list\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/tweet.html#Tweet.get_similar_tweets) [](#twikit.tweet.Tweet.get_similar_tweets "Link to this definition")

Retrieves tweets similar to the tweet (Twitter premium only).

Returns:

A list of Tweet objects representing tweets
similar to the tweet.

Return type:

list\[ [`Tweet`](#twikit.tweet.Tweet "twikit.tweet.Tweet")\]

_class_ twikit.tweet.Poll( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _data:dict_, _tweet:[Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet") \|None=None_) [\[source\]](_modules/twikit/tweet.html#Poll) [](#twikit.tweet.Poll "Link to this definition")

Represents a poll associated with a tweet.
.. attribute:: tweet

> The tweet associated with the poll.
>
> type:
>
> [`Tweet`](#twikit.tweet.Tweet "twikit.tweet.Tweet")

id [](#twikit.tweet.Poll.id "Link to this definition")

The unique identifier of the poll.

Type:

`str`

name [](#twikit.tweet.Poll.name "Link to this definition")

The name of the poll.

Type:

`str`

choices [](#twikit.tweet.Poll.choices "Link to this definition")

A list containing dictionaries representing poll choices.
Each dictionary contains ‘label’ and ‘count’ keys
for choice label and count.

Type:

list\[ `dict`\]

duration_minutes [](#twikit.tweet.Poll.duration_minutes "Link to this definition")

The duration of the poll in minutes.

Type:

`int`

end_datetime_utc [](#twikit.tweet.Poll.end_datetime_utc "Link to this definition")

The end date and time of the poll in UTC format.

Type:

`str`

last_updated_datetime_utc [](#twikit.tweet.Poll.last_updated_datetime_utc "Link to this definition")

The last updated date and time of the poll in UTC format.

Type:

`str`

selected_choice [](#twikit.tweet.Poll.selected_choice "Link to this definition")

Number of the selected choice.

Type:

`str` \| None

_async_ vote( _selected_choice:str_)→[Poll](#twikit.tweet.Poll "twikit.tweet.Poll") [\[source\]](_modules/twikit/tweet.html#Poll.vote) [](#twikit.tweet.Poll.vote "Link to this definition")

Vote on the poll with the specified selected choice.
:param selected_choice: The label of the selected choice for the vote.
:type selected_choice: `str`

Returns:

The Poll object representing the updated poll after voting.

Return type:

[`Poll`](#twikit.tweet.Poll "twikit.tweet.Poll")

_class_ twikit.tweet.CommunityNote( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _data:dict_) [\[source\]](_modules/twikit/tweet.html#CommunityNote) [](#twikit.tweet.CommunityNote "Link to this definition")

Represents a community note.

id [](#twikit.tweet.CommunityNote.id "Link to this definition")

The ID of the community note.

Type:

`str`

text [](#twikit.tweet.CommunityNote.text "Link to this definition")

The text content of the community note.

Type:

`str`

misleading_tags [](#twikit.tweet.CommunityNote.misleading_tags "Link to this definition")

A list of tags indicating misleading information.

Type:

list\[ `str`\]

trustworthy_sources [](#twikit.tweet.CommunityNote.trustworthy_sources "Link to this definition")

Indicates if the sources are trustworthy.

Type:

`bool`

helpful_tags [](#twikit.tweet.CommunityNote.helpful_tags "Link to this definition")

A list of tags indicating helpful information.

Type:

list\[ `str`\]

created_at [](#twikit.tweet.CommunityNote.created_at "Link to this definition")

The timestamp when the note was created.

Type:

`int`

can_appeal [](#twikit.tweet.CommunityNote.can_appeal "Link to this definition")

Indicates if the note can be appealed.

Type:

`bool`

appeal_status [](#twikit.tweet.CommunityNote.appeal_status "Link to this definition")

The status of the appeal.

Type:

`str`

is_media_note [](#twikit.tweet.CommunityNote.is_media_note "Link to this definition")

Indicates if the note is related to media content.

Type:

`bool`

media_note_matches [](#twikit.tweet.CommunityNote.media_note_matches "Link to this definition")

Matches related to media content.

Type:

`str`

birdwatch_profile [](#twikit.tweet.CommunityNote.birdwatch_profile "Link to this definition")

Birdwatch profile associated with the note.

Type:

`dict`

tweet_id [](#twikit.tweet.CommunityNote.tweet_id "Link to this definition")

The ID of the tweet associated with the note.

Type:

`str`

## User [](#module-twikit.user "Link to this heading")

_class_ twikit.user.User( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _data:dict_) [\[source\]](_modules/twikit/user.html#User) [](#twikit.user.User "Link to this definition")id [](#twikit.user.User.id "Link to this definition")

The unique identifier of the user.

Type:

`str`

created_at [](#twikit.user.User.created_at "Link to this definition")

The date and time when the user account was created.

Type:

`str`

name [](#twikit.user.User.name "Link to this definition")

The user’s name.

Type:

`str`

screen_name [](#twikit.user.User.screen_name "Link to this definition")

The user’s screen name.

Type:

`str`

profile_image_url [](#twikit.user.User.profile_image_url "Link to this definition")

The URL of the user’s profile image (HTTPS version).

Type:

`str`

profile_banner_url [](#twikit.user.User.profile_banner_url "Link to this definition")

The URL of the user’s profile banner.

Type:

`str`

url [](#twikit.user.User.url "Link to this definition")

The user’s URL.

Type:

`str`

location [](#twikit.user.User.location "Link to this definition")

The user’s location information.

Type:

`str`

description [](#twikit.user.User.description "Link to this definition")

The user’s profile description.

Type:

`str`

description_urls [](#twikit.user.User.description_urls "Link to this definition")

URLs found in the user’s profile description.

Type:

`list`

urls [](#twikit.user.User.urls "Link to this definition")

URLs associated with the user.

Type:

`list`

pinned_tweet_ids [](#twikit.user.User.pinned_tweet_ids "Link to this definition")

The IDs of tweets that the user has pinned to their profile.

Type:

`str`

is_blue_verified [](#twikit.user.User.is_blue_verified "Link to this definition")

Indicates if the user is verified with a blue checkmark.

Type:

`bool`

verified [](#twikit.user.User.verified "Link to this definition")

Indicates if the user is verified.

Type:

`bool`

possibly_sensitive [](#twikit.user.User.possibly_sensitive "Link to this definition")

Indicates if the user’s content may be sensitive.

Type:

`bool`

can_dm [](#twikit.user.User.can_dm "Link to this definition")

Indicates whether the user can receive direct messages.

Type:

`bool`

can_media_tag [](#twikit.user.User.can_media_tag "Link to this definition")

Indicates whether the user can be tagged in media.

Type:

`bool`

want_retweets [](#twikit.user.User.want_retweets "Link to this definition")

Indicates if the user wants retweets.

Type:

`bool`

default_profile [](#twikit.user.User.default_profile "Link to this definition")

Indicates if the user has the default profile.

Type:

`bool`

default_profile_image [](#twikit.user.User.default_profile_image "Link to this definition")

Indicates if the user has the default profile image.

Type:

`bool`

has_custom_timelines [](#twikit.user.User.has_custom_timelines "Link to this definition")

Indicates if the user has custom timelines.

Type:

`bool`

followers_count [](#twikit.user.User.followers_count "Link to this definition")

The count of followers.

Type:

`int`

fast_followers_count [](#twikit.user.User.fast_followers_count "Link to this definition")

The count of fast followers.

Type:

`int`

normal_followers_count [](#twikit.user.User.normal_followers_count "Link to this definition")

The count of normal followers.

Type:

`int`

following_count [](#twikit.user.User.following_count "Link to this definition")

The count of users the user is following.

Type:

`int`

favourites_count [](#twikit.user.User.favourites_count "Link to this definition")

The count of favorites or likes.

Type:

`int`

listed_count [](#twikit.user.User.listed_count "Link to this definition")

The count of lists the user is a member of.

Type:

`int`

media_count [](#twikit.user.User.media_count "Link to this definition")

The count of media items associated with the user.

Type:

`int`

statuses_count [](#twikit.user.User.statuses_count "Link to this definition")

The count of tweets.

Type:

`int`

is_translator [](#twikit.user.User.is_translator "Link to this definition")

Indicates if the user is a translator.

Type:

`bool`

translator_type [](#twikit.user.User.translator_type "Link to this definition")

The type of translator.

Type:

`str`

profile_interstitial_type [](#twikit.user.User.profile_interstitial_type "Link to this definition")

The type of profile interstitial.

Type:

`str`

withheld_in_countries [](#twikit.user.User.withheld_in_countries "Link to this definition")

Countries where the user’s content is withheld.

Type:

list\[ `str`\]

_property_ created_at_datetime _:datetime_ [](#twikit.user.User.created_at_datetime "Link to this definition")_async_ get_tweets( _tweet_type:Literal\['Tweets','Replies','Media','Likes'\]_, _count:int=40_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/user.html#User.get_tweets) [](#twikit.user.User.get_tweets "Link to this definition")

Retrieves the user’s tweets.

Parameters:

- **tweet_type** ( _{'Tweets'_ _,_ _'Replies'_ _,_ _'Media'_ _,_ _'Likes'}_) – The type of tweets to retrieve.

- **count** ( `int`, default=40) – The number of tweets to retrieve.

Returns:

A Result object containing a list of Tweet objects.

Return type:

Result\[ `Tweet`\]

Examples

```
>>> user = await client.get_user_by_screen_name('example_user')
>>> tweets = await user.get_tweets('Tweets', count=20)
>>> for tweet in tweets:
...    print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

```
>>> more_tweets = await tweets.next()  # Retrieve more tweets
>>> for tweet in more_tweets:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

_async_ follow()→Response [\[source\]](_modules/twikit/user.html#User.follow) [](#twikit.user.User.follow "Link to this definition")

Follows the user.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

See also

`Client.follow_user`

_async_ unfollow()→Response [\[source\]](_modules/twikit/user.html#User.unfollow) [](#twikit.user.User.unfollow "Link to this definition")

Unfollows the user.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

See also

`Client.unfollow_user`

_async_ block()→Response [\[source\]](_modules/twikit/user.html#User.block) [](#twikit.user.User.block "Link to this definition")

Blocks a user.

Parameters:

**user_id** ( `str`) – The ID of the user to block.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

See also

[`unblock`](#twikit.user.User.unblock "twikit.user.User.unblock")

_async_ unblock()→Response [\[source\]](_modules/twikit/user.html#User.unblock) [](#twikit.user.User.unblock "Link to this definition")

Unblocks a user.

Parameters:

**user_id** ( `str`) – The ID of the user to unblock.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

See also

[`block`](#twikit.user.User.block "twikit.user.User.block")

_async_ mute()→Response [\[source\]](_modules/twikit/user.html#User.mute) [](#twikit.user.User.mute "Link to this definition")

Mutes a user.

Parameters:

**user_id** ( `str`) – The ID of the user to mute.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

See also

[`unmute`](#twikit.user.User.unmute "twikit.user.User.unmute")

_async_ unmute()→Response [\[source\]](_modules/twikit/user.html#User.unmute) [](#twikit.user.User.unmute "Link to this definition")

Unmutes a user.

Parameters:

**user_id** ( `str`) – The ID of the user to unmute.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

See also

[`mute`](#twikit.user.User.mute "twikit.user.User.mute")

_async_ get_followers( _count:int=20_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/user.html#User.get_followers) [](#twikit.user.User.get_followers "Link to this definition")

Retrieves a list of followers for the user.

Parameters:

**count** ( `int`, default=20) – The number of followers to retrieve.

Returns:

A list of User objects representing the followers.

Return type:

Result\[ [`User`](#twikit.user.User "twikit.user.User")\]

See also

`Client.get_user_followers`

_async_ get_verified_followers( _count:int=20_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/user.html#User.get_verified_followers) [](#twikit.user.User.get_verified_followers "Link to this definition")

Retrieves a list of verified followers for the user.

Parameters:

**count** ( `int`, default=20) – The number of verified followers to retrieve.

Returns:

A list of User objects representing the verified followers.

Return type:

Result\[ [`User`](#twikit.user.User "twikit.user.User")\]

See also

`Client.get_user_verified_followers`

_async_ get_followers_you_know( _count:int=20_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/user.html#User.get_followers_you_know) [](#twikit.user.User.get_followers_you_know "Link to this definition")

Retrieves a list of followers whom the user might know.

Parameters:

**count** ( `int`, default=20) – The number of followers you might know to retrieve.

Returns:

A list of User objects representing the followers you might know.

Return type:

Result\[ [`User`](#twikit.user.User "twikit.user.User")\]

See also

`Client.get_user_followers_you_know`

_async_ get_following( _count:int=20_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/user.html#User.get_following) [](#twikit.user.User.get_following "Link to this definition")

Retrieves a list of users whom the user is following.

Parameters:

**count** ( `int`, default=20) – The number of following users to retrieve.

Returns:

A list of User objects representing the users being followed.

Return type:

Result\[ [`User`](#twikit.user.User "twikit.user.User")\]

See also

`Client.get_user_following`

_async_ get_subscriptions( _count:int=20_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/user.html#User.get_subscriptions) [](#twikit.user.User.get_subscriptions "Link to this definition")

Retrieves a list of users whom the user is subscribed to.

Parameters:

**count** ( `int`, default=20) – The number of subscriptions to retrieve.

Returns:

A list of User objects representing the subscribed users.

Return type:

Result\[ [`User`](#twikit.user.User "twikit.user.User")\]

See also

`Client.get_user_subscriptions`

_async_ get_latest_followers( _count:int\|None=None_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/user.html#User.get_latest_followers) [](#twikit.user.User.get_latest_followers "Link to this definition")

Retrieves the latest followers.
Max count : 200

_async_ get_latest_friends( _count:int\|None=None_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/user.html#User.get_latest_friends) [](#twikit.user.User.get_latest_friends "Link to this definition")

Retrieves the latest friends (following users).
Max count : 200

_async_ send_dm( _text:str_, _media_id:str=None_, _reply_to=None_)→[Message](#twikit.message.Message "twikit.message.Message") [\[source\]](_modules/twikit/user.html#User.send_dm) [](#twikit.user.User.send_dm "Link to this definition")

Send a direct message to the user.

Parameters:

- **text** ( `str`) – The text content of the direct message.

- **media_id** ( `str`, default=None) – The media ID associated with any media content
  to be included in the message.
  Media ID can be received by using the `upload_media()` method.

- **reply_to** ( `str`, default=None) – Message ID to reply to.

Returns:

Message object containing information about the message sent.

Return type:

`Message`

Examples

```
>>> # send DM with media
>>> media_id = await client.upload_media('image.png')
>>> message = await user.send_dm('text', media_id)
>>> print(message)
<Message id="...">

```

See also

`Client.upload_media`, `Client.send_dm`

_async_ get_dm_history( _max_id:str=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Message](#twikit.message.Message "twikit.message.Message")\] [\[source\]](_modules/twikit/user.html#User.get_dm_history) [](#twikit.user.User.get_dm_history "Link to this definition")

Retrieves the DM conversation history with the user.

Parameters:

**max_id** ( `str`, default=None) – If specified, retrieves messages older than the specified max_id.

Returns:

A Result object containing a list of Message objects representing
the DM conversation history.

Return type:

Result\[ `Message`\]

Examples

```
>>> messages = await user.get_dm_history()
>>> for message in messages:
>>>     print(message)
<Message id="...">
<Message id="...">
...
...

```

```
>>> more_messages = await messages.next()  # Retrieve more messages
>>> for message in more_messages:
>>>     print(message)
<Message id="...">
<Message id="...">
...
...

```

_async_ get_highlights_tweets( _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/user.html#User.get_highlights_tweets) [](#twikit.user.User.get_highlights_tweets "Link to this definition")

Retrieves highlighted tweets from the user’s timeline.

Parameters:

**count** ( `int`, default=20) – The number of tweets to retrieve.

Returns:

An instance of the Result class containing the highlighted tweets.

Return type:

Result\[ `Tweet`\]

Examples

```
>>> result = await user.get_highlights_tweets()
>>> for tweet in result:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

```
>>> more_results = await result.next()  # Retrieve more highlighted tweets
>>> for tweet in more_results:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

_async_ update()→None [\[source\]](_modules/twikit/user.html#User.update) [](#twikit.user.User.update "Link to this definition")

## Message [](#module-twikit.message "Link to this heading")

_class_ twikit.message.Message( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _data:dict_, _sender_id:str_, _recipient_id:str_) [\[source\]](_modules/twikit/message.html#Message) [](#twikit.message.Message "Link to this definition")

Represents a direct message.

id [](#twikit.message.Message.id "Link to this definition")

The ID of the message.

Type:

`str`

time [](#twikit.message.Message.time "Link to this definition")

The timestamp of the message.

Type:

`str`

text [](#twikit.message.Message.text "Link to this definition")

The text content of the message.

Type:

`str`

attachment [](#twikit.message.Message.attachment "Link to this definition")

Attachment Information.

Type:

`dict`

_async_ reply( _text:str_, _media_id:str\|None=None_)→[Message](#twikit.message.Message "twikit.message.Message") [\[source\]](_modules/twikit/message.html#Message.reply) [](#twikit.message.Message.reply "Link to this definition")

Replies to the message.

Parameters:

- **text** ( `str`) – The text content of the direct message.

- **media_id** ( `str`, default=None) – The media ID associated with any media content
  to be included in the message.
  Media ID can be received by using the `upload_media()` method.

Returns:

Message object containing information about the message sent.

Return type:

[`Message`](#twikit.message.Message "twikit.message.Message")

See also

`Client.send_dm`

_async_ add_reaction( _emoji:str_)→Response [\[source\]](_modules/twikit/message.html#Message.add_reaction) [](#twikit.message.Message.add_reaction "Link to this definition")

Adds a reaction to the message.

Parameters:

**emoji** ( `str`) – The emoji to be added as a reaction.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

_async_ remove_reaction( _emoji:str_)→Response [\[source\]](_modules/twikit/message.html#Message.remove_reaction) [](#twikit.message.Message.remove_reaction "Link to this definition")

Removes a reaction from the message.

Parameters:

**emoji** ( `str`) – The emoji to be removed.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

_async_ delete()→Response [\[source\]](_modules/twikit/message.html#Message.delete) [](#twikit.message.Message.delete "Link to this definition")

Deletes the message.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

See also

`Client.delete_dm`

## Streaming [](#streaming "Link to this heading")

With the streaming API, you can receive real-time events such as tweet engagements,
DM updates, and DM typings. The basic procedure involves looping through the
stream session obtained with [`Client.get_streaming_session`](#twikit.client.client.Client.get_streaming_session "twikit.client.client.Client.get_streaming_session") and, if necessary,
updating the topics to be streamed using [`StreamingSession.update_subscriptions`](#twikit.streaming.StreamingSession.update_subscriptions "twikit.streaming.StreamingSession.update_subscriptions").

Example Code:

```
from twikit.streaming import Topic

topics = {
    Topic.tweet_engagement('1739617652'), # Stream tweet engagement
    Topic.dm_update('17544932482-174455537996'), # Stream DM update
    Topic.dm_typing('17544932482-174455537996') # Stream DM typing
}
session = client.get_streaming_session(topics)

for topic, payload in session:
    if payload.dm_update:
        conversation_id = payload.dm_update.conversation_id
        user_id = payload.dm_update.user_id
        print(f'{conversation_id}: {user_id} sent a message')

    if payload.dm_typing:
        conversation_id = payload.dm_typing.conversation_id
        user_id = payload.dm_typing.user_id
        print(f'{conversation_id}: {user_id} is typing')

    if payload.tweet_engagement:
        like = payload.tweet_engagement.like_count
        retweet = payload.tweet_engagement.retweet_count
        view = payload.tweet_engagement.view_count
        print(f'Tweet engagement updated likes: {like} retweets: {retweet} views: {view}')

```

_class_ twikit.streaming.StreamingSession( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _session_id:str_, _stream:AsyncGenerator\[ [Payload](#twikit.streaming.Payload "twikit.streaming.Payload")\]_, _topics:set\[str\]_, _auto_reconnect:bool_) [\[source\]](_modules/twikit/streaming.html#StreamingSession) [](#twikit.streaming.StreamingSession "Link to this definition")

Represents a streaming session.

id [](#twikit.streaming.StreamingSession.id "Link to this definition")

The ID or the session.

Type:

`str`

topics [](#twikit.streaming.StreamingSession.topics "Link to this definition")

The topics to stream.

Type:

set\[ `str`\]

See also

[`Client.get_streaming_session`](#twikit.client.client.Client.get_streaming_session "twikit.client.client.Client.get_streaming_session")

_async_ reconnect()→tuple\[str, [Payload](#twikit.streaming.Payload "twikit.streaming.Payload")\] [\[source\]](_modules/twikit/streaming.html#StreamingSession.reconnect) [](#twikit.streaming.StreamingSession.reconnect "Link to this definition")

Reconnects the session.

_async_ update_subscriptions( _subscribe:set\[str\]\|None=None_, _unsubscribe:set\[str\]\|None=None_)→[Payload](#twikit.streaming.Payload "twikit.streaming.Payload") [\[source\]](_modules/twikit/streaming.html#StreamingSession.update_subscriptions) [](#twikit.streaming.StreamingSession.update_subscriptions "Link to this definition")

Updates subscriptions for the session.

Parameters:

- **subscribe** (set\[ `str`\], default=None) – Topics to subscribe to.

- **unsubscribe** (set\[ `str`\], default=None) – Topics to unsubscribe from.

Examples

```
>>> from twikit.streaming import Topic
...
>>> subscribe_topics = {
...     Topic.tweet_engagement('1749528513'),
...     Topic.tweet_engagement('1765829534')
... }
>>> unsubscribe_topics = {
...     Topic.tweet_engagement('17396176529'),
...     Topic.dm_update('17544932482-174455537996'),
...     Topic.dm_typing('17544932482-174455537996)'
... }
>>> await session.update_subscriptions(
...     subscribe_topics, unsubscribe_topics
... )

```

Note

dm_update and dm_update cannot be added.

See also

[`Topic`](#twikit.streaming.Topic "twikit.streaming.Topic")

_class_ twikit.streaming.Payload( _config:[ConfigEvent](#twikit.streaming.ConfigEvent "twikit.streaming.ConfigEvent") \|None=None_, _subscriptions:[SubscriptionsEvent](#twikit.streaming.SubscriptionsEvent "twikit.streaming.SubscriptionsEvent") \|None=None_, _tweet_engagement:[TweetEngagementEvent](#twikit.streaming.TweetEngagementEvent "twikit.streaming.TweetEngagementEvent") \|None=None_, _dm_update:[DMUpdateEvent](#twikit.streaming.DMUpdateEvent "twikit.streaming.DMUpdateEvent") \|None=None_, _dm_typing:[DMTypingEvent](#twikit.streaming.DMTypingEvent "twikit.streaming.DMTypingEvent") \|None=None_) [\[source\]](_modules/twikit/streaming.html#Payload) [](#twikit.streaming.Payload "Link to this definition")

Represents a payload containing several types of events.

config _: [ConfigEvent](#twikit.streaming.ConfigEvent "twikit.streaming.ConfigEvent") \|None_ [](#twikit.streaming.Payload.config "Link to this definition")

The configuration event.

subscriptions _: [SubscriptionsEvent](#twikit.streaming.SubscriptionsEvent "twikit.streaming.SubscriptionsEvent") \|None_ [](#twikit.streaming.Payload.subscriptions "Link to this definition")

The subscriptions event.

tweet_engagement _: [TweetEngagementEvent](#twikit.streaming.TweetEngagementEvent "twikit.streaming.TweetEngagementEvent") \|None_ [](#twikit.streaming.Payload.tweet_engagement "Link to this definition")

The tweet engagement event.

dm_update _: [DMUpdateEvent](#twikit.streaming.DMUpdateEvent "twikit.streaming.DMUpdateEvent") \|None_ [](#twikit.streaming.Payload.dm_update "Link to this definition")

The direct message update event.

dm_typing _: [DMTypingEvent](#twikit.streaming.DMTypingEvent "twikit.streaming.DMTypingEvent") \|None_ [](#twikit.streaming.Payload.dm_typing "Link to this definition")

The direct message typing event.

_class_ twikit.streaming.ConfigEvent( _session_id:str_, _subscription_ttl_millis:int_, _heartbeat_millis:int_) [\[source\]](_modules/twikit/streaming.html#ConfigEvent) [](#twikit.streaming.ConfigEvent "Link to this definition")

Event representing configuration data.

session_id _:str_ [](#twikit.streaming.ConfigEvent.session_id "Link to this definition")

The session ID associated with the configuration.

subscription_ttl_millis _:int_ [](#twikit.streaming.ConfigEvent.subscription_ttl_millis "Link to this definition")

The time to live for the subscription.

heartbeat_millis _:int_ [](#twikit.streaming.ConfigEvent.heartbeat_millis "Link to this definition")

The heartbeat interval in milliseconds.

_class_ twikit.streaming.SubscriptionsEvent( _errors:list_) [\[source\]](_modules/twikit/streaming.html#SubscriptionsEvent) [](#twikit.streaming.SubscriptionsEvent "Link to this definition")

Event representing subscription status.

errors _:list_ [](#twikit.streaming.SubscriptionsEvent.errors "Link to this definition")

A list of errors.

_class_ twikit.streaming.TweetEngagementEvent( _like_count:str\|None_, _retweet_count:str\|None_, _view_count:str\|None_, _view_count_state:str\|None_, _quote_count:int\|None_, _reply_count:int\|None_) [\[source\]](_modules/twikit/streaming.html#TweetEngagementEvent) [](#twikit.streaming.TweetEngagementEvent "Link to this definition")

Event representing tweet engagement metrics.

like_count _:str\|None_ [](#twikit.streaming.TweetEngagementEvent.like_count "Link to this definition")

The number of likes on the tweet.

retweet_count _:str\|None_ [](#twikit.streaming.TweetEngagementEvent.retweet_count "Link to this definition")

The number of retweets of the tweet.

view_count _:str\|None_ [](#twikit.streaming.TweetEngagementEvent.view_count "Link to this definition")

The number of views of the tweet.

view_count_state _:str\|None_ [](#twikit.streaming.TweetEngagementEvent.view_count_state "Link to this definition")

The state of view count.

quote_count _:int\|None_ [](#twikit.streaming.TweetEngagementEvent.quote_count "Link to this definition")

The number of quotes of the tweet.

reply_count _:int\|None_ [](#twikit.streaming.TweetEngagementEvent.reply_count "Link to this definition")

Alias for field number 5

_class_ twikit.streaming.DMUpdateEvent( _conversation_id:str_, _user_id:str_) [\[source\]](_modules/twikit/streaming.html#DMUpdateEvent) [](#twikit.streaming.DMUpdateEvent "Link to this definition")

Event representing a (DM) update.

conversation_id _:str_ [](#twikit.streaming.DMUpdateEvent.conversation_id "Link to this definition")

The ID of the conversation associated with the DM.

user_id _:str_ [](#twikit.streaming.DMUpdateEvent.user_id "Link to this definition")

ID of the user who sent the DM.

_class_ twikit.streaming.DMTypingEvent( _conversation_id:str_, _user_id:str_) [\[source\]](_modules/twikit/streaming.html#DMTypingEvent) [](#twikit.streaming.DMTypingEvent "Link to this definition")

Event representing typing indication in a DM conversation.

conversation_id _:str_ [](#twikit.streaming.DMTypingEvent.conversation_id "Link to this definition")

The conversation where typing indication occurred.

user_id _:str_ [](#twikit.streaming.DMTypingEvent.user_id "Link to this definition")

The ID of the typing user.

_class_ twikit.streaming.Topic [\[source\]](_modules/twikit/streaming.html#Topic) [](#twikit.streaming.Topic "Link to this definition")

Utility class for generating topic strings for streaming.

_static_ tweet_engagement( _tweet_id:str_)→str [\[source\]](_modules/twikit/streaming.html#Topic.tweet_engagement) [](#twikit.streaming.Topic.tweet_engagement "Link to this definition")

Generates a topic string for tweet engagement events.

Parameters:

**tweet_id** ( `str`) – The ID of the tweet.

Returns:

The topic string for tweet engagement events.

Return type:

`str`

_static_ dm_update( _conversation_id:str_)→str [\[source\]](_modules/twikit/streaming.html#Topic.dm_update) [](#twikit.streaming.Topic.dm_update "Link to this definition")

Generates a topic string for direct message update events.

Parameters:

**conversation_id** ( `str`) – The ID of the conversation.
Group ID (00000000) or partner_ID-your_ID (00000000-00000001)

Returns:

The topic string for direct message update events.

Return type:

`str`

_static_ dm_typing( _conversation_id:str_)→str [\[source\]](_modules/twikit/streaming.html#Topic.dm_typing) [](#twikit.streaming.Topic.dm_typing "Link to this definition")

Generates a topic string for direct message typing events.

Parameters:

**conversation_id** ( `str`) – The ID of the conversation.
Group ID (00000000) or partner_ID-your_ID (00000000-00000001)

Returns:

The topic string for direct message typing events.

Return type:

`str`

## Trend [](#module-twikit.trend "Link to this heading")

_class_ twikit.trend.Trend( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _data:dict_) [\[source\]](_modules/twikit/trend.html#Trend) [](#twikit.trend.Trend "Link to this definition")name [](#twikit.trend.Trend.name "Link to this definition")

The name of the trending topic.

Type:

`str`

tweets_count [](#twikit.trend.Trend.tweets_count "Link to this definition")

The count of tweets associated with the trend.

Type:

`int`

domain_context [](#twikit.trend.Trend.domain_context "Link to this definition")

The context or domain associated with the trend.

Type:

`str`

grouped_trends [](#twikit.trend.Trend.grouped_trends "Link to this definition")

A list of trend names grouped under the main trend.

Type:

`` list`[:class:`str ``\]

_class_ twikit.trend.PlaceTrends [\[source\]](_modules/twikit/trend.html#PlaceTrends) [](#twikit.trend.PlaceTrends "Link to this definition")trends _:list\[ [PlaceTrend](#twikit.trend.PlaceTrend "twikit.trend.PlaceTrend")\]_ [](#twikit.trend.PlaceTrends.trends "Link to this definition")as_of _:str_ [](#twikit.trend.PlaceTrends.as_of "Link to this definition")created_at _:str_ [](#twikit.trend.PlaceTrends.created_at "Link to this definition")locations _:dict_ [](#twikit.trend.PlaceTrends.locations "Link to this definition")_class_ twikit.trend.PlaceTrend( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _data:dict_) [\[source\]](_modules/twikit/trend.html#PlaceTrend) [](#twikit.trend.PlaceTrend "Link to this definition")name [](#twikit.trend.PlaceTrend.name "Link to this definition")

The name of the trend.

Type:

`str`

url [](#twikit.trend.PlaceTrend.url "Link to this definition")

The URL to view the trend.

Type:

`str`

query [](#twikit.trend.PlaceTrend.query "Link to this definition")

The search query corresponding to the trend.

Type:

`str`

tweet_volume [](#twikit.trend.PlaceTrend.tweet_volume "Link to this definition")

The volume of tweets associated with the trend.

Type:

`int`

_class_ twikit.trend.Location( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _data:dict_) [\[source\]](_modules/twikit/trend.html#Location) [](#twikit.trend.Location "Link to this definition")_async_ get_trends()→[PlaceTrends](#twikit.trend.PlaceTrends "twikit.trend.PlaceTrends") [\[source\]](_modules/twikit/trend.html#Location.get_trends) [](#twikit.trend.Location.get_trends "Link to this definition")

## List [](#list "Link to this heading")

_class_ twikit.list.List( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _data:dict_) [\[source\]](_modules/twikit/list.html#List) [](#twikit.list.List "Link to this definition")

Class representing a Twitter List.

id [](#twikit.list.List.id "Link to this definition")

The unique identifier of the List.

Type:

`str`

created_at [](#twikit.list.List.created_at "Link to this definition")

The timestamp when the List was created.

Type:

`int`

default_banner [](#twikit.list.List.default_banner "Link to this definition")

Information about the default banner of the List.

Type:

`dict`

banner [](#twikit.list.List.banner "Link to this definition")

Information about the banner of the List. If custom banner is not set,
it defaults to the default banner.

Type:

`dict`

description [](#twikit.list.List.description "Link to this definition")

The description of the List.

Type:

`str`

following [](#twikit.list.List.following "Link to this definition")

Indicates if the authenticated user is following the List.

Type:

`bool`

is_member [](#twikit.list.List.is_member "Link to this definition")

Indicates if the authenticated user is a member of the List.

Type:

`bool`

member_count [](#twikit.list.List.member_count "Link to this definition")

The number of members in the List.

Type:

`int`

mode [](#twikit.list.List.mode "Link to this definition")

The mode of the List, either ‘Private’ or ‘Public’.

Type:

{‘Private’, ‘Public’}

muting [](#twikit.list.List.muting "Link to this definition")

Indicates if the authenticated user is muting the List.

Type:

`bool`

name [](#twikit.list.List.name "Link to this definition")

The name of the List.

Type:

`str`

pinning [](#twikit.list.List.pinning "Link to this definition")

Indicates if the List is pinned.

Type:

`bool`

subscriber_count [](#twikit.list.List.subscriber_count "Link to this definition")

The number of subscribers to the List.

Type:

`int`

_property_ created_at_datetime _:datetime_ [](#twikit.list.List.created_at_datetime "Link to this definition")_async_ edit_banner( _media_id:str_)→Response [\[source\]](_modules/twikit/list.html#List.edit_banner) [](#twikit.list.List.edit_banner "Link to this definition")

Edit the banner image of the list.

Parameters:

**media_id** ( `str`) – The ID of the media to use as the new banner image.

Returns:

Response returned from twitter api.

Return type:

`httpx.Response`

Examples

```
>>> media_id = await client.upload_media('image.png')
>>> await media.edit_banner(media_id)

```

_async_ delete_banner()→Response [\[source\]](_modules/twikit/list.html#List.delete_banner) [](#twikit.list.List.delete_banner "Link to this definition")

Deletes the list banner.

_async_ edit( _name:str\|None=None_, _description:str\|None=None_, _is_private:bool\|None=None_)→[List](#twikit.list.List "twikit.list.List") [\[source\]](_modules/twikit/list.html#List.edit) [](#twikit.list.List.edit "Link to this definition")

Edits list information.

Parameters:

- **name** ( `str`, default=None) – The new name for the list.

- **description** ( `str`, default=None) – The new description for the list.

- **is_private** ( `bool`, default=None) – Indicates whether the list should be private
  (True) or public (False).

Returns:

The updated Twitter list.

Return type:

[`List`](#twikit.list.List "twikit.list.List")

Examples

```
>>> await list.edit(
...     'new name', 'new description', True
... )

```

_async_ add_member( _user_id:str_)→Response [\[source\]](_modules/twikit/list.html#List.add_member) [](#twikit.list.List.add_member "Link to this definition")

Adds a member to the list.

_async_ remove_member( _user_id:str_)→Response [\[source\]](_modules/twikit/list.html#List.remove_member) [](#twikit.list.List.remove_member "Link to this definition")

Removes a member from the list.

_async_ get_tweets( _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/list.html#List.get_tweets) [](#twikit.list.List.get_tweets "Link to this definition")

Retrieves tweets from the list.

Parameters:

- **count** ( `int`, default=20) – The number of tweets to retrieve.

- **cursor** ( `str`, default=None) – The cursor for pagination.

Returns:

A Result object containing the retrieved tweets.

Return type:

Result\[ `Tweet`\]

Examples

```
>>> tweets = await list.get_tweets()
>>> for tweet in tweets:
...    print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

```
>>> more_tweets = await tweets.next()  # Retrieve more tweets
>>> for tweet in more_tweets:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
...

```

_async_ get_members( _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/list.html#List.get_members) [](#twikit.list.List.get_members "Link to this definition")

Retrieves members of the list.

Parameters:

**count** ( `int`, default=20) – Number of members to retrieve.

Returns:

Members of the list

Return type:

Result\[ `User`\]

Examples

```
>>> members = list_.get_members()
>>> for member in members:
...     print(member)
<User id="...">
<User id="...">
...
...
>>> more_members = members.next()  # Retrieve more members

```

_async_ get_subscribers( _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [User](#twikit.user.User "twikit.user.User")\] [\[source\]](_modules/twikit/list.html#List.get_subscribers) [](#twikit.list.List.get_subscribers "Link to this definition")

Retrieves subscribers of the list.

Parameters:

**count** ( `int`, default=20) – Number of subscribers to retrieve.

Returns:

Subscribers of the list

Return type:

Result\[ `User`\]

Examples

```
>>> subscribers = list_.get_subscribers()
>>> for subscriber in subscribers:
...     print(subscriber)
<User id="...">
<User id="...">
...
...
>>> more_subscribers = subscribers.next()  # Retrieve more subscribers

```

_async_ update()→None [\[source\]](_modules/twikit/list.html#List.update) [](#twikit.list.List.update "Link to this definition")

## Community [](#module-twikit.community "Link to this heading")

_class_ twikit.community.CommunityCreator( _id_, _screen_name_, _verified_) [\[source\]](_modules/twikit/community.html#CommunityCreator) [](#twikit.community.CommunityCreator "Link to this definition")id _:str_ [](#twikit.community.CommunityCreator.id "Link to this definition")

Alias for field number 0

screen_name _:str_ [](#twikit.community.CommunityCreator.screen_name "Link to this definition")

Alias for field number 1

verified _:bool_ [](#twikit.community.CommunityCreator.verified "Link to this definition")

Alias for field number 2

_class_ twikit.community.CommunityRule( _id_, _name_) [\[source\]](_modules/twikit/community.html#CommunityRule) [](#twikit.community.CommunityRule "Link to this definition")id _:str_ [](#twikit.community.CommunityRule.id "Link to this definition")

Alias for field number 0

name _:str_ [](#twikit.community.CommunityRule.name "Link to this definition")

Alias for field number 1

_class_ twikit.community.CommunityMember( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _data:dict_) [\[source\]](_modules/twikit/community.html#CommunityMember) [](#twikit.community.CommunityMember "Link to this definition")_class_ twikit.community.Community( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _data:dict_) [\[source\]](_modules/twikit/community.html#Community) [](#twikit.community.Community "Link to this definition")id [](#twikit.community.Community.id "Link to this definition")

The ID of the community.

Type:

`str`

name [](#twikit.community.Community.name "Link to this definition")

The name of the community.

Type:

`str`

member_count [](#twikit.community.Community.member_count "Link to this definition")

The count of members in the community.

Type:

`int`

is_nsfw [](#twikit.community.Community.is_nsfw "Link to this definition")

Indicates if the community is NSFW.

Type:

`bool`

members_facepile_results [](#twikit.community.Community.members_facepile_results "Link to this definition")

The profile image URLs of members.

Type:

list\[ `str`\]

banner [](#twikit.community.Community.banner "Link to this definition")

The banner information of the community.

Type:

`dict`

is_member [](#twikit.community.Community.is_member "Link to this definition")

Indicates if the user is a member of the community.

Type:

`bool`

role [](#twikit.community.Community.role "Link to this definition")

The role of the user in the community.

Type:

`str`

description [](#twikit.community.Community.description "Link to this definition")

The description of the community.

Type:

`str`

creator [](#twikit.community.Community.creator "Link to this definition")

The creator of the community.

Type:

`User` \| [`CommunityCreator`](#twikit.community.CommunityCreator "twikit.community.CommunityCreator")

admin [](#twikit.community.Community.admin "Link to this definition")

The admin of the community.

Type:

`User`

join_policy [](#twikit.community.Community.join_policy "Link to this definition")

The join policy of the community.

Type:

`str`

created_at [](#twikit.community.Community.created_at "Link to this definition")

The timestamp of the community’s creation.

Type:

`int`

invites_policy [](#twikit.community.Community.invites_policy "Link to this definition")

The invites policy of the community.

Type:

`str`

is_pinned [](#twikit.community.Community.is_pinned "Link to this definition")

Indicates if the community is pinned.

Type:

`bool`

rules [](#twikit.community.Community.rules "Link to this definition")

The rules of the community.

Type:

list\[ [`CommunityRule`](#twikit.community.CommunityRule "twikit.community.CommunityRule")\]

_async_ get_tweets( _tweet_type:Literal\['Top','Latest','Media'\]_, _count:int=40_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/community.html#Community.get_tweets) [](#twikit.community.Community.get_tweets "Link to this definition")

Retrieves tweets from the community.

Parameters:

- **tweet_type** ( _{'Top'_ _,_ _'Latest'_ _,_ _'Media'}_) – The type of tweets to retrieve.

- **count** ( `int`, default=40) – The number of tweets to retrieve.

Returns:

List of retrieved tweets.

Return type:

Result\[ `Tweet`\]

Examples

```
>>> tweets = await community.get_tweets('Latest')
>>> for tweet in tweets:
...     print(tweet)
<Tweet id="...">
<Tweet id="...">
...
>>> more_tweets = await tweets.next()  # Retrieve more tweets

```

_async_ join()→[Community](#twikit.community.Community "twikit.community.Community") [\[source\]](_modules/twikit/community.html#Community.join) [](#twikit.community.Community.join "Link to this definition")

Join the community.

_async_ leave()→[Community](#twikit.community.Community "twikit.community.Community") [\[source\]](_modules/twikit/community.html#Community.leave) [](#twikit.community.Community.leave "Link to this definition")

Leave the community.

_async_ request_to_join( _answer:str\|None=None_)→[Community](#twikit.community.Community "twikit.community.Community") [\[source\]](_modules/twikit/community.html#Community.request_to_join) [](#twikit.community.Community.request_to_join "Link to this definition")

Request to join the community.

_async_ get_members( _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [CommunityMember](#twikit.community.CommunityMember "twikit.community.CommunityMember")\] [\[source\]](_modules/twikit/community.html#Community.get_members) [](#twikit.community.Community.get_members "Link to this definition")

Retrieves members of the community.

Parameters:

**count** ( `int`, default=20) – The number of members to retrieve.

Returns:

List of retrieved members.

Return type:

Result\[ [`CommunityMember`](#twikit.community.CommunityMember "twikit.community.CommunityMember")\]

_async_ get_moderators( _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [CommunityMember](#twikit.community.CommunityMember "twikit.community.CommunityMember")\] [\[source\]](_modules/twikit/community.html#Community.get_moderators) [](#twikit.community.Community.get_moderators "Link to this definition")

Retrieves moderators of the community.

Parameters:

**count** ( `int`, default=20) – The number of moderators to retrieve.

Returns:

List of retrieved moderators.

Return type:

Result\[ [`CommunityMember`](#twikit.community.CommunityMember "twikit.community.CommunityMember")\]

_async_ search_tweet( _query:str_, _count:int=20_, _cursor:str\|None=None_)→[Result](#twikit.utils.Result "twikit.utils.Result")\[ [Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")\] [\[source\]](_modules/twikit/community.html#Community.search_tweet) [](#twikit.community.Community.search_tweet "Link to this definition")

Searchs tweets in the community.

Parameters:

- **query** ( `str`) – The search query.

- **count** ( `int`, default=20) – The number of tweets to retrieve.

Returns:

List of retrieved tweets.

Return type:

Result\[ `Tweet`\]

_async_ update()→None [\[source\]](_modules/twikit/community.html#Community.update) [](#twikit.community.Community.update "Link to this definition")

## Notification [](#notification "Link to this heading")

_class_ twikit.notification.Notification( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _data:dict_, _tweet:[Tweet](#twikit.tweet.Tweet "twikit.tweet.Tweet")_, _from_user:[User](#twikit.user.User "twikit.user.User")_) [\[source\]](_modules/twikit/notification.html#Notification) [](#twikit.notification.Notification "Link to this definition")id [](#twikit.notification.Notification.id "Link to this definition")

The unique identifier of the notification.

Type:

`str`

timestamp_ms [](#twikit.notification.Notification.timestamp_ms "Link to this definition")

The timestamp of the notification in milliseconds.

Type:

`int`

icon [](#twikit.notification.Notification.icon "Link to this definition")

Dictionary containing icon data for the notification.

Type:

`dict`

message [](#twikit.notification.Notification.message "Link to this definition")

The message text of the notification.

Type:

`str`

tweet [](#twikit.notification.Notification.tweet "Link to this definition")

The tweet associated with the notification.

Type:

[`Tweet`](#twikit.tweet.Tweet "twikit.tweet.Tweet")

from_user [](#twikit.notification.Notification.from_user "Link to this definition")

The user who triggered the notification.

Type:

[`User`](#twikit.user.User "twikit.user.User")

## Geo [](#geo "Link to this heading")

_class_ twikit.geo.Place( _client:[Client](#twikit.client.client.Client "twikit.client.client.Client")_, _data:dict_) [\[source\]](_modules/twikit/geo.html#Place) [](#twikit.geo.Place "Link to this definition")id [](#twikit.geo.Place.id "Link to this definition")

The ID of the place.

Type:

`str`

name [](#twikit.geo.Place.name "Link to this definition")

The name of the place.

Type:

`str`

full_name [](#twikit.geo.Place.full_name "Link to this definition")

The full name of the place.

Type:

`str`

country [](#twikit.geo.Place.country "Link to this definition")

The country where the place is located.

Type:

`str`

country_code [](#twikit.geo.Place.country_code "Link to this definition")

The ISO 3166-1 alpha-2 country code of the place.

Type:

`str`

url [](#twikit.geo.Place.url "Link to this definition")

The URL providing more information about the place.

Type:

`str`

place_type [](#twikit.geo.Place.place_type "Link to this definition")

The type of place.

Type:

`str`

attributes [](#twikit.geo.Place.attributes "Link to this definition")Type:

`dict`

bounding_box [](#twikit.geo.Place.bounding_box "Link to this definition")

The bounding box that defines the geographical area of the place.

Type:

`dict`

centroid [](#twikit.geo.Place.centroid "Link to this definition")

The geographical center of the place, represented by latitude and
longitude.

Type:

list\[ `float`\] \| None

contained_within [](#twikit.geo.Place.contained_within "Link to this definition")

A list of places that contain this place.

Type:

list\[ [`Place`](#twikit.geo.Place "twikit.geo.Place")\]

_async_ update()→None [\[source\]](_modules/twikit/geo.html#Place.update) [](#twikit.geo.Place.update "Link to this definition")

## Capsolver [](#capsolver "Link to this heading")

_class_ twikit.\_captcha.capsolver.Capsolver( _api_key:str_, _max_attempts:int=3_, _get_result_interval:float=1.0_, _use_blob_data:bool=False_) [\[source\]](_modules/twikit/_captcha/capsolver.html#Capsolver) [](#twikit._captcha.capsolver.Capsolver "Link to this definition")

You can automatically unlock the account by passing the captcha_solver
argument when initialising the [`Client`](#twikit.client.client.Client "twikit.client.client.Client").

First, visit [https://capsolver.com](https://capsolver.com) and obtain your Capsolver API key.
Next, pass the Capsolver instance to the client as shown in the example.

```
from twikit.twikit_async import Capsolver, Client
solver = Capsolver(
    api_key='your_api_key',
    max_attempts=10
)
client = Client(captcha_solver=solver)

```

Parameters:

- **api_key** ( `str`) – Capsolver API key.

- **max_attempts** ( `int`, default=3) – The maximum number of attempts to solve the captcha.

- **get_result_interval** ( `float`, default=1.0)

- **use_blob_data** ( `bool`, default=False)

## Utils [](#utils "Link to this heading")

_class_ twikit.utils.Result( _results:list\[T\]_, _fetch_next_result:Awaitable\|None=None_, _next_cursor:str\|None=None_, _fetch_previous_result:Awaitable\|None=None_, _previous_cursor:str\|None=None_) [\[source\]](_modules/twikit/utils.html#Result) [](#twikit.utils.Result "Link to this definition")

This class is for storing multiple results.
The next method can be used to retrieve further results.
As with a regular list, you can access elements by
specifying indexes and iterate over elements using a for loop.

next_cursor [](#twikit.utils.Result.next_cursor "Link to this definition")

Cursor used to obtain the next result.

Type:

`str`

previous_cursor [](#twikit.utils.Result.previous_cursor "Link to this definition")

Cursor used to obtain the previous result.

Type:

`str`

token [](#twikit.utils.Result.token "Link to this definition")

Alias of next_cursor.

Type:

`str`

cursor [](#twikit.utils.Result.cursor "Link to this definition")

Alias of next_cursor.

Type:

`str`

_async_ next()→[Result](#twikit.utils.Result "twikit.utils.Result")\[T\] [\[source\]](_modules/twikit/utils.html#Result.next) [](#twikit.utils.Result.next "Link to this definition")

The next result.

_async_ previous()→[Result](#twikit.utils.Result "twikit.utils.Result")\[T\] [\[source\]](_modules/twikit/utils.html#Result.previous) [](#twikit.utils.Result.previous "Link to this definition")

The previous result.

_classmethod_ empty() [\[source\]](_modules/twikit/utils.html#Result.empty) [](#twikit.utils.Result.empty "Link to this definition")

## Errors [](#module-twikit.errors "Link to this heading")

_exception_ twikit.errors.TwitterException( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#TwitterException) [](#twikit.errors.TwitterException "Link to this definition")

Base class for Twitter API related exceptions.

_exception_ twikit.errors.BadRequest( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#BadRequest) [](#twikit.errors.BadRequest "Link to this definition")

Exception raised for 400 Bad Request errors.

_exception_ twikit.errors.Unauthorized( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#Unauthorized) [](#twikit.errors.Unauthorized "Link to this definition")

Exception raised for 401 Unauthorized errors.

_exception_ twikit.errors.Forbidden( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#Forbidden) [](#twikit.errors.Forbidden "Link to this definition")

Exception raised for 403 Forbidden errors.

_exception_ twikit.errors.NotFound( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#NotFound) [](#twikit.errors.NotFound "Link to this definition")

Exception raised for 404 Not Found errors.

_exception_ twikit.errors.RequestTimeout( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#RequestTimeout) [](#twikit.errors.RequestTimeout "Link to this definition")

Exception raised for 408 Request Timeout errors.

_exception_ twikit.errors.TooManyRequests( _\*args_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#TooManyRequests) [](#twikit.errors.TooManyRequests "Link to this definition")

Exception raised for 429 Too Many Requests errors.

_exception_ twikit.errors.ServerError( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#ServerError) [](#twikit.errors.ServerError "Link to this definition")

Exception raised for 5xx Server Error responses.

_exception_ twikit.errors.CouldNotTweet( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#CouldNotTweet) [](#twikit.errors.CouldNotTweet "Link to this definition")

Exception raised when a tweet could not be sent.

_exception_ twikit.errors.DuplicateTweet( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#DuplicateTweet) [](#twikit.errors.DuplicateTweet "Link to this definition")

Exception raised when a tweet is a duplicate of another.

_exception_ twikit.errors.TweetNotAvailable( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#TweetNotAvailable) [](#twikit.errors.TweetNotAvailable "Link to this definition")

Exceptions raised when a tweet is not available.

_exception_ twikit.errors.InvalidMedia( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#InvalidMedia) [](#twikit.errors.InvalidMedia "Link to this definition")

Exception raised when there is a problem with the media ID
sent with the tweet.

_exception_ twikit.errors.UserNotFound( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#UserNotFound) [](#twikit.errors.UserNotFound "Link to this definition")

Exception raised when a user does not exsit.

_exception_ twikit.errors.UserUnavailable( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#UserUnavailable) [](#twikit.errors.UserUnavailable "Link to this definition")

Exception raised when a user is unavailable.

_exception_ twikit.errors.AccountSuspended( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#AccountSuspended) [](#twikit.errors.AccountSuspended "Link to this definition")

Exception raised when the account is suspended.

_exception_ twikit.errors.AccountLocked( _\*args:object_, _headers:dict\|None=None_) [\[source\]](_modules/twikit/errors.html#AccountLocked) [](#twikit.errors.AccountLocked "Link to this definition")

Exception raised when the account is locked (very likey is Arkose challenge).

twikit.errors.raise_exceptions_from_response( _errors:list\[dict\]_) [\[source\]](_modules/twikit/errors.html#raise_exceptions_from_response) [](#twikit.errors.raise_exceptions_from_response "Link to this definition")
