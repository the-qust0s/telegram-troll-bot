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
          
          

with open("config.toml") as file:
     config = toml.load(file)["session"]

session_name = config["session_name"]
api_id = config["api_id"]
api_hash = config["api_hash"]
device_model = config["device_model"]
system_version = config["system_version"]

