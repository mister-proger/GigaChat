#pragma once

#include <QObject>

//utility
#include <array>
#include <utility>
#include <QString>

//widgets
#include <QWidget>
#include <QTabWidget>

class UserInterface : public QWidget
{
    Q_OBJECT
    
    typedef std::tuple<QIcon, QString, QWidget*> window_type;
    
    std::array< window_type, 3 > tabs;
public:
    void constructWindowArray();
    void constructTabWidget();
    UserInterface(QWidget* parent = nullptr);
};

