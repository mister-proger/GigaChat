#include "userinterface.h"

void UserInterface::constructWindowArray()
{
    tabs = 
    {
        std::make_tuple( QIcon(":resources/icon1.png"), "Tab with scrolling windows", new ScrollingWidget()     ),
        std::make_tuple( QIcon(":resources/icon2.png"), "Tab that is actually twitch", new GridScrollingWidget()),
        std::make_tuple( QIcon(":resources/icon3.png"), "Tab that i don't know what the...", new UndefinedPage())
    };
}
void UserInterface::constructTabWidget()
{
    for(const auto& [Icon, Title, Widget] : tabs)
        addTab(Widget, Icon, Title);
    setTabPosition(TabPosition::South);
    setElideMode(Qt::ElideMiddle);
    
}

UserInterface::UserInterface(QWidget *parent) : QTabWidget{parent}
{
    constructWindowArray();
    constructTabWidget();
    
}
