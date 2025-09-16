
def process_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as infile:
            content = infile.read()
        modified_content = content.upper()

        output_file = "modified_" + filename

        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"\n✅ File processed successfully!")
        print(f"📂 Modified content saved as: {output_file}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the name and try again.")
    except PermissionError:
        print("🔒 Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


process_file()
