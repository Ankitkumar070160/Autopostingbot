import tweepy
from googleapiclient.discovery import build
import facebook
from instabot import Bot
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Telegram API token (replace 'your_telegram_token' with your actual token)
telegram_token = 'your_telegram_token'

# Twitter API credentials
twitter_api_key = 'your_api_key'
twitter_api_secret = 'your_api_secret'
twitter_access_token = 'your_access_token'
twitter_access_secret = 'your_access_secret'

# YouTube API credentials
youtube_api_key = 'your_api_key'
youtube_channel_id = 'your_channel_id'

# Facebook API credentials
facebook_access_token = 'your_access_token'

# Instagram credentials
instagram_username = 'your_instagram_username'
instagram_password = 'your_instagram_password'

# TikTok credentials (unofficial)
tiktok_username = 'your_tiktok_username'
tiktok_password = 'your_tiktok_password'

# Twitch credentials
twitch_client_id = 'your_twitch_client_id'
twitch_client_secret = 'your_twitch_client_secret'
twitch_access_token = 'your_twitch_access_token'

# Dailymotion credentials
dailymotion_api_key = 'your_dailymotion_api_key'
dailymotion_username = 'your_dailymotion_username'
dailymotion_password = 'your_dailymotion_password'

# Uscreen credentials (example, may vary)
uscreen_api_key = 'your_uscreen_api_key'
uscreen_username = 'your_uscreen_username'
uscreen_password = 'your_uscreen_password'

# Muvi credentials (example, may vary)
muvi_api_key = 'your_muvi_api_key'
muvi_username = 'your_muvi_username'
muvi_password = 'your_muvi_password'

def add_credit(description):
    return f'{description}\n\nMr Tanit - Subscribe for more content!'

def post_to_twitter(video_path, tweet_text, video_title):
    auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
    auth.set_access_token(twitter_access_token, twitter_access_secret)
    api = tweepy.API(auth)

    media = api.media_upload(video_path)
    api.update_status(status=tweet_text, media_ids=[media.media_id])

def upload_to_youtube(video_path, video_title, video_description, video_tags):
    youtube = build('youtube', 'v3', developerKey=youtube_api_key)
    
    request = youtube.videos().insert(
        part="snippet,status",
        body={
          "snippet": {
            "categoryId": "22",
            "title": video_title,
            "description": add_credit(video_description),
            "tags": video_tags
          },
          "status": {
            "privacyStatus": "public"
          }
        },
        media_body=video_path
    )
    response = request.execute()
    print(f'Video uploaded to YouTube with ID: {response["id"]}')

def post_to_facebook(video_path, message, video_title):
    graph = facebook.GraphAPI(access_token=facebook_access_token, version="3.0")
    with open(video_path, "rb") as video_file:
        graph.put_video(file=video_file, title=video_title, description=add_credit(message))

def post_to_instagram(video_path, caption, tags):
    bot = Bot()
    bot.login(username=instagram_username, password=instagram_password)
    bot.upload_video(video_path, caption=add_credit(f"{caption}\n{tags}"))

def post_to_tiktok(video_path, caption):
    # TikTok automation is unofficial and may violate TikTok's terms of service.
    # Be cautious when using unofficial APIs.

def post_to_twitch(video_path, title, description):
    # Implement Twitch API integration using the provided credentials.
    # Refer to Twitch API documentation for details.

def upload_to_dailymotion(video_path, title, description, tags):
    # Implement Dailymotion API integration using the provided credentials.
    # Refer to Dailymotion API documentation for details.

def post_to_uscreen(video_path, title, description):
    # Implement Uscreen API integration using the provided credentials.
    # Refer to Uscreen API documentation for details.

def post_to_muvi(video_path, title, description):
    # Implement Muvi API integration using the provided credentials.
    # Refer to Muvi API documentation for details.

def upload_video_to_all_platforms(video_path, video_title, video_description, video_tags, message, caption, tags):
    description_with_credit = add_credit(video_description)

    # Call platform-specific functions
    post_to_twitter(video_path, f'{message} {tags} Mr Tanit', video_title)
    upload_to_youtube(video_path, video_title, description_with_credit, video_tags)
    post_to_facebook(video_path, f'{message} {tags} Mr Tanit', video_title)
    post_to_instagram(video_path, f"{caption}\n{tags} #MrTanit", tags)
    post_to_tiktok(video_path, f'{caption} {tags} #MrTanit')
    post_to_twitch(video_path, f'{video_title} - Mr Tanit', f'{description_with_credit}')
    upload_to_dailymotion(video_path, video_title, description_with_credit, video_tags)
    post_to_uscreen(video_path, f'{video_title} - Mr Tanit', description_with_credit)
    post_to_muvi(video_path, f'{video_title} - Mr Tanit', description_with_credit)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Send me a video, and I will share it on multiple platforms.')

def handle_video(update: Update, context: CallbackContext) -> None:
    video_file = update.message.video.file_id
    video_path = f'tmp/{video_file}.mp4'  # Adjust the path as needed

    # Download the video
    video = context.bot.get_file(video_file)
    video.download(video_path)

    # Your video processing logic
    video_title = 'My Awesome Video'
    video_description = 'Watch this amazing video I created.'
    video_tags = ['tag1', 'tag2', 'tag3']
    message = 'Check out my new video!'
    caption = 'New video alert! Check it out.'
    tags = '#tag1 #tag2 #tag3'

    # Call the function to upload to all platforms
    upload_video_to_all_platforms(video_path, video_title, video_description, video_tags, message, caption, tags)

    update.message.reply_text('Your video has been shared on multiple platforms!')

def main() -> None:
    updater = Updater(telegram_token)
    dispatcher = updater.dispatcher

    # Command handlers
    dispatcher.add_handler(CommandHandler("start", start))

    # Message handler for videos
    dispatcher.add_handler(MessageHandler(Filters.video, handle_video))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
