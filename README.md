## pytelog

Simple logger which dispatch messages to a telegram in markdown format. Uses a separate thread for a dispatching.
Support many chats. Support big messages (over 4096 chars). Support telegram API calls restrictions.

## Installation

    pip install pytelog
    
## Quick start

#### 1. Configuration

    config = {
        ...
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "telegram": {
                "class": "pytelog.Handler",
                "token": "bot_token",
                "chat_ids": [123456789, -1234567891011],

            }
        },
        "loggers": {
            "telegram": {
                "level": "INFO",
                "handlers": ["telegram",]
            }
        }
    }
    
#### 2. Usage

    import logging
    logger = logging.getLogger("telegram")

    logger.info("Message")
        
#### 3. Formatting:

    config = {
        ...
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "telegram": {
                "()": "pytelog.MarkdownFormatter",
            }
        },
        ...
    }