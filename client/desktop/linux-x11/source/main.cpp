#include "widget.h"

#include <QApplication>
#include <QTranslator>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Widget w;
    
    if (argc > 1)
    {
        QString server = argv[1];
        w.set_server_addres(server);
    }
    
    w.show();
    return a.exec();
}
