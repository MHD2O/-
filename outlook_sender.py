import os
import win32com.client as win32


class OutlookSender:

    def __init__(self):
        self.outlook = win32.Dispatch("Outlook.Application")

    def send_email(
        self,
        recipient,
        subject,
        body,
        attachment_path=None
    ):

        mail = self.outlook.CreateItem(0)

        mail.To = recipient
        mail.Subject = subject
        mail.Body = body

        if attachment_path:

            if os.path.exists(attachment_path):
                mail.Attachments.Add(os.path.abspath(attachment_path))

        mail.Send()

        return True
