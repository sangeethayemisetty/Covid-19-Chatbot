import configparser

class ConfigReader:
    def __init__(self):
        self.filename = 'config.ini'
    def read_config(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.filename)
        self.configuration=self.config['DEFAULT']
        self.sender_email=self.configuration['sangeethayemisety369@gmail.com']
        self.password = self.configuration['Gmail@369']
        self.email_body = self.configuration['EMAIL_BODY']
        self.email_subject = self.configuration['Covid report']

        return self.configuration