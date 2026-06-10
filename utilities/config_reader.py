class ConfigReader:

    config = {}

    @classmethod
    def load_config(cls):

        with open("config/config.properties") as file:

            for line in file:

                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    cls.config[key] = value

    @classmethod
    def get(cls, key):
        return cls.config.get(key)