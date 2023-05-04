from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class AddingService:
    services = {
        "MainService": MainService,
        "SecondaryService": SecondaryService,
    }

    def add_new_service(self, service_type, name):
        if service_type in self.services:
            return self.services[service_type](name)

        raise Exception("Invalid service type!")