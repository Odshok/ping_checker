from pyexpat.errors import messages

import bot_notification


def statusChange (currentStatus, newStatus, serverName, serverInfo: str = ""):
    if currentStatus != newStatus:
        if newStatus == True:
            # Соединение восстановлено
            status = "Соединение восстановлено! "
        else:
            # Соединение разорвано
            status = "Соединение разорвано!"

        message_from_tg = status + "server:" + serverName + " " + serverInfo
        bot_notification.send_error_message(message_from_tg)