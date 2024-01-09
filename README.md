# Telegram Video Sharing Bot

This Telegram bot automates the process of sharing videos on various social media platforms. Users can send a video to the bot, and it will post the video with a universal credit line on platforms like YouTube, Twitter, Facebook, Instagram, TikTok, Twitch, Dailymotion, Uscreen, and Muvi.

## Features

- **Universal Credit:** Every video description includes a credit line: "Mr Tanit - Subscribe for more content!"
- **Multi-Platform Sharing:** Videos are shared on multiple social media platforms.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/telegram-video-bot.git
    ```

2. **Install Dependencies:**

    ```bash
    pip install python-telegram-bot tweepy google-api-python-client facebook-sdk instabot
    ```

3. **Configure Credentials:**

    - Replace `'your_telegram_token'` with your actual Telegram bot token.
    - Replace placeholder values for Twitter, YouTube, Facebook, Instagram, TikTok, Twitch, Dailymotion, Uscreen, and Muvi with your API keys and tokens.

4. **Run the Bot:**

    ```bash
    python bot.py
    ```

## Usage

1. Start the bot by sending the `/start` command.
2. Send a video to the bot, and it will process and share it on various platforms.

## Contributing

Contributions are welcome! Feel free to open issues or create pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
