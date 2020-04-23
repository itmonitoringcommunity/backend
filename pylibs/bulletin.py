from .mail import CustomMail

mail = CustomMail()


class CustomBulletin():
    def __init(self):
        self.htmltext = ''
        self.msg = ''

    def set_bulletin_text(self, bulletin):
        self.htmltext = '''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Bulletin</title>
</head>
<body style="text-align: center;">
    <div style="display: inline-block; " id="root">
        <table border="1" width="500px">
            <tr>
                <td colspan="2" style="margin: 10px; padding: 10px; text-align: right;">
                    {0.insert_time}
                </td>
            </tr>
            <tr>
                <td colspan="2" style="margin: 10px; padding: 10px;  text-align: center;">
                    <span style="color: {0.color}; font-weight: bold;">{0.code} - {0.title}</span>
                </td>
            </tr>
            <tr>
                <td style=" text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Type
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {0.btype}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Created By
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px; ">
                    {0.created_by}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Detail
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {0.detail}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Effect
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {0.effect}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Contact
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {0.contact}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Begin Time
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {0.begin_time}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    End Time
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {0.end_time}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 
                150px;">
                    Duration
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {0.duration} (Min.)
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Ticket Case Id
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    <a href="{0.ticket_case_url}" style="text-decoration:none;"> {0.ticket_case_id}</a>
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Priority
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {0.priority}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    State
                </td>
                <td style="text-align: left; margin: 10px; padding: 10px; color: #ffffff; background-color: {0.color};">
                    <span> {0.state} </span>
                </td>
            </tr>
        </table>
        <br />
        
        © 2020 smiley-py, Inc.
    </div>
</body>
</html>
'''.format(bulletin)

    def send_bulletin(self,bulletin):
        self.set_bulletin_text(bulletin)

        kwargs_mail = {
            'smtp': str(bulletin.smtp),
            'port': str(bulletin.port),
            'username': str(bulletin.username),
            'password': str(bulletin.password),
            'tolist': str(bulletin.tolist),
            'cclist': str(bulletin.cclist),
            'bcclist': str(bulletin.bcclist),
            'subject': str(bulletin.code) + str(' - ') + str(bulletin.title),
            'body': str(self.htmltext)
        }

        mail.send_mail(kwargs_mail)
        self.msg = mail.msg
