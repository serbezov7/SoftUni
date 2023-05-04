class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return True if len(name) >= self.min_length else False

    def __is_mail_valid(self, mail):
        return True if mail in self.mails else False

    def __is_domain_valid(self, domain):
        return True if domain in self.domains else False

    def validate(self, email):
        name, rest = email.split("@")
        mail, domain = rest.split(".")
        self.__is_name_valid(name)
        self.__is_mail_valid(mail)
        self.__is_domain_valid(domain)
        return True if self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain) \
            else False

