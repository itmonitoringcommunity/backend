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
                    {bulletin.insert_time}
                </td>
            </tr>
            <tr>
                <td colspan="2" style="margin: 10px; padding: 10px;  text-align: center;">
                    <span style="color: {bulletin.color}; font-weight: bold;">{bulletin.code} - {bulletin.title}</span>
                </td>
            </tr>

            <tr>
                <td style=" text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Type
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {bulletin.btype}
                </td>
            </tr>

            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Created By
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px; ">
                    {bulletin.created_by}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Detail
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {bulletin.detail}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Effect
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {bulletin.effect}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Contact
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {bulletin.contact}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Begin Time
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {bulletin.begin_time}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    End Time
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {bulletin.end_time}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Duration
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {bulletin.duration} (Min.)
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Ticket Case Id
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    <a href="{bulletin.ticket_case_url}" style="text-decoration:none;"> {bulletin.ticket_case_id}</a>
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Priority
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {bulletin.priority}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    State
                </td>
                <td style="text-align: left; margin: 10px; padding: 10px; color: #ffffff; background-color: {kwargs[color]};">
                    <span> {bulletin.state} </span>
                </td>
            </tr>
        </table>

        <br />

        <table border="1" width="500px">
            <tr>
                <td colspan="2" style="margin: 10px; padding: 10px; text-align: right;">
                    {bulletin.resolved_time}
                </td>
            </tr>
            <tr>
                <td colspan="2"
                    style="color:#ffffff; background-color: #1985ac; margin: 10px; padding: 10px;  text-align: center; ">
                    <span style=" font-weight: bold;">Resolution</span>
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Resolved By
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {bulletin.resolved_by}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Temporary Solution
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {bulletin.temporary_solution}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Permanent_solution
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {bulletin.permanent_solution}
                </td>
            </tr>
            <tr>
                <td style="text-align: left; margin: 10px; padding: 10px; width: 150px;">
                    Root Cause
                </td>
                <td style=" text-align: left; margin: 10px; padding: 10px;">
                    {bulletin.root_cause}
                </td>
            </tr>

        </table>
        <br />
        © 2020 smiley-py, Inc.
    </div>

</body>

</html>
'''.format(kwargs=kwargs_bulletin)

    def send_bulletin(self):
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
            'body': self.htmltext
        }

        mail.send_mail(kwargs_mail)
        print(mail.msg)
