import toml

class FunctionSettings:

      def __init__(self):
      
          with open("words.txt", "r") as file:
               self.words = file.read().split("\n")

          with open("config.toml") as file:
               config = toml.load(file)["settings"]

          self.min_time = config["min_time"]
          self.max_time = config["max_time"]

          self.strings = config["strings"]
          
          

class SessionSettings:

      def __init__(self):
      
          with open("config.toml") as file:
               config = toml.load(file)["session"]

          self.session_name = config["session_name"]
          self.api_id = config["api_id"]
          self.api_hash = config["api_hash"]
          self.device_model = config["device_model"]
          self.system_version = config["system_version"]

