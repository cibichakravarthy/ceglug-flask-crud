class Config(object):
	"""
	Common configurations
	"""
class Devecon(Config):
	"""
	Development configurations
	"""
	DEBUG = True
	SQLALCHEMY_ECHO = True
class Procon(Config):
	"""
	Production configuration
	"""
	DEBUG = False
app_config = {
	'development':Devecon,
	'production':Procon
}
