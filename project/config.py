#services/users/project/config.py

class BaseConfig:
	"""Base configruation"""
	TESTING = False

class DevelopmentConfig(BaseConfig):
	"""Development configruation"""
	pass

class TestingConfig(BaseConfig):
	TESTING = True

class ProductionConfig(BaseConfig):
	pass
	
