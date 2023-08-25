#include "widget.h"

void Widget::initializeConnections()
{
    connect(helloScreen, &Authorizer::successfullyAuthorized,
            this, &Widget::onAuthentication,
            Qt::DirectConnection);
}
//TODO: IMPLEMENT
void Widget::constructEvents()
{
#ifdef QT_DEBUG
    
#endif
}

void Widget::set_server_addres(const QString &newServer_addres)
{
    server_addres = newServer_addres;
    helloScreen->set_server_address(newServer_addres);
}

Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    authorizeControl = new QStackedLayout(this);
    helloScreen = new Authorizer(server_addres, this);
    
    eventsAndUI = new QWidget();
    eventsAndUILayout = new QHBoxLayout(eventsAndUI);
    UI = new UserInterface();
    recentEvents = new QListWidget();
    eventsAndUILayout->addWidget(recentEvents, 1);
    eventsAndUILayout->addWidget(UI, 9);
    
    authorizeControl->addWidget(helloScreen);
    authorizeControl->addWidget(eventsAndUI);
    
    initializeConnections();
}

Widget::~Widget()
{}

//TODO: IMPLEMENT
void Widget::onAuthentication(QByteArray data)
{
    authorizeControl->setCurrentIndex(1);
    DEBUG(data);
}

void Widget::addRecentEvents(QList<RecentEvent *> REList)
{
    foreach(RecentEvent* re, REList)
    {
        QListWidgetItem* item = new QListWidgetItem();
        recentEvents->addItem(item);
        recentEvents->setItemWidget(item, re);
    }
}

