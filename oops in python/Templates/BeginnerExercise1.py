class Notification:
    def __init__(self, content):
        self.content = content

    def send(self):
        print(f"Notification sent: {self.content}")


# Example usage
if __name__ == "__main__":
    # Text message
    text_alert = Notification("Disk space low")
    text_alert.send()

    # Numeric code
    code_alert = Notification(404)
    code_alert.send()

    # Boolean status
    status_alert = Notification(True)
    status_alert.send()
