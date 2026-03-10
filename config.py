import os

class Config:
    """Base configuration."""
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    """Development configuration settings."""
    DEBUG = True
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

class ProductionConfig(Config):
    """Production configuration settings."""
    DEBUG = False
    SESSION_COOKIE_SECURE = True

class TestingConfig(Config):
    """Testing configuration settings."""
    DEBUG = True
    TESTING = True
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}.add('txt')  # Adding .txt for testing
