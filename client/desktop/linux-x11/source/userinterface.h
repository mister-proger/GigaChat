#pragma once

//custom widgets
#include "mainwidgets/gridscrollingwidget.h"
#include "mainwidgets/scrollingwidget.h"
#include "mainwidgets/undefinedpage.h"

#include <QObject>

//utility
#include <array>
#include <utility>
#include <tuple>
#include <QString>

//widgets
#include <QWidget>
#include <QTabWidget>

class UserInterface : public QTabWidget
{
    Q_OBJECT
    
    typedef std::tuple<QIcon, QString, QWidget*> window_type;
    
    std::array< window_type, 3 > tabs;

public:
    void constructWindowArray();
    void constructTabWidget();
    UserInterface(QWidget* parent = nullptr);
};

