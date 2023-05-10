import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom


def show_input_notification():
    toast_xml = dom.XmlDocument()
    toast_xml.load_xml("""
        <toast>
            <visual>
                <binding template="ToastGeneric">
                    <text>Введите свое имя:</text>
                    <input id="name" type="text" placeholderContent="Имя"/>
                </binding>
            </visual>
        </toast>
    """)

    toast = notifications.ToastNotification(toast_xml)
    manager = notifications.ToastNotificationManager.create_toast_notifier()
    manager.show(toast)

    return None


while True:

    input()

    show_input_notification()
