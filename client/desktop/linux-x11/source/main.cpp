#include "widget.h"

#include <QApplication>
#include <QTranslator>

#ifdef QT_DEBUG
    #include <QNetworkAccessManager>
    #include <QNetworkReply>
#endif

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Widget w;
    
    w.show();
    return a.exec();
}
