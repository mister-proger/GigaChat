#include "userinterface.h"

void UserInterface::constructWindowArray()
{
    tabs = 
    {
        std::make_tuple( QIcon(":resources/icon1.png"), "Tab with scrolling windows", new QWidget()              ),
        std::make_tuple( QIcon(":resources/icon2.png"), "Tab that is actually twitch", new QWidget()             ),
        std::make_tuple( QIcon(":resources/icon3.png"), "Tab that i don't know what the fuck is", new QWidget()  )
    };
}
void UserInterface::constructTabWidget()
{
    for(const auto& [Icon, Title, Widget] : tabs)
    {
        qDebug() << Icon << Title << Widget;
    }
}

UserInterface::UserInterface(QWidget *parent) : QTabWidget{parent}
{
    constructWindowArray();
    constructTabWidget();
}
