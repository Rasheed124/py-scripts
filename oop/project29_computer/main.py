
from computer import Computer


def main():
    # Create a computer
    computer = Computer(
        "Dell", "XPS 15", "Intel Core i7", 16, 512, "SSD"
    )

    print("Computer brand:", computer.display_info())

    # Display configuration
    print("Model:", computer.model)
    print("Processor:", computer.configuration.processor)
    print("RAM:", computer.configuration.ram_gb, "GB")
    print("Storage:", computer.configuration.storage_gb, "GB")
    print("Storage type:", computer.configuration.storage_type)

    # Test upgrade_ram()
    computer.upgrade_ram(32)

    print("\nAfter RAM upgrade:")
    print("RAM:", computer.configuration.ram_gb, "GB")


if __name__ == "__main__":
    main()
