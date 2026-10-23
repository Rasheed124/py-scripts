
class Computer:

    def __init__(self, brand, model, processor, ram_gb,
                 storage_gb, storage_type):
        self.brand = brand
        self.model = model
        self.configuration = self.Configuration(
            processor, ram_gb, storage_gb, storage_type
        )

    class Configuration:
        def __init__(self, processor, ram_gb, storage_gb, storage_type):
            self.processor = processor
            self.ram_gb = ram_gb
            self.storage_gb = storage_gb
            self.storage_type = storage_type

    def display_info(self):
        return f"{self.brand} {self.model}"

    def upgrade_ram(self, new_ram):
        self.configuration.ram_gb = new_ram
