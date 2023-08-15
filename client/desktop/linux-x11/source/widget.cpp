#include "widget.h"

void Widget::InitializeConnections()
{
    qDebug() << __PRETTY_FUNCTION__;

    connect(HelloScreen, &Authorizer::AuthenticationComplete,
            this, &Widget::OnAuthentication,
            Qt::QueuedConnection); //IF I ENABLE MULTITHREADING
}

Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    AuthorizeControl = new QStackedLayout(this);
    HelloScreen = new Authorizer();
    AuthorizeControl->addWidget(HelloScreen);
    AuthorizeControl->addWidget(temporar);
    InitializeConnections();
}

Widget::~Widget()
{
    qInfo() << "destroyed" << this;
}

void Widget::OnAuthentication(bool success)
{
    qDebug() << "today is a good day, since \e[31mON_AUTHENTICATION function works!\e[0m";
    qDebug() << (success ? "\e[96mDA SUCCESS\e[0m" : "\e[96mDA NOT SUCCESS\e[0m");
    AuthorizeControl->setCurrentIndex(success);
}

