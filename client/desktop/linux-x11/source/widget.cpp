#include "widget.h"

void Widget::InitializeConnections()
{
    connect(HelloScreen, &Authorizer::successfullyAuthorized,
            this, &Widget::OnAuthentication,
            Qt::DirectConnection);
}

void Widget::set_server_addres(const QString &newServer_addres)
{
    server_addres = newServer_addres;
}

Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    AuthorizeControl = new QStackedLayout(this);
    HelloScreen = new Authorizer(server_addres, this);
    
    EventsAndUI = new QWidget();
    EventsAndUILayout = new QHBoxLayout(EventsAndUI);
    UI = new UserInterface();
    recentEvents = new QListView(); //TODO: IMPLEMENT
    EventsAndUILayout->addWidget(recentEvents, 1);
    EventsAndUILayout->addWidget(UI, 9);
    
    AuthorizeControl->addWidget(HelloScreen);
    AuthorizeControl->addWidget(EventsAndUI);
    
    InitializeConnections();
}

Widget::~Widget()
{}

//TODO: IMPLEMENT
void Widget::OnAuthentication(QByteArray data)
{
    AuthorizeControl->setCurrentIndex(1);
    DEBUG(data);
}

